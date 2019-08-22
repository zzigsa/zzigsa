from django.urls import path, include

from .import views

urlpatterns = [
    path('photographer/<int:id>', views.photographer, name="photographer"),
    path('like/', views.like, name="like"),
    path('uploadproduct/', views.upload, name="upload"),
    path('list/',views.list, name="list"),
    # path('list/', views.upload, name="list"),
    path('photographeredit/', views.photographeredit, name="photographeredit"),
    path('search/', include('haystack.urls')),
]