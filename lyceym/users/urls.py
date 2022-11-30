from django.contrib.auth.views import LogoutView, LoginView, PasswordChangeView
from django.contrib.auth.views import PasswordChangeDoneView, PasswordResetView
from django.contrib.auth.views import PasswordResetConfirmView
from django.contrib.auth.views import PasswordResetCompleteView
from django.urls import path
from .views import registrations, profile, users_list, user_detail


app_name = 'users'


urlpatterns = [
    path('login/', LoginView.as_view(
        template_name='user/login.html'),
        name='login'),
    path('logout/', LogoutView.as_view(
        template_name='user/logout.html'),
        name='logout'),
    path('password_change/', PasswordChangeView.as_view(
        template_name='user/password_change.html'),
        name='passwordchange'),
    path('registration/', registrations, name='registration'),
    path('password_change/done/', PasswordChangeDoneView.as_view(
        template_name='user/password_change_done.html'),
        name='passwordchangedone'),
    path('profile/', profile, name='profile'),
    path('password_reset/', PasswordResetView.as_view(
        template_name='user/password_reset.html'),
        name='passwordreset'),
    path('password_reset/done/', PasswordResetView.as_view(
        template_name='user/password_reset_done.html'),
        name='passwordresetdone'),
    path('reset/<uidb64>/<token>/', PasswordResetConfirmView.as_view(
        template_name='user/reset.html'),
        name='reset'),
    path('reset/done/', PasswordResetCompleteView.as_view(
        template_name='user/done.html'),
        name='done'),
    path('user_list/', users_list, name='users_list'),
    path('user_detail/<int:pk>/', user_detail, name='users_detail'),
]
