from django.urls import path

from . import views

app_name = "type"

urlpatterns = [
    path("", views.TypeListView.as_view(), name="type_list"),
    path("getInfo/<int:pk>", views.TypeDetailView.as_view(), name="type_detail"),

]