from django.urls import path, include
from . import views

app_name = "api_task"

urlpatterns = [
    path("api/get-number/", views.GetNumber.as_view(), name="get_number"),
    path("api/classify-number", views.ClassifyNumber.as_view(), name="classify_number"),
]