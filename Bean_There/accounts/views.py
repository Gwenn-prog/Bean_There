from django.shortcuts import render
from rest_framework.authtoken.models import Token
from django.contrib.auth import authenticate
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .serializers import UserSerializer
from django.core.exceptions import ObjectDoesNotExist
from .models import CustomUser
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated


@api_view(['POST'])
def register_user(request):
    if request.method == 'POST':
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(
                {'message': 'User registered successfully.', 'data': serializer.data},
                status=status.HTTP_201_CREATED
            )
        return Response(
            {'error': 'Invalid data.', 'details': serializer.errors},
            status=status.HTTP_400_BAD_REQUEST
        )
   


@api_view(['POST'])
def user_login(request):
    if request.method == 'POST':
        username = request.data.get('username')
        password = request.data.get('password')
        

        user = None
        if '@' in username:
            user = CustomUser.objects.filter(email=username).first()
        else:
            user = authenticate(username=username, password=password)


        if user:
            token, _ = Token.objects.get_or_create(user=user)
            return Response(
                {'token': token.key, 'message': 'Login successful.'},
                status=status.HTTP_200_OK
            )


        return Response(
            {'error': 'Invalid credentials. Please check your username/email and password.'},
            status=status.HTTP_401_UNAUTHORIZED
        )


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def user_logout(request):
    if request.method == 'POST':
        try:
            # Check if the user has a token
            if hasattr(request.user, 'auth_token'):
                request.user.auth_token.delete()
                return Response(
                    {'message': 'Successfully logged out.'},
                    status=status.HTTP_200_OK
                )
            else:
                return Response(
                    {'error': 'No token found for this user.'},
                    status=status.HTTP_400_BAD_REQUEST
                )
        except Exception as e:
            return Response(
                {'error': 'An error occurred during logout.', 'details': str(e)},
                status=status.HTTP_500_INTERNAL_SERVER_ERROR
            )
