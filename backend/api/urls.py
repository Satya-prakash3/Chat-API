from django.urls import (
    path,
    re_path
)

from api.views import (
    Root
)

urlpatterns = [
    path("", Root.as_view(), name="Root View")
]