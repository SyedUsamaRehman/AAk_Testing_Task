from rest_framework import viewsets,permissions
from .models import Task,Label
from .serializers import LabelSerializers , TaskSerializers
from .permissions_task import IsOwner


class LabelViewSet(viewsets.ModelViewSet):
    serializer_class=LabelSerializers
    permission_classes=[permissions.IsAuthenticated,IsOwner]


    def get_queryset(self):
        return Label.objects.filter(owner=self.request.user)
    
    def perform_create(self, serializer):
        return serializer.save(owner=self.request.user)


class TaskViewSet(viewsets.ModelViewSet):
    serializer_class=TaskSerializers
    permission_classes=[permissions.IsAuthenticated,IsOwner]


    def get_queryset(self):
        return Task.objects.filter(owner=self.request.user)
    
    def perform_create(self, serializer):
        return serializer.save(owner=self.request.user)





