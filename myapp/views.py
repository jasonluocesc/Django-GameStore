from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from myapp.forms import SignUpForm,ProfileForm,AddgameForm,EditgameForm
from myapp.models import Profile,Game,Purchase,Gameplay,Score
from django.contrib.sites.shortcuts import get_current_site
from django.core.mail import send_mail
from django.template.loader import render_to_string
from django.utils.http import urlsafe_base64_encode,urlsafe_base64_decode
from django.contrib.auth.tokens import PasswordResetTokenGenerator
from django.utils.encoding import force_bytes,force_text
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate
from hashlib import md5
from django.http import Http404
import json
from django.http import HttpResponse,JsonResponse
from django.db.models import F
from django.db.models import Q
import uuid
# Create your views here.


def signup(request):
	if request.method == 'POST':
		#submit form
		form = SignUpForm(request.POST)
		if form.is_valid():
			#save user model
			user = form.save(commit=False)
			user.is_active = False
			user.save()
			#save profile model
			profile = Profile()
			profile.self_description = form.cleaned_data.get('self_description')
			profile.is_gamer = form.cleaned_data.get('is_gamer')
			profile.is_developer = form.cleaned_data.get('is_developer')
			profile.user = user
			profile.save()
			current_site = get_current_site(request)
			#form the link
			message = render_to_string('registration/activation.html',
			{
				'username':user.username,
				'domain':current_site.domain,
				'uid':urlsafe_base64_encode(force_bytes(user.pk)),
				'usertoken':PasswordResetTokenGenerator().make_token(user)
			}
			)
			subject = 'Your email confirmation link (do NOT reply)'
			user.email_user(subject,message)
			return redirect('activation_email_sent')
	else:
		#normal access to the page
		form = SignUpForm()
	return render(request, 'registration/signup.html', {'form':form})
	
def login_user(request):
    form = RegistrationForm()
    logout(request)
    email = password = ''

    if request.POST:
        form = RegistrationForm(request.POST)

   ## rest of the code goes here ##

    context = RequestContext(request, {
        'state': state,
        'email': email,
        'form': form, 
    })

    return render_to_response('registration/login.html', {}, context)
    
def activation_email_sent(request):
	return render(request,'registration/activation_email_sent.html')
	
def activate(request, uid, token):
	try:
		#decode and get the user
		user = User.objects.get(pk=force_text(urlsafe_base64_decode(uid)))
	except:
		#all faults
		return render(request, 'registration/activation_fail.html')
	else:
		#reuse the passwordresettoken
		if PasswordResetTokenGenerator().check_token(user, token) and user.profile.email_confirmed==False:
			user.is_active = True
			user.profile.email_confirmed = True
			user.save()
			user.profile.token = uuid.uuid1()
			user.profile.save()
			login(request,user,backend='django.contrib.auth.backends.ModelBackend')
			return redirect('profile')
		else:
			return render(request, 'registration/activation_fail.html')

@login_required			
def profile(request):
	#get the user for this page
	tmp_user=request.user
	#if new form submitted then save it
	if request.method == 'POST':
		form = ProfileForm(request.POST)
		if form.is_valid():
			#save
			tmp_user.first_name = form.cleaned_data.get('first_name')
			tmp_user.last_name = form.cleaned_data.get('last_name')
			tmp_user.profile.self_description = form.cleaned_data.get('self_description')
			if tmp_user.profile.is_developer==False:
				tmp_user.profile.is_developer = form.cleaned_data.get('is_developer')
			if 'photo' in request.FILES:
				tmp_user.profile.photo = request.FILES['photo']
			tmp_user.save()
			tmp_user.profile.save()
			print(tmp_user.profile.photo.url)
			return render(request,'profile-dev.html',{'form':form, 'success':"Your information was successfully updated"})
	#always return form with saved data if the request is GET
	else:
		form = ProfileForm(initial=
		{
			'first_name':tmp_user.first_name,
			'last_name':tmp_user.last_name,
			'self_description':tmp_user.profile.self_description,
			'is_gamer':tmp_user.profile.is_gamer,
			'is_developer':tmp_user.profile.is_developer
		}
		)
		return render(request,'profile-dev.html',{'form':form, 'success':False})

@login_required
def addgame(request):
	#get the user for this page
	tmp_user=request.user
	if tmp_user.profile.is_developer == False:
		return redirect('index')
	#if form submitted
	if request.method == 'POST':
		form = AddgameForm(request.POST)
		if form.is_valid():
			#save the game
			newgame = form.save(commit=False)
			newgame.developer = tmp_user
			if 'image' in request.FILES:
				newgame.image = request.FILES['image']
			newgame.save()
			return redirect('index')
	#access to the page
	else:
		form = AddgameForm()
	
	return render(request,'add-game.html',{'form':form})
	
@login_required
def editgame(request,gameid):
	#get the user and the game
	tmp_user=request.user
	try:
		tmp_game=Game.objects.get(id=gameid)
	except Game.DoesNotExist:
		raise Http404("invalid game ID")
	#check if matches
	if tmp_game.developer == tmp_user:
		if request.method == 'POST':
			form = EditgameForm(request.POST)
			if form.is_valid():
				tmp_game.description = form.cleaned_data.get('description')
				tmp_game.url = form.cleaned_data.get('url')
				tmp_game.price = form.cleaned_data.get('price')
				tmp_game.valid = form.cleaned_data.get('valid')
				if 'image' in request.FILES:
					tmp_game.image = request.FILES['image']
				tmp_game.save()
				return render(request,'edit-game.html',{'form':form,'success':"Your information was successfully updated",'game':tmp_game})
		else:
			form = EditgameForm(instance = tmp_game)
		return render(request,'edit-game.html',{'form':form,'success':False,'game':tmp_game})
	else:
		raise Http404("Not Your Game")
		
def index(request):
	#return all games
	if request.method == 'POST' and request.POST['game-search']!="":
		allgame = Game.objects.filter(Q(name__icontains=request.POST['game-search']) | Q(description__icontains=request.POST['game-search']))
		keyword = request.POST['game-search']
	else:
		allgame = Game.objects.all()
		keyword= ""
	token = ""
	if request.user.is_authenticated():
		developed = allgame.filter(developer = request.user)
		purchased = allgame.filter(pk__in=list(Purchase.objects.all().filter(customer=request.user, success=True).values_list('game',flat=True)))
		gamelist = developed.union(purchased)
		newgame = allgame.filter(valid=True).difference(gamelist)
		token = request.user.profile.token
	else:
		gamelist=allgame.filter(valid=True)
		newgame=False
	return render(request,'index.html',{'games':gamelist,'newgames':newgame,'keyword':keyword,'token':token})


	
def game(request,gameid):
	try:
		tmp_game=Game.objects.get(id=gameid)
	except Game.DoesNotExist:
		raise Http404("invalid game ID")
	if request.user.is_authenticated:
		tmp_user=request.user
		if Purchase.objects.all().filter(customer=tmp_user, game=tmp_game, success=True):
			allowed = "customer"
		elif tmp_game.developer==tmp_user:
			allowed = "developer"
		else:
			allowed = "not_purchased"
		score = Score.objects.filter(player=tmp_user, game=tmp_game).order_by('score').last()
		if score is None:
			score = 0
		else:
			score = score.score
	else:
		allowed = "anonymous"
		score = 0
	if tmp_game.valid==False and (allowed == "not_purchased" or allowed == "anonymous"):
		raise Http404("game is not valid")
	else:
		return render(request,'game-view.html',{'game':tmp_game,'allowed':allowed,'score':score})

def fetch_game(request,rest=False):
	if rest==True:
		games = list(Game.objects.all().filter(valid=True).values('name','price','description','highest_score','id'))
		print(games)
		return JsonResponse(games,safe=False)
	return JsonResponse({'info':'invalid api'},status=404)
	
@login_required
def purchase(request,gameid):
	sid = 'worldgame'
	secret_key = '5029e6754d52702703ee8d46ae2ca063'
	tmp_user=request.user
	try:
		tmp_game=Game.objects.get(id=gameid)
	except Game.DoesNotExist:
		raise Http404("invalid game")
	if tmp_game.valid==False:
		raise Http404("game is not valid")
	if Purchase.objects.all().filter(customer=tmp_user, game=tmp_game, success=True) or tmp_game.developer==tmp_user:
		return render(request,'payment/game-already-purchased.html',{'gameid':gameid})
	try:
		purchase_history = Purchase.objects.get(customer=tmp_user, game=tmp_game, pending=True)
	except Purchase.DoesNotExist:
		purchase_history = Purchase(customer=tmp_user, game=tmp_game,price=tmp_game.price)
		purchase_history.save()
	checksumstr = "pid={}&sid={}&amount={}&token={}".format(purchase_history.id, sid, purchase_history.price, secret_key)
	# checksumstr is the string concatenated above
	m = md5(checksumstr.encode("ascii"))
	checksum = m.hexdigest()
	# checksum is the value that should be used in the payment request
	return render(request,'purchase-form.html',{
		'site':get_current_site(request).domain,
		'checksum':checksum,
		'pid':purchase_history.id,
		'sid':sid,
		'amount':purchase_history.price,
		'game':tmp_game
	}
	)
	
@login_required
def payment(request,status,gameid):
	secret_key = '5029e6754d52702703ee8d46ae2ca063'
	if request.method == 'GET':
		pid = request.GET['pid']
		ref = request.GET['ref']
		result = request.GET['result']
		checksum = request.GET['checksum']
		checksumstr = "pid={}&ref={}&result={}&token={}".format(pid, ref, result, secret_key)
		m = md5(checksumstr.encode("ascii"))
		if checksum == m.hexdigest() and status==result:
			try:
				purchase_history = Purchase.objects.get(id = pid)
			except Purchase.DoesNotExist:
				raise Http404("payment infomation does not exist")
			purchase_history.ref = ref
			purchase_history.pending = False
			if status == 'success':
				purchase_history.success = True
				purchase_history.save()
				purchase_history.game.sales = F('sales') + 1
				purchase_history.game.save()
				developer_profile = purchase_history.game.developer.profile
				developer_profile.profit = F('profit') + purchase_history.price
				developer_profile.save()
				return render(request,'payment/payment-success.html',{'gameid':gameid})
			else:
				purchase_history.success = False
				purchase_history.save()
				return render(request,'payment/payment-failed.html',{'gameid':gameid})
	raise Http404("payment infomation does not exist")
	

def play(request,gameid):
	if request.user.is_authenticated:
		try:
			tmp_game=Game.objects.get(id=gameid)
		except Game.DoesNotExist:
			raise Http404("invalid game")
		tmp_user=request.user
		if Purchase.objects.all().filter(customer=tmp_user, game=tmp_game, success=True) or tmp_game.developer==tmp_user:
			return redirect(tmp_game.url)
	
	return render(request,'restricted-game.html',{'gameid':gameid})
	

def gamedata(request,gameid):
	if request.user.is_authenticated and request.is_ajax:
		try:
			tmp_game = Game.objects.get(id=gameid)
		except Game.DoesNotExist:
			return JsonResponse({'info':'invalid game'},status=404)
		tmp_user=request.user
		if tmp_game.developer!=tmp_user:
			try:
				purchase_history = Purchase.objects.get(customer=tmp_user,game=tmp_game,success=True)
			except Purchase.DoesNotExist:
				return JsonResponse({'info':'Your game is not correctly purchased'},status=404)
		gameplay = Gameplay.objects.get_or_create(player=tmp_user, game=tmp_game)[0]
	else:
		return JsonResponse({'info':'please submit your Gamestate correctly from our webpage!'},status=404)
	if request.method=='POST':
		json_data=request.body#Json data
		json_dict=json.loads(json_data) #JSON to dict
		gameplay.data = json_dict
		gameplay.save()
		json_response = {'message':'saved'}
	if request.method=='GET':
		if any(gameplay.data):
			json_response=gameplay.data
		else:
			return JsonResponse({'info':'Gamestate could not be loaded'},status=404)

	return JsonResponse(json_response,safe=False)

def score(request,gameid,rest=False):
	if rest==False and request.method=='POST' and request.user.is_authenticated:
		try:
			tmp_game = Game.objects.get(id=gameid)
		except Game.DoesNotExist:
			return JsonResponse({'info':'invalid game'},status=404)
		tmp_user=request.user
		if tmp_game.developer!=tmp_user:
			try:
				purchase_history = Purchase.objects.get(customer=tmp_user,game=tmp_game,success=True)
			except Purchase.DoesNotExist:
				return JsonResponse({'info':'Your game is not correctly purchased'},status=404)
		json_data=request.body#Json data
		json_dict=json.loads(json_data) #JSON to dict
		if (json_dict['score']>tmp_game.highest_score):
			tmp_game.highest_score=json_dict['score']
			tmp_game.save()
		score = Score.objects.create(player=tmp_user, game=tmp_game, score=json_dict['score'])
		score = Score.objects.filter(player=tmp_user, game=tmp_game).order_by('score').last()
		return JsonResponse({'highest':score.score})
	if rest==True and request.method=='GET':
		try:
			tmp_game = Game.objects.get(id=gameid)
		except Game.DoesNotExist:
			return JsonResponse({'info':'invalid game'},status=404)
		if request.GET.__contains__('num'):
			try:
				num = int(request.GET['num'])
			except ValueError:
				return JsonResponse({'info':'invalid parameters'},status=404)
			scores = Score.objects.filter(game=tmp_game).order_by('-score')[:num]
		else:
			scores = Score.objects.filter(game=tmp_game).order_by('-score')[:5]
		res = [{'name':x.player.username,'score':x.score, 'time':x.time} for x in scores]
		return JsonResponse(res,safe=False)
	return JsonResponse({'info':'invalid api'},status=404)


def stat(request,rest=False):
	if rest==True:
		if request.GET.__contains__('token'):
			try:
				user = User.objects.get(profile__token=request.GET['token'])
			except User.DoesNotExist:
				return JsonResponse({'info':'invalid token'},status=404)
			tmp_list = list(Purchase.objects.filter(game__developer=user,success=True).order_by("time").values("game__name","price","time"))
			return JsonResponse(tmp_list,safe=False)
		else:
			return JsonResponse({'info':'token required'},status=404)
		
	if request.user.is_authenticated and request.user.profile.is_developer:
		tmp_list = Purchase.objects.filter(game__developer=request.user,success=True).order_by("-time")
		purchasedict = dict(list())
		for purchase in tmp_list:
			if purchase.game not in purchasedict:
				purchasedict[purchase.game]=[]
			purchasedict[purchase.game].append(purchase)
		return render(request, 'dev-statistics.html', {'purchasedict':purchasedict.items()})
	else:
		return render(request, 'not-dev.html',{})

def error_404(request):
	return render(request,'404.html', {})
	
