from django.shortcuts import render

# Create your views here.
def analytics(request):
    template_name = "analytics/analytics.html"

    context = {}
    return render(request, template_name, context)