from django.urls import path  
from .views import UserLogin

urlpatterns = [
    # path('user_signup/' , UserSignUp.as_view()),
    path('user_login/' , UserLogin.as_view()),

]