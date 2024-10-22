from django.urls import path
from django.contrib.auth import views as auth_views
from django.urls import reverse_lazy

from .views import LogInView, LogOutView, RegisterView, profile_view

app_name = "account"

urlpatterns = [
    path("login/", LogInView.as_view(), name="login"),
    path("logout/", LogOutView.as_view(), name="logout"),
    path("register/", RegisterView.as_view(), name="register"),
    path("profile/", profile_view, name="profile"),

    path("password_reset/",
         auth_views.PasswordResetView.as_view(
         template_name="account/password_reset.html",
         email_template_name="account/password_reset_email.html",
         success_url=reverse_lazy("account:password_reset_done")),
         name="password_reset"
    ),
    path("password_reset/done/",
         auth_views.PasswordResetDoneView.as_view(
         template_name="account/password_reset_done.html"),
         name="password_reset_done"
    ),
    path('password_reset_confirm/<uidb64>/<token>/',
         auth_views.PasswordResetConfirmView.as_view(
         template_name='account/password_reset_confirm.html',
         success_url=reverse_lazy("account:password_reset_complete")),
         name='password_reset_confirm'
    ),
    path('password_reset_complete/',
         auth_views.PasswordResetCompleteView.as_view(
         template_name='account/password_reset_complete.html'),
         name='password_reset_complete'
    ),

    # path("password_change/",
    #      auth_views.PasswordChangeView.as_view(
    #      template_name="account/password_change.html"),
    #      name="password_change"
    # )

]
