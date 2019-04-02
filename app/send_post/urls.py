from django.urls import path
from .views import PaperView, SuccessView

urlpatterns = [
    path('send_post/', PaperView.as_view(), name='send_post'),
    path('send_post/success/', SuccessView.as_view(), name='success'),
]
