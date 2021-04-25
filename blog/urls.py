from . import views
from django.urls import path, re_path
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', views.PostList.as_view(), name='home'),
    path('home', views.PostList.as_view(), name='home'),
    path("login/", auth_views.LoginView.as_view(template_name='login.html'), name="login"),
    # path("login/", views.login_request, name="login"),
    path("logout", views.logout_request, name="logout"),
    path("register/", views.register_request, name="register"),
    path('<slug:slug>/', views.post_detail, name='post_detail'),
    # re_path(r'^password_reset/$', auth_views.PasswordResetView.as_view(template_name="password_reset.html"),
    #         name="password_reset"),
    # re_path(r'^password_reset/done/$', auth_views.password_reset_done,
    #         name='password_reset_done'),
    # re_path(r'^reset/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$',
    #         auth_views.password_reset_confirm, name='password_reset_confirm'),
    # re_path(r'^reset/done/$', auth_views.password_reset_complete,
    #         name='password_reset_complete'),
    path('password_reset/done/', auth_views.PasswordResetDoneView.as_view(
        template_name='password_reset_done.html'), name='password_reset_done'),
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(
        template_name="password_reset_confirm.html"), name='password_reset_confirm'),
    path('reset/done/', auth_views.PasswordResetCompleteView.as_view(
        template_name='password_reset_complete.html'), name='password_reset_complete'),

]
