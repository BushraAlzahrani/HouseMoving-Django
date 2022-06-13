from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from rest_framework.decorators import api_view, permission_classes, authentication_classes
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework import status
from rest_framework_simplejwt.tokens import AccessToken
from .serializers import UserRegisterSerializer, UserSearchSerializer
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication


# Create your views here.

@api_view(['POST'])
def register_user(request: Request):
    user_serializer = UserRegisterSerializer(data=request.data)
    if user_serializer.is_valid():
        new_user = User.objects.create_user(**user_serializer.data)
        new_user.save()
        return Response({"msg": "created user successfully"})
    else:
        print(user_serializer.errors)
        return Response({"msg": "Couldn't create user"}, status=status.HTTP_400_BAD_REQUEST)


@api_view(['POST'])
def login_user(request: Request):
    if 'username' in request.data and 'password' in request.data:
        user = authenticate(request, username=request.data['username'], password=request.data['password'])
        if user is not None:
            token = AccessToken.for_user(user)
            responseData = {
                "msg": "Your token is ready",
                "token": str(token)
            }
            return Response(responseData)

    return Response({"msg": "please provide your username & password"}, status=status.HTTP_401_UNAUTHORIZED)



@api_view(['GET'])
@authentication_classes([JWTAuthentication])
@permission_classes([IsAuthenticated])
def search_user (request: Request, username):

# add authentication and permission, it is showing password fix it
    #if not request.user.is_authenticated or not request.user.has_perm('users.view_user'):
       # return Response({"msg": "Not Allowed"}, status=status.HTTP_401_UNAUTHORIZED)

   user_search= User.objects.filter(username__contains= username.lower())

   user_info = UserSearchSerializer(instance=user_search,  many=True).data
   if user_info:
       dataResponse = {
           "User": user_info
       }
       return Response(dataResponse)
   else:
       print(user_info.errors)
       return Response({"msg": "couldn't find the user"}, status=status.HTTP_400_BAD_REQUEST)
