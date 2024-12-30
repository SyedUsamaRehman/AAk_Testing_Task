from rest_framework import serializers
from .models import Label,Task



class LabelSerializers(serializers.ModelSerializer):
    class Meta:
        model=Label
        fields='__all__'
        read_only_fields=['owner']


class TaskSerializers(serializers.ModelSerializer):
    labels=LabelSerializers(many=True,read_only=True)

    class Meta:
        model=Task
        fields='__all__'
        read_only_fields=['owner']
