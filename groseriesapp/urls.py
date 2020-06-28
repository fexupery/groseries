from django.urls import path
from . import views
from django.conf.urls.static import static
from django.conf import settings

app_name = 'groseriesapp' #to reference all urls to groseries and avoid mistakes with urls to others apps

urlpatterns = [
    path('all_groseries', views.all_groseries, name='all_groseries'),
    path('signupuser',views.signupuser,name='signupuser'),
    path('logoutuser',views.logoutuser,name='logoutuser'),
    path('loginuser',views.loginuser,name='loginuser'),
    path('addproduct', views.addProduct, name='addproduct'),

]
