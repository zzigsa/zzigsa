from django.urls import path

from .import views

urlpatterns = [
    path('login/',views.login, name="login"),
    path('join/',views.join, name="join"),
    path('enroll/<int:id>',views.enroll, name="enroll"),    
    path('signout/',views.signout, name="signout"),
    path('confirm/', views.confirm_email, name="confirm_email"),
    path('email_sent/', views.email_sent, name="email_sent"),
]