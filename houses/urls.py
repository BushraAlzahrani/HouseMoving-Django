from django.urls import path
from . import views


urlpatterns = [
    # house
    path("house/add", views.add_house, name="add_house"),
    path("house/all", views.list_house, name="list_house"),
    path("house/update/<house_id>", views.update_house, name="update_house"),
    path("note/delete/<house_id>", views.delete_house, name="delete_house"),

    # house belongings
    path("belonging/add", views.add_belonging, name="add_belonging"),
    path("belonging/all", views.list_belonging, name="list_belonging"),
    path("belonging/update/<belong_id>", views.update_belonging, name="update_belonging"),
    path("belonging/delete/<belong_id>", views.delete_belonging, name="delete_belonging"),

    # Appointments
    path("appointment/add", views.add_appointment, name="add_appointment"),
    path("appointment/all", views.list_appointment, name="list_appointment"),
    path("appointment/update/<appo_id>", views.update_appointment, name="update_appointment"),
    path("appointment/delete/<appo_id>", views.delete_appointment, name="delete_appointment"),
    path("appointment/user", views.user_appointment, name="user_appointment"),

    # Moving Trucks
    path("truck/all", views.list_truck, name="list_truck"),


]
