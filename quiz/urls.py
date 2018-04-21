from django.conf.urls import url
from . import views

app_name = 'quiz'

urlpatterns = [
    # #/dev/
    url(r'^$', views.LogInView, name='login'),
    url(r'^index/$', views.IndexView, name='index'),
    url(r'^profile/$', views.ProfileView, name='profile'),
    url(r'^test/$', views.TestView),
    ]
