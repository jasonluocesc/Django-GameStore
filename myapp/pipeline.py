from urllib.request import urlopen
from myapp.models import Profile
from django.core.files.base import ContentFile
import os
import uuid
def profile(backend, user, response, is_new, *args, **kwargs):
	if is_new:
		profile = Profile()
		profile.user = user
		url = 'http://graph.facebook.com/{0}/picture?type=large'.format(response.get('id'))
		profile.photo.save(user.username+"-facebook", ContentFile(urlopen(url).read()))
		user.profile.token = uuid.uuid1()
		profile.save()