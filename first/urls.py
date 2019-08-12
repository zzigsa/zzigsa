from django.urls import path,include

from .import views

urlpatterns = [
    path('customer_login/',views.customer_login, name="customer_login"),
    path('join/',views.join, name="join"),
    path('enroll/<int:id>',views.enroll, name="enroll"),    
    path('signout/',views.signout, name="signout"),
    path('confirm/', views.confirm_email, name="confirm_email"),
    path('email_sent/', views.email_sent, name="email_sent"),
    path('bestphoto/',views.bestphoto, name="bestphoto"),
    path('recommend/',views.recommend,name="recommend"),
]