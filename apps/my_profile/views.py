from django.views.generic import TemplateView

# Create your views here.
class MyProfileView(TemplateView):
    template_name = 'my_profile.html'

class ProfileView(TemplateView):
    template_name = 'profile.html'