from django.urls import path

from .views import *

urlpatterns = [
    path("", ListBookAPIView.as_view(), name="list_post"),
    path("create/", CreateBookAPIView.as_view(), name="create_post"),
    path("<int:pk>/", DetailBookAPIView.as_view(), name="post_detail"),
    path("search/", SearchView.as_view(), name="search"),
]
