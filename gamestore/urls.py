"""gamestore URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url,include
from django.contrib import admin
from myapp import views as myviews
from django.views.generic.base import RedirectView
from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls import handler404

urlpatterns = [
    url(r'^admin/', admin.site.urls),
	#all auth views
	url(r'^accounts/', include('django.contrib.auth.urls')),
	url(r'^accounts/signup/$', myviews.signup, name='signup'),
	url(r'^activation_email_sent/$', myviews.activation_email_sent, name='activation_email_sent'),
	url(r'^activate/(\w+)/([\w-]+)/$',myviews.activate,name='activate'),
	url(r'^accounts/profile/$',myviews.profile,name='profile'),
	url(r'^addgame/$',myviews.addgame,name='addgame'),
	url(r'^$',myviews.index,name='index'),
	url(r'^edit/([0-9]+)/$',myviews.editgame, name='editgame'),
	url(r'^game/([0-9]+)/$',myviews.game, name='game'),
	url(r'^purchase/([0-9]+)/$',myviews.purchase, name='purchase'),
	url(r'^payment/(\w+)/([0-9]+)/$',myviews.payment, name='payment'),
	url(r'^play/([0-9]+)/$',myviews.play, name='play'),
	url(r'^social/', include('social_django.urls', namespace='social')),
	url(r'^gamedata/([0-9]+)/$',myviews.gamedata, name='gamedata'),
    url(r'^ratings/', include('star_ratings.urls', namespace='ratings', app_name='ratings')),
	url(r'^stat/$', myviews.stat, name='stat'),
	url(r'^newscore/([0-9]+)/$',myviews.score),
	url(r'^API/score/([0-9]+)/$',myviews.score,{'rest':True}),
	url(r'^API/game/$',myviews.fetch_game,{'rest':True}),
	url(r'^API/sales/$',myviews.stat,{'rest':True}),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

handler404 = myviews.error_404