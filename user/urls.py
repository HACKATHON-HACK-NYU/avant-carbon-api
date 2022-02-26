from django.urls import path  
from .views import UserLogin, UserSignUp

urlpatterns = [
    path('user-signup/' , UserSignUp.as_view()),
    path('user-login/' , UserLogin.as_view()),

]