from django.urls import path
from django.contrib.auth import views  as auth_view
from .views import signup, signin, logout_view, profile



app_name = 'user'
urlpatterns = [
    path('signup/', signup, name = 'signup'),
    path('login/', signin, name='login'),
    path('logout/', logout_view, name='logout'),
    path('profile/', profile, name = 'profile')

    # path('password_reset/', auth_view.PasswordResetView.as_view(), name='password_reset'),
    # path('password_reset/done/', auth_view.PasswordResetDoneView.as_view(), name = 'password_reset_done'),``
    # path('reset/<uidb64>/<token>/', auth_view.PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    # path('reset/done', auth_view.PasswordResetCompleteView.as_view(), name="password_reset_complete")
]