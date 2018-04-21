from django.conf.urls import url
from . import views

app_name = 'quiz'

urlpatterns = [
    # #/dev/
    # url(r'^$', views.IndexTemp),
    url('login/', views.LogInView),
    # url(r'^test2/$', views.test2View),
    ]
