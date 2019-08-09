from django.urls import path

from .import views

urlpatterns = [
    path('id_find/', views.id_find, name="id_find"),
    path('mypage/<int:id>', views.mypage,name="mypage"),
    path('change_user/', views.change_user, name="change_user"),
]