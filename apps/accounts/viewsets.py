from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from django.db.models import Avg, Sum
from django.views.decorators.csrf import csrf_exempt
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


@api_view(['post'])
def password_change(request):
    try:
        data = request.data

        old_password = data.get('oldPassword')

        if not request.user.check_password(old_password):
            raise ValidationError("The password is incorrect.")

        new_password_1 = data.get('newPassword1')
        new_password_2 = data.get('newPassword2')

        if new_password_1 != new_password_2:
            raise ValueError("The new passwords do not match.")

        user = User.objects.get(id=request.user.id)
        user.set_password(new_password_1)
        user.save()

    except ValueError:
        return Response(status=status.HTTP_400_BAD_REQUEST, data={'message': "The new passwords do not match."})
    except ValidationError:
        return Response(status=status.HTTP_400_BAD_REQUEST, data={'message': "Old password is incorrect."})
    else:
        return Response(status=status.HTTP_200_OK, data={'message': "Success!"})


@api_view(['get'])
def check_username(request):
    username = request.GET.get('username')
    exist = User.objects.filter(username=username).exists()
    can_use = not exist
    return Response(status=status.HTTP_200_OK, data={'can_use': can_use})


@api_view(['get'])
def check_displayname(request):
    display_name = request.GET.get('display_name')
    exist = Account.objects.filter(display_name=display_name).exists()
    can_use = not exist
    return Response(status=status.HTTP_200_OK, data={'can_use': can_use})


@api_view(['get'])
def get_best_rating(request):
    accounts = Account.objects.all().annotate(average_rating=Avg('shop_ratings__rating'),
                                              rating_count=Sum('shop_ratings')).order_by('average_rating').values(
        'display_name', 'id', 'average_rating', 'rating_count')[:10]
    return Response(status=status.HTTP_200_OK, data=accounts)
