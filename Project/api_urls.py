from rest_framework.routers import DefaultRouter

from apps.accounts.viewsets import AccountViewSet

router = DefaultRouter()
router.register('accounts', AccountViewSet, base_name='account')