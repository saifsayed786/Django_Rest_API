from rest_framework import viewsets
from . models import Client,Project
from apipackage import serializers

class ClientViewset(viewsets.ModelViewSet):
    queryset = Client.objects.all()
    serializer_class = serializers.ClientSerializers
    

class ProjectViewset(viewsets.ModelViewSet):
    queryset = Project.objects.all()
    serializer_class = serializers.ProjectSerializer