from django.urls import path
from . import views

urlpatterns = [
    path('', views.review),
    path('all-reviews', views.thank_you)
]
