from django.urls import path
from .views import Login, Signup, Logout

urlpatterns = [
    path('signup', Signup.as_view()),
    path('login', Login.as_view()),
    path('logout', Logout.as_view())
]