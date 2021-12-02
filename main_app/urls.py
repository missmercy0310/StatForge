from django.urls import path
from . import views

urlpatterns = [
    path('', views.Home.as_view(), name="home"),
    path('accounts/signup/', views.Signup.as_view(), name="signup"),
    path('accounts/<int:pk>/', views.AccountDetail.as_view(), name='account_detail'),
    path('accounts/<int:pk>/update/', views.AccountUpdate.as_view(), name='account_update'),
    path('rpgs/', views.RPGIndex.as_view(), name="rpg_index"),
    path('rpgs/<int:pk>/', views.RPGDetail.as_view(), name="rpg_detail"),
]