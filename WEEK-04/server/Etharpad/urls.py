from django.urls import path
from .views import Etherpad_Access
urlpatterns = [
     path('etherpad/',Etherpad_Access.as_view())
]
