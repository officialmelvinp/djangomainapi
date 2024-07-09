from rest_framework.views import APIView
from rest_framework import permissions
from rest_framework.response import Response
from rest_framework import status
from .serializer import UserSerializer
from django.contrib.auth import authenticate
from rest_framework_simplejwt.tokens import AccessToken

# Create your views here.
class UserRegistrationView(APIView):
    permission_classes = [permissions.AllowAny]
    
    
    def post(self, request):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"message": "user registered successfully"}, status=status.HTTP_200_OK)
        return Response(serializer.errors)
    
    
    
class UserLoginView(APIView):
    permission_classes = [permissions.AllowAny]
    
    def post(self, request):
        username = request.data.get('username')
        password = request.data.get('password')
        user = authenticate(username=username, password=password)
        print(user)
        print(username, password)
        
        
        if user is not None:
            access_token = AccessToken.for_user(user)
            return Response({
                'access': str(access_token),
            }, status=status.HTTP_200_OK)
        else:
            return Response({"error":"invalid credentials"}, status=status.HTTP_401_UNAUTHORIZED)
        
        
