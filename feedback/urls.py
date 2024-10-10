from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('offers/', views.offers, name='offers'),
    path('problems/', views.problems, name='problems'),
    path('offers/<int:offer_id>/comments/', views.comments, name='comments'),
    path('auth/', views.auth_view, name='auth'),
    path('profile/', views.profile, name='profile'),
    path('404/', views.page_not_found, name='404'),
]
