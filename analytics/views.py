from django.shortcuts import render
from django.db.models import Sum, Count
from django.db import connection
from orders.models import *
from products.models import *

# Create your views here.
def analytics(request):
    """
    It gets the total number of orders, total sales and total products. It also gets the total sales per
    month, total number of orders per product, total number of products per category and total sales per
    product
    
    :param request: This is the request object that is sent to the view
    :return: The total number of orders, total sales, total products, total sales per month, total
    number of orders per product, total number of products per category and total sales per product.
    """

    template_name = "analytics/analytics.html"

    # Get total count
    # This is just a simple query to get the total number of orders, total sales and total products.
    total_orders = Orders.objects.all().count()
    total_sales = Orders.objects.filter(status="Done").aggregate(Sum('total_amount'))
    total_products = Products.objects.filter(status=True).count()

    # Getting the total sales per month.
    truncate_month = connection.ops.date_trunc_sql('month', 'date_ordered')
    total_monthly_sales = Orders.objects.extra({'month' : truncate_month}).values('month').filter(status="Done").annotate(Sum('total_amount'))

    # Getting the total number of orders per product.
    total_orders_per_products = Orders.objects.filter(status__in=['Done', 'Pending', 'Cancelled', 'Late']).values('products_id__product_name').annotate(Sum('no_of_order'))

    # Getting the total number of products per category.
    total_product_per_category = Products.objects.filter(status=True).values('category_id__category').annotate(Count('category'))
    
    # Getting the total sales per product.
    total_sales_per_product = Orders.objects.filter(status="Done").values('products_id__product_name').annotate(Sum('total_amount'))


    context = {
        "total_orders" : total_orders,
        "total_sales" : total_sales,
        "total_products": total_products,
        'total_monthly_sales' : total_monthly_sales,
        'total_orders_per_products' : total_orders_per_products,
        'total_product_per_category' : total_product_per_category,
        'total_sales_per_product' : total_sales_per_product
    }
    return render(request, template_name, context)

    