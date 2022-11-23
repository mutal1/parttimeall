from django.urls import path
from .views import Main, Uploadviews

urlpatterns = [
    path('', Main.as_view()),
    path('upload/', Uploadviews.as_view())
]