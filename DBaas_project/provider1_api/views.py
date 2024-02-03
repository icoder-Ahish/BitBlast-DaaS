from rest_framework import viewsets,status
from .models import Provider
from .serializers import ProviderSerializer
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from django.contrib.auth.models import User

class ProviderViewSet(viewsets.ModelViewSet):
    queryset = Provider.objects.all()
    serializer_class = ProviderSerializer

    def create(self, request, *args, **kwargs):
        user_id = request.data.get('user_id')
        provider_name = request.data.get('provider_name')
        Key_name = request.data.get('key_name')
        provider_url = request.data.get('provider_url')
        secret_key = request.data.get('secret_key')
        access_token = request.data.get('access_token')
        
        if Provider.objects.filter(provider_url=provider_url, user_id=user_id).exists():
            return Response({"Provider_error": "Provider URL already exists for this user"}, status=status.HTTP_400_BAD_REQUEST)

        # Error handling for key_name
        if Provider.objects.filter(Key_name=Key_name, user_id=user_id).exists():
            return Response({"apiName_error": "Key name already exists for this user"}, status=status.HTTP_400_BAD_REQUEST)

        provider = Provider(
            user_id=user_id,
            provider_name=provider_name,
            Key_name=Key_name,
            provider_url=provider_url,
            secret_key=secret_key,
            access_token=access_token,
            is_connected=True
        )
        provider.save()

        serializer = ProviderSerializer(provider)
        return Response(serializer.data, status=201)

    def get_provider_by_name(self, request, provider_name):
        provider = get_object_or_404(Provider, provider_name=provider_name)
        serializer = ProviderSerializer(provider)
        return Response(serializer.data)

    def get_provider_by_user_id(self, request, user_id):
        providers = Provider.objects.filter(user_id=user_id, is_connected=True)
        serializer = ProviderSerializer(providers, many=True)
        return Response(serializer.data)

    def get_provider_by_username_and_name(self, request, username, provider_name):
        
        user = get_object_or_404(User, username=username)

        # Get the provider based on the user and provider name
        provider = get_object_or_404(Provider, user_id=user.id, provider_name=provider_name)

        serializer = ProviderSerializer(provider)
        return Response(serializer.data)


