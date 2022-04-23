from django.urls import path
from app import views

urlpatterns = [
    path('venues/<str:hku_id>/<str:date>', views.InfectiousVenues.as_view(), name="infectious_venues"),
    path('contacts/<str:hku_id>/<str:date>', views.CloseContacts.as_view(), name="close_contacts")
]
