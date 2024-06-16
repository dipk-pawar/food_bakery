from django.urls import path

from apps.accounts import views

urlpatterns = [path("register/", views.RegisterUser.as_view(), name="register")]
