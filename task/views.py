from rest_framework import viewsets,permissions
from .models import Task,Label
from .serializers import LabelSerializers , TaskSerializers
from .permissions_task import IsOwner
from drf_spectacular.utils import extend_schema, extend_schema_view




@extend_schema_view(
    list=extend_schema(summary="List all labels", description="Retrieve all labels owned by the authenticated user."),
    create=extend_schema(summary="Create a new label", description="Create a new label for the authenticated user."),
    retrieve=extend_schema(summary="Retrieve a label", description="Retrieve details of a specific label."),
    update=extend_schema(summary="Update a label", description="Update a specific label."),
    destroy=extend_schema(summary="Delete a label", description="Delete a specific label."),
)
class LabelViewSet(viewsets.ModelViewSet):
    serializer_class=LabelSerializers
    permission_classes=[permissions.IsAuthenticated,IsOwner]


    def get_queryset(self):
        return Label.objects.filter(owner=self.request.user)
    
    def perform_create(self, serializer):
        return serializer.save(owner=self.request.user)
    



@extend_schema_view(
    list=extend_schema(summary="List all Task", description="Retrieve all Task owned by the authenticated user."),
    create=extend_schema(summary="Create a new Task", description="Create a new Task for the authenticated user."),
    retrieve=extend_schema(summary="Retrieve a Tasks", description="Retrieve details of a specific Task."),
    update=extend_schema(summary="Update a Task", description="Update a specific Task."),
    destroy=extend_schema(summary="Delete a Task", description="Delete a specific Task."),
)
class TaskViewSet(viewsets.ModelViewSet):
    serializer_class=TaskSerializers
    permission_classes=[permissions.IsAuthenticated,IsOwner]


    def get_queryset(self):
        return Task.objects.filter(owner=self.request.user)
    
    def perform_create(self, serializer):
        return serializer.save(owner=self.request.user)





