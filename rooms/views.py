from rest_framework import viewsets
from .models import Room, Roomcategory
from .serializers import RoomSerializer, RoomCategorySerializer

# Create your views here.
class RoomViewSet(viewsets.ModelViewSet):
    queryset = Room.objects.all()
    serializer_class = RoomSerializer


class RoomCategoryViewSet(viewsets.ModelViewSet):
    queryset = Roomcategory.objects.all()
    serializer_class = RoomCategorySerializer
