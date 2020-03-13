from django.db import models

# Create your models here.
class Operation(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name
    
class Station(models.Model):
    name = models.CharField(max_length=50, blank=True)
    code = models.IntegerField()

    def __str__(self):
        return str(self.code)
    
class Piece(models.Model):
    code = models.BigIntegerField()
    name = models.CharField(max_length=100)
    amount = models.DecimalField(max_digits=6, decimal_places=5, default=1)
    main_product_code = models.IntegerField()
    operation_name = models.ForeignKey(Operation, on_delete=models.SET('DELETED'))
    station_code = models.ForeignKey(Station, on_delete=models.SET('DELETED'))
    parent_product_code = models.ForeignKey("self", on_delete=models.SET('DELETED'))
    time = models.DecimalField(max_digits=4, decimal_places=2)

    def __str__(self):
        return f"{self.name} ---> {self.main_product_code}"
    
