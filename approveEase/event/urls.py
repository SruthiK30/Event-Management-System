from django.urls import path
from . import views

urlpatterns = [
    path('base/',views.base, name="base"),
    path('eventlist/',views.eventlist,name="events"),
    path('create_event/',views.create_event,name="eventcreate"),
    path('delete_event/<int:id>/', views.delete_event, name="eventdelete"),  # Delete event URL
]