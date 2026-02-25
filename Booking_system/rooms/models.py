from django.db import models

# Create your models here.
class Roomcategory(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    price_per_night = models.DecimalField(max_digits=8, decimal_places=2)
    capacity = models.IntegerField(default=1)

    def __str__(self):
        return self.name


class Room(models.Model):

    ROOM_STATUS = [
        ('available', 'Available'),
        ('occupied', 'Occupied'),
        ('cleaning', 'Cleaning'),
        ('maintenance', 'Maintenance')
    ]

    number = models.CharField(max_length=10)
    category = models.ForeignKey(Roomcategory, on_delete=models.CASCADE, related_name='rooms')
    block = models.IntegerField()
    status = models.CharField(max_length=20, choices=ROOM_STATUS, default='available')

    def __str__(self):
        return str(self.number)
    
  