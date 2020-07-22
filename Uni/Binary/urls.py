from django.urls import path
from . import views


urlpatterns = [
    path('', views.HomePage, name='Home'),
    path('binarycheck/', views.BinaryCheck, name='binarycheck'),
    path('solution/<int:num1>/<int:num2>/', views.Solution, name="solution"),
    path('apiquery/', views.ApiQuery, name='apiquery'),
    path('dataquery/', views.dataquery, name='dataquery'),
    path('top3/', views.Top3, name='top3'),
]
