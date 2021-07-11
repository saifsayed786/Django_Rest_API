from django.contrib.auth.models import User, Group
from client.models import Client, Project
from rest_framework import serializers

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['url', 'username', 'email',]

class ClientSerializers(serializers.ModelSerializer): 
    # clientproject = serializers.PrimaryKeyRelatedField(many=True,queryset=Project.objects.all())
    clientproject = serializers.SlugRelatedField(many=True,slug_field='project_name',queryset=Project.objects.all())

    class Meta:
        model = Client
        # fields = '__all__'
        fields = ['id','client_name','created_at','created_by','clientproject']

class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model= Project
        fields ='__all__'