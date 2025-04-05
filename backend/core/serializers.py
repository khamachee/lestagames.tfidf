from rest_framework import serializers
from .models import Document

class DocumentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Document
        exclude = []
        read_only_fields = ['id', 'statistics', 'created_at']
        
