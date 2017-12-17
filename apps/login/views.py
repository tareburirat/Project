from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect
from django.shortcuts import redirect
from django.urls import reverse_lazy
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
    authenticated_user = authenticate(
        username=username,
        password=password,
    )

    # wrong username and password, user not logged in
    if authenticated_user is None:
        response_data = {"message": "Failed!!!!"}

    # user logged in
    else:
        response_data = {"message": "Success!!!!"}
        login(request, authenticated_user)

    return Response(status=status.HTTP_200_OK, data=response_data)


def log_out(request):
    logout(request)
    return redirect(reverse_lazy('home'))
