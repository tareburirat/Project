from django.views.generic import TemplateView

# Create your views here.
class MyProfileView(TemplateView):
    template_name = 'tab_menu_profile.html'

class ProfileView(TemplateView):
    template_name = 'user_information.html'