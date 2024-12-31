from rest_framework import serializers
from .models import Label,Task



class LabelSerializers(serializers.ModelSerializer):
    class Meta:
        model=Label
        fields='__all__'
        read_only_fields=['owner']


class TaskSerializers(serializers.ModelSerializer):
    labels=serializers.PrimaryKeyRelatedField(queryset=Label.objects.all(),many=True)
    is_completed=serializers.BooleanField(default=False)

    class Meta:
        model=Task
        fields='__all__'
        read_only_fields=['owner']
        
    def validate(self, attrs):
        owner=self.context['request'].user
        title=attrs.get('title')
        if Task.objects.filter(title=title,owner=owner).exists():
            raise serializers.ValidationError("You already have a task with this title")
        return attrs