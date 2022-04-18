from rest_framework import viewsets
from .models import Car
from .permissions import DealerPermission
from .serializers import CarSerializer


class CarModelViewSet(viewsets.ModelViewSet):
    permission_classes = [DealerPermission]
    serializer_class = CarSerializer
    queryset = Car.objects.all()
