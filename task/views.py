from rest_framework import viewsets,permissions,status
from rest_framework.response import Response
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

        
        task = serializer.save(owner=self.request.user)
        labels = self.request.data.get('labels', [])
        if labels:
            task.labels.set(labels)
        self.response_message = {
            "message": "Task created successfully!",
            "task": TaskSerializers(task).data  
        }
    
    def create(self, request, *args, **kwargs):
        response = super().create(request, *args, **kwargs)
        return Response(self.response_message, status=status.HTTP_201_CREATED)
    
    def perform_destroy(self, instance):
        print(f"Task with ID{instance.id} is being deleted")
        instance.delete()
    def destroy(self,request,*args,**kwargs):

        instance=self.get_object()
        self.perform_destroy(instance)
        return Response(
            {"message": "Task deleted successfully!"},
            status=status.HTTP_204_NO_CONTENT
        )



