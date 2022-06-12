from django.urls import path
from . import views


urlpatterns = [
    # house
    path("house/add", views.add_house, name="add_house"),
    path("house/all", views.list_house, name="list_house"),
    path("house/update/<house_id>", views.update_house, name="update_house"),
    path("note/delete/<house_id>", views.delete_house, name="remove_note"),

    # house belongings
    path("belonging/add", views.add_belonging, name="add_belonging"),
    path("belonging/all", views.list_belonging, name="list_belonging"),

    # Appointments
    # add_appointment, list_appointment, update_appointment appo_id, delete_appointment appo_id

    # Moving Trucks
    path("truck/all", views.list_truck, name="list_truck"),


]
