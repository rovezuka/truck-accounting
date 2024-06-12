from django.shortcuts import render
from .models import Truck, Warehouse
# Create your views here.


def truck_list(request):
    trucks = Truck.objects.all()
    warehouses = Warehouse.objects.all()
    context = {
        "trucks": trucks,
        "warehouses": warehouses,
    }
    return render(request, "mining_app/truck_list.html", context)