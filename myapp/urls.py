from django.urls import path
from .views import MyDataAPIView, MyDataDetailAPIView

urlpatterns = [
    path('mydata/', MyDataAPIView.as_view(), name='mydata-list'),
    path('mydata/<uuid:pk>/', MyDataDetailAPIView.as_view(), name='mydata-detail'),
]
