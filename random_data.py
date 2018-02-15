import random

from django.db import transaction

from apps.categories.models import Category
from apps.category_product.models import CategoryProduct
from apps.products.models import Product, ProductImage
from apps.values.models import Value


def random_d(val):
    with transaction.atomic():
        for ran in range(val):
            try:
                original_product_id = random.randint(1, 151)
                product = Product.objects.get(id=original_product_id)
                product.pk = None
                print('product id:', original_product_id, ' new product id: ', product.pk)
                print('product name:', product)
                product.price = random.randint(round(product.price*9/10), round(product.price*11/10))
                print('new price:', product.price)
                product.seller_id = random.randint(1, 53)
                print('new user id:', product.seller_id)
                product.save()

                # product image
                images = ProductImage.objects.filter(product_id=original_product_id)
                print('total images found :', images.count())
                new_images = []
                for image in images:
                    image.pk = None
                    image.product_id = product.id
                    new_images.append(image)
                print('new images count : ', len(new_images))
                ProductImage.objects.bulk_create(new_images)


                # create category product
                cat_pro = CategoryProduct.objects.get(product_id=original_product_id, category__category_type=Category.normal)
                print('category id: {}'.format(cat_pro.pk))
                cat_pro.pk = None
                cat_pro.product_id = product.id
                cat_pro.save()

                # create values
                values = Value.objects.filter(product_id=original_product_id)
                print('total values found :', values.count())
                new_values = []
                for value in values:
                    value.pk = None
                    value.product_id = product.id
                    new_values.append(value)
                print('new value count : ', len(new_values))
                Value.objects.bulk_create(new_values)

                print('new product id: ', product.id)

            except Exception as e:
                print(e)
            print('----------------------------------------------')


