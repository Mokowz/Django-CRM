from django.urls import path

from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("logout/", views.logout_user, name="logout"),
    path("signup/", views.register_user, name="signup"),
    path("records/<int:pk>/", views.view_record, name="view_record"),
    path("records/<int:pk>/update/", views.update_record, name="update_record"),
    path("records/<int:pk>/delete/", views.delete_record, name="delete_record"),
    path("add_record/", views.add_record, name="add_record"),
]