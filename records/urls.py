from django.urls import path

from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("logout/", views.logout_user, name="logout"),
    path("signup/", views.register_user, name="signup"),
    path("records/<int:pk>/", views.view_record, name="view_record"),
]