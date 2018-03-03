from django.views.generic import TemplateView

# Create your views here.
class MyProfileView(TemplateView):
    template_name = 'tab_menu_profile.html'

class ProfileView(TemplateView):
    template_name = 'user_information.html'

class PurchaseHistoryView(TemplateView):
    template_name = 'purchase_history.html'


class SalesHistoryView(TemplateView):
    template_name = 'sales_history.html'