import time
from django.shortcuts import render
from django.db.models import Sum, Count
from django.db import connection
from orders.models import *
from products.models import *
from inquiries.models import *
from bookings.models import *
from datetime import datetime
import datetime as dt
from django.db.models import Q
from django.contrib.auth.decorators import login_required
from django.db.models.functions import TruncMonth

# Create your views here.
@login_required(login_url='/accounts/login')
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
    total_orders = Orders.objects.filter(status__in=['Done', 'Pending', 'Cancelled', 'Late']).aggregate(Sum('no_of_order'))
    total_sales = Orders.objects.filter(status="Done").aggregate(Sum('total_amount'))
    total_products = Products.objects.filter(status=True).count()
    # total_inquiries = Inquiries.objects.all().count()
    total_bookings = Bookings.objects.all().count()

    # Getting the total sales per month.
    # truncate_month = connection.ops.date_trunc_sql('month', 'date_ordered')
    total_monthly_sales = Orders.objects.annotate(month=TruncMonth('date_ordered')).values('month').filter(status="Done").annotate(Sum('total_amount'))

    # Getting the total number of orders per product.
    total_orders_per_products = Orders.objects.filter(status__in=['Done', 'Pending', 'Cancelled', 'Late']).values('product_id__product_name').annotate(Sum('no_of_order'))

    # Getting the total number of products per category.
    total_product_per_category = Products.objects.filter(status=True).values('category_id__category').annotate(Count('category'))

    # Getting the total sales per product.
    total_sales_per_product = Orders.objects.filter(status="Done").values('product_id__product_name').annotate(Sum('total_amount'))


    context = {
        "total_orders" : total_orders,
        "total_sales" : total_sales,
        "total_products": total_products,
        'total_monthly_sales' : total_monthly_sales,
        'total_orders_per_products' : total_orders_per_products,
        'total_product_per_category' : total_product_per_category,
        'total_sales_per_product' : total_sales_per_product,
        # 'total_inquiries' : total_inquiries,
        'total_bookings' : total_bookings,
        "analytics_state": "background-color: #dbeafe;"
    }
    return render(request, template_name, context)


@login_required(login_url='/accounts/login')
def analytics_day(request):
    """
    It gets the total number of orders, total sales and total products for a specific day
    
    :param request: This is the request object that is sent to the view
    :return: The total number of orders, total sales and total products.
    """
    template_name = "analytics/analytics_day.html"

    if 'day' in request.GET:
        day = request.GET['day']
        total_orders_range = Q(Q(date_ordered=datetime.strptime(day, '%Y-%m-%d' ).date()) & Q(status__in=['Done', 'Pending', 'Cancelled', 'Late']))
        total_sales_range = Q(Q(date_ordered=datetime.strptime(day, '%Y-%m-%d').date()) & Q(status="Done"))
        total_products_range = Q(Q(created_date=datetime.strptime(day, '%Y-%m-%d').date()) & Q(status=True))
        total_monthly_sales_range = Q(Q(date_ordered=datetime.strptime(day, '%Y-%m-%d').date()) & Q(status="Done"))
        total_orders_per_product_range = Q(Q(date_ordered=datetime.strptime(day, '%Y-%m-%d').date()) & Q(status__in=['Done', 'Pending', 'Cancelled', 'Late']))
        total_product_per_category_range = Q(Q(created_date=datetime.strptime(day, '%Y-%m-%d').date()) & Q(status=True))
        total_sales_per_product_range = Q(Q(date_ordered=datetime.strptime(day, '%Y-%m-%d').date()) & Q(status="Done"))
        # total_inquiries_range = Q(Q(created_date=datetime.strptime(day, '%Y-%m-%d').date()))
        total_bookings_range = Q(Q(created_date=datetime.strptime(day, '%Y-%m-%d').date()))

        total_orders = Orders.objects.filter(total_orders_range).aggregate(Sum('no_of_order'))
        total_sales = Orders.objects.filter(total_sales_range).aggregate(Sum('total_amount'))
        total_products = Products.objects.filter(total_products_range).count()

        # truncate_month = connection.ops.date_trunc_sql('month', 'date_ordered')
        total_monthly_sales = Orders.objects.annotate(month=TruncMonth('date_ordered')).values('month').filter(total_monthly_sales_range).annotate(Sum('total_amount'))
        total_orders_per_products = Orders.objects.filter(total_orders_per_product_range).values('product_id__product_name').annotate(Sum('no_of_order'))
        total_product_per_category = Products.objects.filter(total_product_per_category_range).values('category_id__category').annotate(Count('category'))
        total_sales_per_product = Orders.objects.filter(total_sales_per_product_range).values('product_id__product_name').annotate(Sum('total_amount'))
        # total_inquiries = Inquiries.objects.filter(total_inquiries_range).count()
        total_bookings = Bookings.objects.filter(total_bookings_range).count()
        date = f"as of {day}"
    else:
        # Get total count
        # This is just a simple query to get the total number of orders, total sales and total products.
        day = dt.date.today()
        total_orders_range = Q(Q(date_ordered=day))
        total_sales_range = Q(Q(date_ordered=day) & Q(status="Done"))
        total_products_range = Q(Q(created_date=day) & Q(status=True))
        total_monthly_sales_range = Q(Q(date_ordered__range=[day, day]) & Q(status="Done"))
        total_orders_per_product_range = Q(Q(date_ordered=day) & Q(status__in=['Done', 'Pending', 'Cancelled', 'Late']))
        total_product_per_category_range = Q(Q(created_date=day) & Q(status=True))
        total_sales_per_product_range = Q(Q(date_ordered=day) & Q(status="Done"))
        # total_inquiries_range = Q(Q(created_date=day))
        total_bookings_range = Q(Q(created_date=day))

        total_orders = Orders.objects.filter(total_orders_range).aggregate(Sum('no_of_order'))
        total_sales = Orders.objects.filter(total_sales_range).aggregate(Sum('total_amount'))
        total_products = Products.objects.filter(total_products_range).count()

        # truncate_month = connection.ops.date_trunc_sql('month', 'date_ordered')
        total_monthly_sales = Orders.objects.annotate(month=TruncMonth('date_ordered')).values('month').filter(total_monthly_sales_range).annotate(Sum('total_amount'))
        total_orders_per_products = Orders.objects.filter(total_orders_per_product_range).values('product_id__product_name').annotate(Sum('no_of_order'))
        total_product_per_category = Products.objects.filter(total_product_per_category_range).values('category_id__category').annotate(Count('category'))
        total_sales_per_product = Orders.objects.filter(total_sales_per_product_range).values('product_id__product_name').annotate(Sum('total_amount'))
        # total_inquiries = Inquiries.objects.filter(total_inquiries_range).count()
        total_bookings = Bookings.objects.filter(total_bookings_range).count()
        date = f"as of {day}"

    context = {
        "total_orders" : total_orders,
        "total_sales" : total_sales,
        "total_products": total_products,
        'total_monthly_sales' : total_monthly_sales,
        'total_orders_per_products' : total_orders_per_products,
        'total_product_per_category' : total_product_per_category,
        'total_sales_per_product' : total_sales_per_product,
        # "total_inquiries" : total_inquiries,
        'total_bookings' : total_bookings,
        'date' : date,
        "day" : day,
        "analytics_state": "background-color: #dbeafe;"
    }

    return render(request, template_name, context)

@login_required(login_url='/accounts/login')
def analytics_week(request):
    """
    I'm trying to get the total number of orders, total sales and total products from the database
    
    :param request: The request object is the first parameter to the view function. It contains the
    request data, such as the HTTP method, the URL, the headers, and the body
    :return: The total number of orders, total sales and total products.
    """
    template_name = "analytics/analytics_week.html"

    if 'from_date' in request.GET or  'to_date' in request.GET:
        from_date = request.GET['from_date']
        to_date = request.GET['to_date']
        total_orders_range = Q(Q(date_ordered__range=[datetime.strptime(from_date, '%Y-%m-%d').date(), datetime.strptime(to_date, '%Y-%m-%d').date()]) & Q(status__in=['Done', 'Pending', 'Cancelled', 'Late']))
        total_sales_range = Q(Q(date_ordered__range=[datetime.strptime(from_date, '%Y-%m-%d').date(), datetime.strptime(to_date, '%Y-%m-%d').date()]) & Q(status="Done"))
        total_products_range = Q(Q(created_date__range=[datetime.strptime(from_date, '%Y-%m-%d').date(), datetime.strptime(to_date, '%Y-%m-%d').date()]) & Q(status=True))
        total_monthly_sales_range = Q(Q(date_ordered__range=[datetime.strptime(from_date, '%Y-%m-%d').date(), datetime.strptime(to_date, '%Y-%m-%d').date()]) & Q(status="Done"))
        total_orders_per_product_range = Q(Q(date_ordered__range=[datetime.strptime(from_date, '%Y-%m-%d').date(), datetime.strptime(to_date, '%Y-%m-%d').date()]) & Q(status__in=['Done', 'Pending', 'Cancelled', 'Late']))
        total_product_per_category_range = Q(Q(created_date__range=[datetime.strptime(from_date, '%Y-%m-%d').date(), datetime.strptime(to_date, '%Y-%m-%d').date()]) & Q(status=True))
        total_sales_per_product_range = Q(Q(date_ordered__range=[datetime.strptime(from_date, '%Y-%m-%d').date(), datetime.strptime(to_date, '%Y-%m-%d').date()]) & Q(status="Done"))
        # total_inquiries_range = Q(Q(created_date__range=[datetime.strptime(from_date, '%Y-%m-%d').date(), datetime.strptime(to_date, '%Y-%m-%d').date()]))
        total_bookings_range = Q(Q(created_date__range=[datetime.strptime(from_date, '%Y-%m-%d').date(), datetime.strptime(to_date, '%Y-%m-%d').date()]))


        total_orders = Orders.objects.filter(total_orders_range).aggregate(Sum('no_of_order'))
        total_sales = Orders.objects.filter(total_sales_range).aggregate(Sum('total_amount'))
        total_products = Products.objects.filter(total_products_range).count()

        # truncate_month = connection.ops.date_trunc_sql('month', 'date_ordered')
        total_monthly_sales = Orders.objects.annotate(month=TruncMonth('date_ordered')).values('month').filter(total_monthly_sales_range).annotate(Sum('total_amount'))
        total_orders_per_products = Orders.objects.filter(total_orders_per_product_range).values('product_id__product_name').annotate(Sum('no_of_order'))
        total_product_per_category = Products.objects.filter(total_product_per_category_range).values('category_id__category').annotate(Count('category'))
        total_sales_per_product = Orders.objects.filter(total_sales_per_product_range).values('product_id__product_name').annotate(Sum('total_amount'))
        # total_inquiries = Inquiries.objects.filter(total_inquiries_range).count()
        total_bookings = Bookings.objects.filter(total_bookings_range).count()
        date = f"from {from_date} to {to_date}"
    else:
        # Get total count
        # This is just a simple query to get the total number of orders, total sales and total products.
        from_date = dt.date.today()
        to_date = from_date - dt.timedelta(days=7)
        total_orders_range = Q(Q(date_ordered__range=[from_date, to_date]))
        total_sales_range = Q(Q(date_ordered__range=[from_date, to_date]) & Q(status="Done"))
        total_products_range = Q(Q(created_date__range=[from_date, to_date]) & Q(status=True))
        total_monthly_sales_range = Q(Q(date_ordered__range=[from_date, to_date]) & Q(status="Done"))
        total_orders_per_product_range = Q(Q(date_ordered__range=[from_date, to_date]) & Q(status__in=['Done', 'Pending', 'Cancelled', 'Late']))
        total_product_per_category_range = Q(Q(created_date__range=[from_date, to_date]) & Q(status=True))
        total_sales_per_product_range = Q(Q(date_ordered__range=[from_date, to_date]) & Q(status="Done"))
        # total_inquiries_range = Q(Q(created_date__range=[from_date, to_date]))
        total_bookings_range = Q(Q(created_date__range=[from_date, to_date]))

        total_orders = Orders.objects.filter(total_orders_range).aggregate(Sum('no_of_order'))
        total_sales = Orders.objects.filter(total_sales_range).aggregate(Sum('total_amount'))
        total_products = Products.objects.filter(total_products_range).count()

        # truncate_month = connection.ops.date_trunc_sql('month', 'date_ordered')
        total_monthly_sales = Orders.objects.annotate(month=TruncMonth('date_ordered')).values('month').filter(total_monthly_sales_range).annotate(Sum('total_amount'))
        total_orders_per_products = Orders.objects.filter(total_orders_per_product_range).values('product_id__product_name').annotate(Sum('no_of_order'))
        total_product_per_category = Products.objects.filter(total_product_per_category_range).values('category_id__category').annotate(Count('category'))
        total_sales_per_product = Orders.objects.filter(total_sales_per_product_range).values('product_id__product_name').annotate(Sum('total_amount'))
        # total_inquiries = Inquiries.objects.filter(total_inquiries_range).count()
        total_bookings = Bookings.objects.filter(total_bookings_range).count()
        date = f"from {from_date} to {to_date}"

    context = {
        "total_orders" : total_orders,
        "total_sales" : total_sales,
        "total_products": total_products,
        'total_monthly_sales' : total_monthly_sales,
        'total_orders_per_products' : total_orders_per_products,
        'total_product_per_category' : total_product_per_category,
        'total_sales_per_product' : total_sales_per_product,
        # 'total_inquiries' : total_inquiries,
        'total_bookings' : total_bookings,
        'date' : date,
        "from_date" : from_date,
        "to_date" : to_date,
        "analytics_state": "background-color: #dbeafe;"
    }

    return render(request, template_name, context)

@login_required(login_url='/accounts/login')
def analytics_month(request):
    """
    It gets the total number of orders, total sales and total products for a specific day
    
    :param request: This is the request object that is sent to the view
    :return: The total number of orders, total sales and total products.
    """
    template_name = "analytics/analytics_month.html"

    if 'month' in request.GET:
        month = request.GET['month']
        get_month = datetime.strptime(month, '%Y-%m' )
        current_month = datetime.strftime(get_month, '%m' )
        current_year = datetime.strftime(get_month, '%Y' )

        total_orders_range = Q(Q(date_ordered__year__exact=current_year) & Q(date_ordered__month__exact=current_month)  & Q(status__in=['Done', 'Pending', 'Cancelled', 'Late']))
        total_sales_range = Q(Q(date_ordered__year__exact=current_year) & Q(date_ordered__month__exact=current_month)  & Q(status="Done"))
        total_products_range = Q(Q(created_date__year__exact=current_year) & Q(created_date__month__exact=current_month)  & Q(status=True))
        total_monthly_sales_range = Q(Q(date_ordered__year__exact=current_year) & Q(date_ordered__month__exact=current_month)  & Q(status="Done"))
        total_orders_per_product_range = Q(Q(date_ordered__year__exact=current_year) & Q(date_ordered__month__exact=current_month)  & Q(status__in=['Done', 'Pending', 'Cancelled', 'Late']))
        total_product_per_category_range = Q(Q(created_date__year__exact=current_year) & Q(created_date__month__exact=current_month)  & Q(status=True))
        total_sales_per_product_range = Q(Q(date_ordered__year__exact=current_year) & Q(date_ordered__month__exact=current_month)  & Q(status="Done"))
        # total_inquiries_range = Q(Q(created_date__year__exact=current_year) & Q(created_date__month__exact=current_month))
        total_bookings_range = Q(Q(created_date__year__exact=current_year) & Q(created_date__month__exact=current_month))

        total_orders = Orders.objects.filter(total_orders_range).aggregate(Sum('no_of_order'))
        total_sales = Orders.objects.filter(total_sales_range).aggregate(Sum('total_amount'))
        total_products = Products.objects.filter(total_products_range).count()

        # truncate_month = connection.ops.date_trunc_sql('month', 'date_ordered')
        total_monthly_sales = Orders.objects.annotate(month=TruncMonth('date_ordered')).values('month').filter(total_monthly_sales_range).annotate(Sum('total_amount'))
        total_orders_per_products = Orders.objects.filter(total_orders_per_product_range).values('product_id__product_name').annotate(Sum('no_of_order'))
        total_product_per_category = Products.objects.filter(total_product_per_category_range).values('category_id__category').annotate(Count('category'))
        total_sales_per_product = Orders.objects.filter(total_sales_per_product_range).values('product_id__product_name').annotate(Sum('total_amount'))
        # total_inquiries = Inquiries.objects.filter(total_inquiries_range).count()
        total_bookings = Bookings.objects.filter(total_bookings_range).count()
        date = f"as of {month}"
    else:
        # Get total count
        # This is just a simple query to get the total number of orders, total sales and total products.
        current_year = datetime.now().year
        current_month = datetime.now().month
        if current_month == 12 or current_month == 11:
            var_month = f"{current_year}-{current_month}"
        else:
            var_month = f"{current_year}-0{current_month}"
        month = datetime.strptime(var_month, '%Y-%m' ).month
        total_orders_range = Q(Q(date_ordered__year__exact=current_year) & Q(date_ordered__month__exact=current_month)  & Q(status__in=['Done', 'Pending', 'Cancelled', 'Late']))
        total_sales_range = Q(Q(date_ordered__year__exact=current_year) & Q(date_ordered__month__exact=current_month)  &  Q(status="Done"))
        total_products_range = Q(Q(created_date__year__exact=current_year) & Q(created_date__month__exact=current_month)  &  Q(status=True))
        total_monthly_sales_range = Q(Q(date_ordered__year__exact=current_year) & Q(date_ordered__month__exact=current_month)  &  Q(status="Done"))
        total_orders_per_product_range = Q(Q(date_ordered__year__exact=current_year) & Q(date_ordered__month__exact=current_month)  &  Q(status__in=['Done', 'Pending', 'Cancelled', 'Late']))
        total_product_per_category_range = Q(Q(created_date__year__exact=current_year) & Q(created_date__month__exact=current_month)  &  Q(status=True))
        total_sales_per_product_range = Q(Q(date_ordered__year__exact=current_year) & Q(date_ordered__month__exact=current_month)  & Q(status="Done"))
        # total_inquiries_range = Q(Q(created_date__year__exact=current_year) & Q(created_date__month__exact=current_month))
        total_bookings_range = Q(Q(created_date__year__exact=current_year) & Q(created_date__month__exact=current_month))

        total_orders = Orders.objects.filter(total_orders_range).aggregate(Sum('no_of_order'))
        total_sales = Orders.objects.filter(total_sales_range).aggregate(Sum('total_amount'))
        total_products = Products.objects.filter(total_products_range).count()

        # truncate_month = connection.ops.date_trunc_sql('month', 'date_ordered')
        total_monthly_sales = Orders.objects.annotate(month=TruncMonth('date_ordered')).values('month').filter(total_monthly_sales_range).annotate(Sum('total_amount'))
        total_orders_per_products = Orders.objects.filter(total_orders_per_product_range).values('product_id__product_name').annotate(Sum('no_of_order'))
        total_product_per_category = Products.objects.filter(total_product_per_category_range).values('category_id__category').annotate(Count('category'))
        total_sales_per_product = Orders.objects.filter(total_sales_per_product_range).values('product_id__product_name').annotate(Sum('total_amount'))
        # total_inquiries = Inquiries.objects.filter(total_inquiries_range).count()
        total_bookings = Bookings.objects.filter(total_bookings_range).count()
        date = f"as of {var_month}"

    context = {
        "total_orders" : total_orders,
        "total_sales" : total_sales,
        "total_products": total_products,
        'total_monthly_sales' : total_monthly_sales,
        'total_orders_per_products' : total_orders_per_products,
        'total_product_per_category' : total_product_per_category,
        'total_sales_per_product' : total_sales_per_product,
        # 'total_inquiries' : total_inquiries,
        'total_bookings' : total_bookings,
        'date' : date,
        "month" : month,
        "analytics_state": "background-color: #dbeafe;"
    }

    return render(request, template_name, context)

@login_required(login_url='/accounts/login')
def analytics_year(request):
    """
    It gets the total number of orders, total sales and total products for a specific day
    
    :param request: This is the request object that is sent to the view
    :return: The total number of orders, total sales and total products.
    """
    template_name = "analytics/analytics_year.html"

    if 'year' in request.GET:
        year = request.GET['year']
        current_year = datetime.strptime(year, '%Y' ).year

        total_orders_range = Q(Q(date_ordered__year__exact=current_year)  & Q(status__in=['Done', 'Pending', 'Cancelled', 'Late']))
        total_sales_range = Q(Q(date_ordered__year__exact=current_year) & Q(status="Done"))
        total_products_range = Q(Q(created_date__year__exact=current_year) &  Q(status=True))
        total_monthly_sales_range = Q(Q(date_ordered__year__exact=current_year) & Q(status="Done"))
        total_orders_per_product_range = Q(Q(date_ordered__year__exact=current_year) & Q(status__in=['Done', 'Pending', 'Cancelled', 'Late']))
        total_product_per_category_range = Q(Q(created_date__year__exact=current_year) & Q(status=True))
        total_sales_per_product_range = Q(Q(date_ordered__year__exact=current_year) & Q(status="Done"))
        # total_inquiries_range = Q(Q(created_date__year__exact=current_year))
        total_bookings_range = Q(Q(created_date__year__exact=current_year))

        total_orders = Orders.objects.filter(total_orders_range).aggregate(Sum('no_of_order'))
        total_sales = Orders.objects.filter(total_sales_range).aggregate(Sum('total_amount'))
        total_products = Products.objects.filter(total_products_range).count()

        # truncate_month = connection.ops.date_trunc_sql('month', 'date_ordered')
        total_monthly_sales = Orders.objects.annotate(month=TruncMonth('date_ordered')).values('month').filter(total_monthly_sales_range).annotate(Sum('total_amount'))
        total_orders_per_products = Orders.objects.filter(total_orders_per_product_range).values('product_id__product_name').annotate(Sum('no_of_order'))
        total_product_per_category = Products.objects.filter(total_product_per_category_range).values('category_id__category').annotate(Count('category'))
        total_sales_per_product = Orders.objects.filter(total_sales_per_product_range).values('product_id__product_name').annotate(Sum('total_amount'))
        # total_inquiries = Inquiries.objects.filter(total_inquiries_range).count()
        total_bookings = Bookings.objects.filter(total_bookings_range).count()
        date = f"as of {year}"
    else:
        # Get total count
        # This is just a simple query to get the total number of orders, total sales and total products.
        year = datetime.now().year
        total_orders_range = Q(Q(date_ordered__year__exact=year)  & Q(status__in=['Done', 'Pending', 'Cancelled', 'Late']))
        total_sales_range = Q(Q(date_ordered__year__exact=year)  &  Q(status="Done"))
        total_products_range = Q(Q(created_date__year__exact=year)  &  Q(status=True))
        total_monthly_sales_range = Q(Q(date_ordered__year__exact=year) &  Q(status="Done"))
        total_orders_per_product_range = Q(Q(date_ordered__year__exact=year) &  Q(status__in=['Done', 'Pending', 'Cancelled', 'Late']))
        total_product_per_category_range = Q(Q(created_date__year__exact=year)  &  Q(status=True))
        total_sales_per_product_range = Q(Q(date_ordered__year__exact=year)  & Q(status="Done"))
        # total_inquiries_range = Q(Q(created_date__year__exact=year))
        total_bookings_range = Q(Q(created_date__year__exact=year))

        total_orders = Orders.objects.filter(total_orders_range).aggregate(Sum('no_of_order'))
        total_sales = Orders.objects.filter(total_sales_range).aggregate(Sum('total_amount'))
        total_products = Products.objects.filter(total_products_range).count()

        # truncate_month = connection.ops.date_trunc_sql('month', 'date_ordered')
        total_monthly_sales = Orders.objects.annotate(month=TruncMonth('date_ordered')).values('month').filter(total_monthly_sales_range).annotate(Sum('total_amount'))
        total_orders_per_products = Orders.objects.filter(total_orders_per_product_range).values('product_id__product_name').annotate(Sum('no_of_order'))
        total_product_per_category = Products.objects.filter(total_product_per_category_range).values('category_id__category').annotate(Count('category'))
        total_sales_per_product = Orders.objects.filter(total_sales_per_product_range).values('product_id__product_name').annotate(Sum('total_amount'))
        # total_inquiries = Inquiries.objects.filter(total_inquiries_range).count()
        total_bookings = Bookings.objects.filter(total_bookings_range).count()
        date = f"as of {year}"

    context = {
        "total_orders" : total_orders,
        "total_sales" : total_sales,
        "total_products": total_products,
        'total_monthly_sales' : total_monthly_sales,
        'total_orders_per_products' : total_orders_per_products,
        'total_product_per_category' : total_product_per_category,
        'total_sales_per_product' : total_sales_per_product,
        # 'total_inquiries' : total_inquiries,
        'total_bookings' : total_bookings,
        'date' : date,
        "year" : year,
        "analytics_state": "background-color: #dbeafe;"
    }

    return render(request, template_name, context)