from django.urls import path

from PaginaWebApp import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('',views.home, name="Home"),
    path('register/', views.registerPage, name="Register"),
	path('login/', views.loginPage, name="Login"),  
	path('logout/', views.logoutUser, name="Logout"),
   

]

urlpatterns+=static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)