from django.urls import path, include
from . import views
from .views import offers, comments, problems, home

urlpatterns = [
    path('/', home, name='home'),
    path('offers/', offers, name='offers'),
    path('problems/', problems, name='problems'),
    path('comments/', comments, name='comments'),
    path('feedback/', include('feedback')),
    # path('auth/', include(auth_view), name='auth'),
    # path('profile/', include(profile), name='profile'),
    # path('404/', include(page_not_found), name='404'),
]
