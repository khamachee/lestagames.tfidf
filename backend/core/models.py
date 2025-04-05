from django.db import models
from config import settings
from .tasks import process_document_statistics
# Create your models here.

class Document(models.Model):
    file = models.FileField(upload_to='documents/')
    statistics = models.JSONField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Document {self.id}'
    
    def save(self, *args, **kwargs):
        is_new = self.pk is None  
        super().save(*args, **kwargs)
        
        if is_new: 
            process_document_statistics.delay(self.id)
