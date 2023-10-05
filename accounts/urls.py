from django.urls import include, path
from django.contrib.auth import views  as auth_view 
from . import views 

urlpatterns = [
   # path('', include("django.contrib.auth.urls")),

path('profile/',views.profile, name='profile') ,
path('register/', views.register_user, name='register.html'),



 path('login/',auth_view.LoginView.as_view(), name='login') ,
path('logout/', auth_view.LogoutView.as_view(template_name='registration/logged_outt.html'),name='logged_outt'),
path('password_change/',auth_view.PasswordChangeView.as_view(template_name='registration/password_change.html'), name='password_change') ,
path('password_change_done/',auth_view.PasswordChangeDoneView.as_view(template_name='registration/password_change_done.html'), name='password_change_done') ,
 
 
 
 path('password_reset_form/', auth_view.PasswordResetView.as_view(), name='password_reset_form'),
path('password_reset_done/', auth_view.PasswordResetDoneView.as_view(), name='password_reset_done'),
    path('password_reset_form/<uidb64>/<token>/', auth_view.PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    path('password_reset_complete/', auth_view.PasswordResetCompleteView.as_view(), name='password_reset_complete'),
    
]

 

    
