

from django.conf.urls import url
from . import views
from django.conf import settings
from django.conf.urls.static import static
from rest_framework.authtoken.views import obtain_auth_token

urlpatterns = [
    url(r'^$', views.home, name='home'),
    url(r'register/',views.register, name='register'),
    url('login/', views.loginPage, name="login"),
    url('logout/', views.logoutUser, name="logout"),
    url(r'^user/', views.userPage, name='user'),
    url(r'^addProduct/', views.add_product, name='addProduct'),
    url(r'options/', views.show_options, name='options'),
    url(r'milkData/', views.add_milk, name='milkData'),
    url(r'products/', views.products, name='products'),
    url(r'total/', views.SalaryModel, name='total'),
    url(r'margin/', views.margin, name='margin'),
    url(r'sales/', views.add_user_sales, name='sales'),
]

if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)