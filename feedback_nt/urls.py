from django.urls import path

from comments.views import createCommentView
from users.views import login_view, logout_view, register_view, profile_view, error_404_view, verify_email
from .views import *

urlpatterns = [
    path('', landingPageView, name='home'),
    path('login', login_view, name='login'),
    path('logout', logout_view, name='logout'),
    path('register', register_view, name='register'),
    path('feedbacks', feedbacksView, name='feedbacks'),
    path('feedbacks/create', offerFormView, name='create_feedback'),
    path('feedbacks/<int:pk>/', createCommentView, name='feedback_detail'),
    path('comments/', commentsView, name='create_comment'),
    path('verify-email/<uidb64>/<token>/', verify_email, name='verify-email'),
    path('profile', profile_view, name='profile'),
    path('404', error_404_view, name='error404'),
]
