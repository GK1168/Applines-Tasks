from django.urls import path

from .views import ProductList,ProductInfo,ProductQuery,ProductFilter,FetchProducts,Etherpad_Access

urlpatterns = [
    path('prod-list/', ProductList.as_view(),name = 'prod-list' ),
    path('prod-info/<int:id>/', ProductInfo.as_view() ),
    path('prod-query/<str:value>', ProductQuery.as_view() ),
    path('prod-filter/<str:name>/<int:price>',ProductFilter.as_view()),
    path('prod-fetch/',FetchProducts.as_view()),
    path('prod-desc/',Etherpad_Access.as_view())
]