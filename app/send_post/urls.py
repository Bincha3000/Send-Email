from django.urls import path
from .views import PaperView



urlpatterns = [
    path('send_post/', PaperView.as_view(), name='send_post'),
]
