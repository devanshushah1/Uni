from django.urls import path
from . import views


urlpatterns = [
    path('', views.HomePage, name='Home'),
    path('solution/<int:num1>/<int:num2>/', views.Solution, name="solution")
]
