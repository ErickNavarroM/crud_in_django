from django.db import models

# Create your models here.
class TaskModel(models.Model):
    id = models.IntegerField(primary_key=True)
    title = models.CharField(max_length=255)
    description = models.TextField(null=True)
    is_completed = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)