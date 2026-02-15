from django.db import models
from django.contrib.auth.models import User
from rooms.models import Room

# Create your models here.
class Reservation(models.Model):
    status_choice = (
        ('pending', 'Pending'),
        ('confirmed', 'Confirmed'),
        ('cancelled', 'Cancelled'),
    )
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    room = models.ForeignKey(Room, on_delete=models.CASCADE)
    check_in = models.DateField()
    check_out = models.DateField()
    status = models.CharField(max_length=20, choices=status_choice, default='booked')

    def __str__(self):
        return f"{self.guest.username} - {self.room.room_number}"






