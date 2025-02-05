from django.urls import path, include
from . import views

urlpatterns = [
    path("api/classify-number", views.ClassifyNumber.as_view()),
]