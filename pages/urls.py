
# In your urls.py, you will need to add the new class-based views:
from django.urls import path
from .views import UsersView, RegisterUserView

urlpatterns = [
    path('users/', UsersView.as_view(), name='users'),
    path('register_user/', RegisterUserView.as_view(), name='register_user'),
]

