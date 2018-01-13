from django.conf.urls import url

from apps.accounts.views import EditProfileView
from apps.my_profile.views import ProfileView

urlpatterns = [
    url(r'edit', EditProfileView.as_view()),
    url(r'^profile/', ProfileView.as_view()),
]

