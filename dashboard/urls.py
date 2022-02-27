from django.urls import path  
from .views import AddCard

urlpatterns = [
    path('add-card/' , AddCard.as_view()),

]