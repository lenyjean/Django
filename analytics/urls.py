from django.urls import path


from .views import *

urlpatterns = [
    path("analytics", analytics, name="analytics"),
    path("analytics/day", analytics_day, name="analytics_day"),
    path("analytics/week", analytics_week, name="analytics_week"),
    path("analytics/month", analytics_month, name="analytics_month"),
    path("analytics/year", analytics_year, name="analytics_year"),
]
