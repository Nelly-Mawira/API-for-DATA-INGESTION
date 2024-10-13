from django.db import models
from django.utils import timezone
# Create your models here.


class DataEntry(models.Model):
    STATUS_CHOICES = [
        ('uploaded', 'Uploaded'),
        ('processing', 'Processing'),
        ('processed', 'processed'),
        ('failed', 'failed'),
    ]

    data = models.JSONField()
    metadata = models.JSONField()
    processed_data = models.JSONField(null=True, blank=True)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='uploaded')
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(auto_now=True)



    def __str__(self):
        return f"DataEntry {self.id} - {self.status}"





      
