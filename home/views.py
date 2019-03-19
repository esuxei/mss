from django.shortcuts import render

# Create your views here.
from django.contrib.auth.decorators import login_required
from activity.models import Activity

from django.http import JsonResponse

@login_required
def index(request):
    if request.user.has_perm('warehouse.view_all_order'):
        order_items = ""#Orderitem.objects.all().order_by('order')[:20]
    else:
        order_items = ""#Orderitem.objects.all().filter(order__office__in = request.user.profile.department.all()).order_by('order')[:20]
    return render(request, 'home/index.html', {'order_items': order_items})

def login(request):
    content ={'title':"Login page"}
    return render(request, 'home/login.html', content)

def error_400(request):
    return render(request, '400.html', {'title': "400 page"})

def error_401(request):
    return render(request, '401.html', {'title': "401 page"})

def error_403(request):
    return render(request, '403.html', {'title': "403 page"})

def error_404(request):
    return render(request, '404.html', {'title': "404 page"})

def error_500(request):
    return render(request, '500.html', {'title': "500 page"})

def error_503(request):
    return render(request, '503.html', {'title': "503 page"})
