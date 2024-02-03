from rest_framework import generics
from django.contrib.auth.models import User
from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.authtoken.models import Token
from django.contrib.auth import authenticate, login
import random
import string
from project_api .models import Project 
from project_api.serializers import projectSerializers 
from rest_framework.views import APIView
from .models import Role, UserRole
from .serializers import userAuthSerializers
from django.http import JsonResponse
from django.views.decorators.http import require_POST
from django.views.decorators.csrf import csrf_exempt

class UserAuthViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = userAuthSerializers

    def generate_random_project_name(self):
        static_prefix = "default-"
        
        adjectives = ['happy', 'colorful', 'creative', 'vibrant', 'sparkling']
        nouns = ['unicorn', 'rainbow', 'garden', 'ocean', 'harmony']

        random_adjective = random.choice(adjectives)
        random_noun = random.choice(nouns)

        generated_name = f"{static_prefix}{random_adjective}-{random_noun}"

        while Project.objects.filter(project_name=generated_name).exists():
            random_adjective = random.choice(adjectives)
            random_noun = random.choice(nouns)
            generated_name = f"{static_prefix}{random_adjective}-{random_noun}"

        return generated_name

    def create(self, request, *args, **kwargs):
        first_name = request.data.get('first_name')
        username = request.data.get('username')
        email = request.data.get('email')
        password = request.data.get('password')
        cpassword = request.data.get('cpassword')

        # if password != cpassword:
        #     return Response({"error": "password mismatch"})

        existing_email = User.objects.filter(email=email).exists()
        existing_username = User.objects.filter(username=username).exists()

        if existing_username:
            return Response({"username_error": "User with this username already exists"})
        if existing_email:
            return Response({"email_error": "User with this email already exists"})
        try:
            # Create the user
            user = User.objects.create_user(username=username, email=email, first_name=first_name, password=password)

            project_name = self.generate_random_project_name()          
            
            project= Project(user= user, project_name = project_name) 
            project.save()
            serializer= projectSerializers(project)
            return Response({"message": "user created a default project"})

        except Exception as e:
            return Response({"error": f"Failed to create user: {str(e)}"}, status=status.HTTP_400_BAD_REQUEST)

class AddRoleViewset(viewsets.ModelViewSet):
    queryset = UserRole.objects.all()

    def create(self, request, *args, **kwargs):
        # Get user_id and role_names from the request POST data
        user_id = request.data.get('user_id')
        print(user_id)
        role_names = request.data.get('roles')
        print(role_names)

        try:
            # Retrieve the user
            user = User.objects.get(pk=user_id)

            # Retrieve or create roles
            roles = []
            for role_name in role_names:
                role, created = Role.objects.get_or_create(name=role_name, defaults={'description': f'Default description for {role_name}'})
                roles.append(role)

            # Associate roles with user
            for role in roles:
                UserRole.objects.get_or_create(user=user, role=role)

            return JsonResponse({'success': True, 'message': 'Roles added successfully'})
        except User.DoesNotExist:
            return JsonResponse({'success': False, 'message': 'User does not exist'}, status=404)
        except Exception as e:
            return JsonResponse({'success': False, 'message': str(e)}, status=500)

class LoginViewSet(viewsets.ViewSet):
    def create(self, request):
       
        username_or_email = request.data.get('username_or_email')
        password = request.data.get('password')
        

        if '@' in username_or_email:
            
            user = User.objects.filter(email=username_or_email).first()
        else:
            user = User.objects.filter(username=username_or_email).first()
 
        if user is not None and user.check_password(password):
            # Log the user in
            login(request, user)
 
            serializer = userAuthSerializers(user)
 
            return Response({
                # 'token': token.key,
                'user_data': serializer.data,
            })
        else:
            return Response({"error": "Invalid credentials"}, status=status.HTTP_401_UNAUTHORIZED)