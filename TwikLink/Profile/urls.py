from django.urls import path,re_path
from .views import ProfileView,SignUpCutosm,LoginCutosm,HomeView,AccountView,logout_view,UpdataItemView,ResetPasswordView,DoneResetPasswordView,ChangePasswordView,ChangePasswordViewDone

from allauth.account.views import password_reset_from_key

urlpatterns = [
    path('@<username>', ProfileView.as_view(),name='profile'),
    path('signup/', SignUpCutosm.as_view(),name="signup"),
    path('login/', LoginCutosm.as_view(),name="login"),
    path('',HomeView.as_view(),name="home"),
    path('Account/',AccountView.as_view(),name='Account'),
    path('edit/<int:pk>',UpdataItemView.as_view(),name="edit"),

    path('logout/', logout_view, name='logout'),
    path("forgetPassword/",ResetPasswordView.as_view(),name="forgetPassword"),
    path("forgetPassword/Done",DoneResetPasswordView.as_view(),name="DoneforgetPassword"),
    re_path(
        r"^password/reset/keys/(?P<uidb36>[0-9A-Za-z]+)-(?P<key>.+)/$",
        ChangePasswordView.as_view(),
        name="account_reset_password_from_key",
    ),
    path(
        "password/reset/key/done/",
        ChangePasswordViewDone.as_view(),
        name="account_reset_password_from_key_done_gg",
    ),

]

