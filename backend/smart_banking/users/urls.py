from django.urls import path
from .views import CreateUserView, LoginView, UserInfoView


urlpatterns = [
    path('users', CreateUserView.as_view(), name='create_user'),
    path('login', LoginView.as_view(), name='login'),
    path('me', UserInfoView.as_view(), name='user_info'),
   
]
