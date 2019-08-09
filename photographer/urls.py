from django.urls import path

from .import views

urlpatterns = [
    path('photographer/<int:id>', views.photographer, name="photographer"),
    path('like/', views.like, name="like"),
    path('uploadproduct/', views.upload, name="upload"),
    # path('list/', views.upload, name="list"),
]