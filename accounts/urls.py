from django.conf.urls import url

from . import views

urlpatterns = [
    url(r"login/$", views.LoginView.as_view(), name="login"),
    url(r"logout/$", views.LogoutView.as_view(), name="logout"),
    url(r"profile/$", views.ProfileView.as_view(), name="profile"),
    url(r"profile/edit/$", views.EditProfileView.as_view(), name="edit_profile"),
    url(r"signup/$", views.SignUp.as_view(), name="signup"),
]