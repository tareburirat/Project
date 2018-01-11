from django.views.generic import TemplateView

# Create your views here.


class SignUpView(TemplateView):
    template_name = 'signup.html'


class EditProfileView(TemplateView):
    template_name = "edit_profile.html"
