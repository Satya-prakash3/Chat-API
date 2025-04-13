from django.urls import path
from .views.views import *

urlpatterns = [
    path("", root.as_view(), name="ChatAPI"),
]