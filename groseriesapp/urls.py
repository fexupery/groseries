from django.urls import path
from . import views

app_name = 'groseriesapp' #to reference all urls to groseries and avoid mistakes with urls to others apps

urlpatterns = [
    path('all_groseries', views.all_groseries, name='all_groseries'),
    path('signupuser',views.signupuser,name='signupuser')

]
