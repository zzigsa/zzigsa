from django.urls import path

from .import views

urlpatterns = [
    path('photographer/<int:id>', views.photographer, name="photographer"),
    path('like/', views.like, name="like"),
    path('uploadproduct/<int:id>', views.upload, name="upload"),
    path('list/',views.list, name="list"),
    # path('list/', views.upload, name="list"),
    path('photographeredit/', views.photographeredit, name="photographeredit"),
]