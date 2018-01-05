from rest_framework import viewsets, status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from apps.accounts.models import Account
from apps.accounts.serializers import AccountSerializer


class AccountViewSet(viewsets.ModelViewSet):
    serializer_class = AccountSerializer
    queryset = Account.objects.all()

@api_view(['post'])
def create_account(request):
    data = request.data

    username = data['username']
    password = data['password']
    first_name = data['first_name']
    last_name = data['last_name']
    email = data['email']
    display_name = data['display_name']
    telephone = data['telephone']

    Account.objects.create(
        username=username,
        password=password,
        first_name=first_name,
        last_name=last_name,
        email=email,
        display_name=display_name,
        telephone=telephone
    )

    return Response(status=status.HTTP_200_OK, data={'message': "success!"})

