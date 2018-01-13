from django.conf.urls import url

from apps.accounts.views import EditProfileView, ChangePassWordView
from apps.my_profile.views import ProfileView

urlpatterns = [
    url(r'edit', EditProfileView.as_view()),
    url(r'^profile/', ProfileView.as_view()),
    url(r'^change_password/', ChangePassWordView.as_view()),
]

