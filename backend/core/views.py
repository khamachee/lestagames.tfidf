from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, mixins
from rest_framework.viewsets import GenericViewSet


from .models import Document
from .serializers import DocumentSerializer
from .tasks import process_document_statistics

class DocumentViewSet(APIView):
    def post(self, request):
        serializer = DocumentSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        document = serializer.save()

        return Response({'id': document.id}, status=status.HTTP_201_CREATED)
    

class DocumentView(GenericViewSet, 
                   mixins.CreateModelMixin,
                   mixins.RetrieveModelMixin,
                   mixins.ListModelMixin):
    
    serializer_class = DocumentSerializer
    queryset = Document.objects.all()
    pagination_class = []
