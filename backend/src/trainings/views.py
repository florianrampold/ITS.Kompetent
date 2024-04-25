from django.shortcuts import render

# Create your views here.
from rest_framework.viewsets import ModelViewSet
from rest_framework import pagination
from rest_framework.response import Response
from .models import *
from .serializers import *


class TrainingPagination(pagination.PageNumberPagination):
    """
    A Pagination Class for pagination on trainings.    
    """
    page_size=10
    def get_paginated_response(self, data):
        """
        Paginates the trainin programs

        Args:
            data (Model): The training programs

        Returns:
            Response: A Django Response object. 
        """
        return Response({
        
            'next': self.get_next_link(),
            'previous': self.get_previous_link(),
            'count': self.page.paginator.count,
            'total_pages': self.page.paginator.num_pages,
            'results': data
        })

class LanguageViewSet(ModelViewSet):
    """
    A ViewSet for handling CRUD operations on languages of trainings.

    This ViewSet provides endpoints for creating, retrieving, updating, and deleting languages.
    
    Attributes:
        queryset (QuerySet): The queryset containing all languages.
        serializer_class (Serializer): The serializer class used for languages serialization and deserialization.
    """
    queryset = Language.objects.all()
    serializer_class = LanguageSerializer

class DeliveryMethodViewSet(ModelViewSet):
    """
    A ViewSet for handling CRUD operations on delivery methods of trainings.

    This ViewSet provides endpoints for creating, retrieving, updating, and deleting delivery methods.
    
    Attributes:
        queryset (QuerySet): The queryset containing all delivery methods.
        serializer_class (Serializer): The serializer class used for delivery methods serialization and deserialization.
    """
    queryset = DeliveryMethod.objects.all()
    serializer_class = DeliveryMethodSerializer

class TrainingViewSet(ModelViewSet):
    """
    A ViewSet for handling CRUD operations on training programs.

    This ViewSet provides endpoints for creating, retrieving, updating, and deleting training programs.
    
    Attributes:
        queryset (QuerySet): The queryset containing all training programs.
        serializer_class (Serializer): The serializer class used for training programs serialization and deserialization.
    """
    queryset = Training.objects.get_queryset().order_by('training_name')
    serializer_class = TrainingSerializer