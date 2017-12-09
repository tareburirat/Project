from django.views.generic import TemplateView
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response


class LoginView(TemplateView):
    template_name = 'login.html'


@api_view(['post', ])
def log_in_user(request):
    data = request.data
    username = data['username']
    password = data['password']
    print(username, password)
    return Response(status=status.HTTP_200_OK)
