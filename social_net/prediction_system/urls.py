from django.urls import path
from .views import index,prediction_detail

app_name='prediction'

urlpatterns =[
    path('',index,name='prediction-index'),
    path('result',prediction_detail,name='prediction-detail'),
]