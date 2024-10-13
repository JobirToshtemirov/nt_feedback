from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

from feedback.views import home, offers, problems, comments, login

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home, name='home'),
    path('offers/', offers, name='offers'),
    path('problems/', problems, name='problems'),
    path('comments/', comments, name='comments'),
    path('login/', login, name='login'),

]


if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)