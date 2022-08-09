from django.urls import re_path


from .views import GenerateOTP, ValidateOTP, CheckUsernameAvailability, AddUserDetailsView, SearchUserView, Profile, \
    ViewProfile

app_name = 'accounts'
STATIC_ROOT = 'Static'

urlpatterns = [
    re_path(r'^generate/$', GenerateOTP.as_view(), name="generate"),
    re_path(r'^validate/$', ValidateOTP.as_view(), name="validate"),
    re_path(r'check_username', CheckUsernameAvailability.as_view(), name="check username"),
    re_path(r'add_profile', AddUserDetailsView.as_view(), name="user_details"),
    re_path(r'search', SearchUserView.as_view(), name="SearchUserView"),
    re_path(r'view_profile/<str:username>', ViewProfile.as_view(), name="view profile"),
    re_path(r'profile', Profile.as_view(), name="Profile"),

]
