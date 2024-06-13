from django.shortcuts import render, redirect
from .models import Truck, Warehouse
from collections import deque
from turfpy.measurement import boolean_point_in_polygon
from geojson import Point, Polygon, Feature

# Create your views here.

POLYGON = ((30, 10), (40, 40), (20, 40), (10, 20), (30, 10))
p1, p2, p3 = 900, 34.0, 65.0


def truck_list(request):
    trucks = Truck.objects.all()
    warehouses = Warehouse.objects.all()

    
    # TODO: выполнить проверки на координаты
    
    id_truck = 1
    truck_info = []
    
    t = Warehouse.objects.get(id=1)
    t.overloading, t.si_content, t.fe_content = p1, p2, p3
    t.save(update_fields=['overloading']) 
    t.save(update_fields=['si_content']) 
    t.save(update_fields=['fe_content'])
    
    if request.method == 'POST':
        coords = request.POST.getlist("coords")
        
        for coord in coords:
            x, y = [int(i) for i in coord.split()]

            if check_coords(x, y):
                print(x, y)
                b = Truck.objects.get(id=id_truck)
                truck_info.append([b.current_load, b.si_content, b.fe_content])
            id_truck += 1
        t = Warehouse.objects.get(id=1)
        z, x, c = t.overloading, t.si_content, t.fe_content
        for i in truck_info:
            z, x, c = mix_ores(z, x, c, i[0], i[1], i[2])
        t.overloading, t.si_content, t.fe_content = z, x, c
        t.save(update_fields=['overloading']) 
        t.save(update_fields=['si_content']) 
        t.save(update_fields=['fe_content']) 
            
    trucks = Truck.objects.all()
    warehouses = Warehouse.objects.all()
    

    context = {
        "trucks": trucks,
        "warehouses": warehouses,
    }
    
    return render(request, "mining_app/truck_list.html", context)

def check_coords(x, y):
    point = Feature(geometry=Point((x, y)))
    polygon = Polygon(
        [
            [
                (30, 10),
                (40, 40),
                (20, 40),
                (10, 20),
                (30, 10),
            ]
        ]
    )
    return boolean_point_in_polygon(point, polygon)

def mix_ores(mass1, si_content1, fe_content1, mass2, si_content2, fe_content2):
    # Общая масса после смешивания
    total_mass = mass1 + mass2

    # Новое содержание SiO2
    new_si_content = (mass1 * si_content1 + mass2 * si_content2) / total_mass

    # Новое содержание Fe
    new_fe_content = (mass1 * fe_content1 + mass2 * fe_content2) / total_mass

    return total_mass, new_si_content, new_fe_content
