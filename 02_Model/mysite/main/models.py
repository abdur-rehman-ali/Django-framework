from django.db import models

# Create your models here.
class studentRegistration(models.Model):
    name = models.CharField(max_length=100)
    reg_no = models.IntegerField()
    cgpa = models.FloatField(default=3.00,max_length=4)

    def __str__(self):
        return self.name