import profile

from django.urls import path, include

import feedback
from . import views
from .views import offers, comments, problems, home

urlpatterns = [
    path('/', home, name='home'),
    path('offers/', offers, name='offers'),
    path('problems/', problems, name='problems'),
    path('problems/', views.problems, name='problems'),
    path('comments/', comments, name='comments'),
    path('feedback/',feedback, name ='feedback'),
    path('auth/', auth_view, name='auth'),
    path('profile/', profile, name='profile'),
    path('404/', page_not_found, name='404'),
]
