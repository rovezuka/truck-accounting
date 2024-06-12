from django.db import models

# Грузовик
class TruckModel(models.Model):
    name = models.CharField(max_length=200)
    max_load_capacity = models.FloatField(help_text="Максимальная грузоподъемность в тоннах")
    
    def __str__(self):
        return self.name

class Truck(models.Model):
    number = models.CharField(max_length=200)
    model = models.ForeignKey(TruckModel, on_delete=models.CASCADE)
    current_load = models.FloatField(help_text="Текущая нагрузка в тоннах")
    overloading = models.FloatField(help_text="Перегруз в процентах")
    si_content = models.FloatField(help_text="Содержание SiO2 в процентах")
    fe_content = models.FloatField(help_text="Содержание Fe в процентах")
    
    def __str__(self):
        return f"{self.number} ({self.model.name})"

# Склад 
class Warehouse(models.Model):
    name = models.CharField(max_length=200)
    current_load = models.FloatField(default=0, help_text="Текущая нагрузка в тоннах")
    si_content = models.FloatField(help_text="Содержание SiO2 в процентах")
    fe_content = models.FloatField(help_text="Содержание Fe в процентах")
    polygon = models.TextField(help_text="WKT-представление полигона")
    
    def __str__(self):
        return self.name
