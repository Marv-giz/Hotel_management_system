from django.db import models
from rooms.models import Room
from django.contrib.auth.models import User

# Create your models here.
class Reservation(models.Model):

    STATUS_CHOICES = [
        ('reserved', 'Reserved'),
        ('checked_in', 'Checked In'),
        ('checked_out', 'Checked Out'),
        ('cancelled', 'Cancelled')
    ]

    guest_name = models.CharField(max_length=200)
    guest_email = models.EmailField()

    room = models.ForeignKey(Room, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    check_in = models.DateField()
    check_out = models.DateField()

    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='reserved')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.guest_name} - Room{self.room.id}"