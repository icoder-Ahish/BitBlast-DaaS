from django.contrib.auth.models import User
from rest_framework import serializers
from .models import Project, Cluster, DBcredentials,  Db_credentials

class projectSerializers(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields = "__all__"

class ClusterSerializers(serializers.ModelSerializer):
    class Meta:
        model = Cluster
        fields = "__all__"        
        
# class DBcredentialsSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = DBcredentials
#         fields = ['content']   



class DbcredentialsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Db_credentials
        fields = ['content']              