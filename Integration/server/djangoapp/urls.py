from django.urls import path
from . import views


urlpatterns = [
    # path('',views.getRoutes,name = "routes"),
    path('note/',views.getNotes.as_view()),
    path("note/<int:id>",views.getNote.as_view()),
]
