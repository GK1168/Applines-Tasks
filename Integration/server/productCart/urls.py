from django.urls import path
from . import views


urlpatterns = [
    path('prod-det/',views.getProdDetails.as_view()),
    path('prod-det/<int:id>',views.getProdDet.as_view()),
    path('prod-det/<str:name>',views.SearchProducts.as_view()),
    path('prod-det/<int:id>/<str:operand>',views.ChangeQuantity.as_view()),
    path('prod-deta/',views.ChangeQuantity.as_view()),
    path('chg-con/',views.ChangeContent.as_view()),
    path('chg-con-put/<int:id>',views.ChangeContent.as_view()),
    path('chg-con-del/<int:id>',views.ChangeContent.as_view()),
    
]
