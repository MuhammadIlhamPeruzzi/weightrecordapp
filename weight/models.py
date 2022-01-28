from django.db import models
 
class WeightRecord(models.Model):
    maxWeight = models.CharField(max_length=20)  
    minWeight = models.CharField(max_length=20) 
    createdAt = models.DateField()
    class Meta:  
        db_table = "weight"