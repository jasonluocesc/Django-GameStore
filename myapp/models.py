from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator, MinValueValidator
from django.contrib.postgres.fields import JSONField
from star_ratings.models import Rating

#django auth user imported
# Create your models here.

#extra fields for user
class Profile(models.Model):
	user = models.OneToOneField(User, on_delete=models.CASCADE)
	self_description = models.TextField(blank=True, max_length = 200)
	email_confirmed = models.BooleanField(default=False)
	is_gamer = models.BooleanField(default=True)
	is_developer = models.BooleanField(default=False)
	photo = models.ImageField(upload_to='user_photos/', default = 'user_photos/default-user.png')
	profit = models.DecimalField(max_digits=10, decimal_places=2, validators=[MinValueValidator(0.00)], default = 0)
	token = models.CharField(max_length=40,blank=True)
	
#model for each added game
class Game(models.Model):
    name = models.CharField(max_length=25)
    description = models.TextField(max_length=1000,blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2, default=0.01, validators=[MinValueValidator(0.005)])
    developer = models.ForeignKey(User, on_delete=models.CASCADE)
    url = models.URLField()
    highest_score = models.FloatField(default=0)
    sales = models.PositiveIntegerField(default=0)
    image = models.ImageField(upload_to='game_pic/', default = 'game_pic/default-game-n.png')
    valid = models.BooleanField(default=True)

#model for saving and loading json data
class Gameplay(models.Model):
    update_time = models.DateTimeField(auto_now=True)
    game = models.ForeignKey(Game, on_delete=models.CASCADE)
    player = models.ForeignKey(User, on_delete=models.CASCADE)
    data = JSONField(default=dict)

#model to save each purchase
class Purchase(models.Model):
	customer = models.ForeignKey(User, on_delete=models.CASCADE)
	game = models.ForeignKey(Game, on_delete=models.CASCADE)
	price = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True, validators=[MinValueValidator(0.00)],default = 0)
	time = models.DateTimeField(auto_now=True)
	success = models.BooleanField(default = False)
	pending = models.BooleanField(default = True)
	ref = models.CharField(max_length=30, blank=True)
	
#all submited scores
class Score(models.Model):
	player = models.ForeignKey(User, on_delete=models.CASCADE)
	game = models.ForeignKey(Game, on_delete=models.CASCADE)
	time = models.DateTimeField(auto_now=True)
	score = models.FloatField(default=0)