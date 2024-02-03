from django.contrib.auth.models import User
from userAuth_app.serializers import userAuthSerializers
from rest_framework import serializers
from .models import Provider

class ProviderSerializer(serializers.ModelSerializer):
    # user = userAuthSerializers()
    class Meta:
        model = Provider
        fields = "__all__"