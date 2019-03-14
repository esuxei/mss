from django.conf.urls import url
from . import views

urlpatterns = [
    # The home page
    #url('', views.index, name='home_index'),
    url('ajax/load-orders/', views.load_orders, name='home_ajax_load_orders'),
    url('get',views.orders, name='home_orders'),
    url(r'^$', views.index, name='home')
]