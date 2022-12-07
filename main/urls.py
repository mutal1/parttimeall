from django.urls import path
from .views import Main, Uploadviews, List, Hot

urlpatterns = [
    path('', Main.as_view()),
    path('upload/', Uploadviews.as_view()),
    path('list/', List.as_view()),
    path('hottime/', Hot.as_view())
]