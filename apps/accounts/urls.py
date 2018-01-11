from django.conf.urls import url

from apps.accounts.views import EditProfileView

urlpatterns = [
    url(r'edit', EditProfileView.as_view()),
]
