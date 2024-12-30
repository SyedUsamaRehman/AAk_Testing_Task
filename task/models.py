from django.db import models
from django.contrib.auth.models import User





class Label(models.Model):
    name=models.CharField(max_length=50)
    owner=models.ForeignKey(User,on_delete=models.CASCADE)

    class Meta:
        unique_together=('name','owner')
    
    def __str__(self):
        return self.name


class Task (models.Model):
    title=models.CharField(max_length=100)
    description=models.TextField()
    is_completed=models.BooleanField(default=False)
    owner=models.ForeignKey(User,on_delete=models.CASCADE)
    labels=models.ManyToManyField(Label)


    def __str__(self):
        return self.title