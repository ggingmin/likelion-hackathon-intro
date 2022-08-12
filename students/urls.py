from django.urls import path

from .views import IndexView, StudentListView

urlpatterns = [
    path("", IndexView.as_view(), name='index'),
    path("students/", StudentListView.as_view(), name="list")
]