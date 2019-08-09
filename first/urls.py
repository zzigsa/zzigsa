from django.urls import path,include

from .import views

urlpatterns = [
    path('customer_login/',views.customer_login, name="customer_login"),
    path('join/',views.join, name="join"),
    path('enroll/<int:id>',views.enroll, name="enroll"),    
    path('signout/',views.signout, name="signout"),
    path('confirm/', views.confirm_email, name="confirm_email"),
    path('email_sent/', views.email_sent, name="email_sent"),
<<<<<<< HEAD
    path('accounts/',include('django.contrib.auth.urls')),
    path('bestphoto/',views.bestphoto,name="bestphoto"),
=======
    path('bestphoto/',views.bestphoto, name="bestphoto"),
>>>>>>> 82f4b21d96c5f5d204b295379410cdd20b705d30
    path('recommend/',views.recommend,name="recommend"),
]