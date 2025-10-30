from rest_framework import viewsets

from .models import Classroom
from .serializers import ClassroomSerializer


class ClassroomViewSet(viewsets.ModelViewSet):
    queryset = Classroom.objects.order_by("id")
    serializer_class = ClassroomSerializer
