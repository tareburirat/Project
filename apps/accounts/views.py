from django.views.generic import TemplateView

# Create your views here.

class SignUpView(TemplateView):
    template_name = 'signup.html'
