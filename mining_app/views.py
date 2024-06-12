from django.shortcuts import render, redirect
from .models import Truck, Warehouse
import numpy as np
# Create your views here.


def truck_list(request):
    trucks = Truck.objects.all()
    warehouses = Warehouse.objects.all()

    coords = request.POST.getlist("coords")
    
    # TODO: выполнить проверки на координаты
        
    for coord in coords:
        x, y = [int(i) for i in coord.split()]
        print(x, y)

    context = {
        "trucks": trucks,
        "warehouses": warehouses,
    }
    
    return render(request, "mining_app/truck_list.html", context)
