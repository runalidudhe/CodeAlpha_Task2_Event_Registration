
from django.urls import path
from .views import (
    EventListCreateView,
    EventDetailView,
    RegistrationCreateView,
    UserRegistrationListView,
)

urlpatterns = [
    path('events/', EventListCreateView.as_view(), name='event-list'),
    path('events/<int:pk>/', EventDetailView.as_view(), name='event-detail'),
    path('register/', RegistrationCreateView.as_view(), name='event-register'),
    path('my-registrations/', UserRegistrationListView.as_view(), name='my-registrations'),
]
