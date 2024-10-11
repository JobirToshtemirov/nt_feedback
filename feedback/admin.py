from django.contrib import admin
from django.urls import path, include

from feedback.views import home, offers, problems, comments

urlpatterns =[
    path('admin/', admin.site.urls),
    path('/', home, name='home'),
    path('offers/', offers, name='offers'),
    path('problems/', problems, name='problems'),
    path('comments/', comments, name='comments'),
]