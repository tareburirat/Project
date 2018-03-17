from django.db.models import Count, Sum
from django.views.generic import TemplateView
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from apps.categories.models import Category


class CategoryDashBoardView(TemplateView):
    template_name = 'admin_dashboard/dashboard.html'


@api_view(http_method_names=['get'])
def category_summary(request):
    request_data = request.GET
    cat_table = Category.objects.all()
    if request_data.get('mode') == 'year':
        cat_table = cat_table.filter(categoryproduct__product__date_of_sale__year=request_data['year'])
    elif request_data.get('mode') == 'month':
        cat_table = cat_table.filter(
            categoryproduct__product__date_of_sale__year=request_data['year'],
            categoryproduct__product__date_of_sale__month=request_data['month']
        )
    elif request_data.get('mode') == 'day':
        cat_table = cat_table.filter(
            categoryproduct__product__date_of_sale__year=request_data['year'],
            categoryproduct__product__date_of_sale__month=request_data['month'],
            categoryproduct__product__date_of_sale__day=request_data['day']
        )
    data = cat_table.filter(category_type=Category.normal) \
        .annotate(product_count=Count('categoryproduct__product_id'),
                  total_price=Sum('categoryproduct__product__price')) \
        .order_by('-product_count').values('id', 'name', 'product_count', 'total_price')
    return Response(status=status.HTTP_200_OK, data=data)
