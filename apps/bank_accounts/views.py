from django.views.generic import TemplateView


class BankAccountPickOrCreate(TemplateView):
    template_name = "bank_accounts/pick_or_create.html"

