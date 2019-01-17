from django.conf.urls import url, include
from django.contrib import admin
from mainAPI import views

urlpatterns = [
    url(r'^$', views.test),
    url(r'^facebookPOST/', views.fbPOST),
    url(r'^twitterPOST/', views.twPOST),
    url(r'^tokenSTATUS/', views.tokenStatus),
]
