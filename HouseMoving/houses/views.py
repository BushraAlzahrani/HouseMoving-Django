from django.shortcuts import render
from rest_framework.decorators import api_view, authentication_classes, permission_classes
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework import status
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.permissions import IsAuthenticated
from .models import *
from .serializers import *

# Create your views here.


# House Views:

@api_view(['POST'])
@authentication_classes([JWTAuthentication])
@permission_classes([IsAuthenticated])
def add_house(request : Request):
    ''' this view function is for adding a house if the user is authenticated and has permission from house owner group '''
    if not request.user.is_authenticated or not request.user.has_perm('houses.add_house'):
        return Response({"msg": "Not Allowed"}, status=status.HTTP_401_UNAUTHORIZED)

    request.data["owner"] = request.user.id
    adding_house = HouseSerializer(data=request.data)
    if adding_house.is_valid():
        adding_house.save()
        dataResponse = {
            "msg" : "Created Successfully",
            "house": adding_house.data
        }
        return Response(dataResponse)
    else:
        print(adding_house.errors)
        return Response( {"msg": "couldn't add the house"}, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
@authentication_classes([JWTAuthentication])
@permission_classes([IsAuthenticated])
def list_house(request : Request):
    ''' this view function is for listing all the houses if the user has permission from groups packer or driver'''
    if not request.user.is_authenticated or not request.user.has_perm('houses.view_house'):
        return Response({"msg": "Not Allowed"}, status=status.HTTP_401_UNAUTHORIZED)

    house = House.objects.all()
    houses_list = HouseSerializer(instance=house, many=True).data
    dataResponse = {
        "msg": "List of All Houses",
        "houses": houses_list
    }
    return Response(dataResponse)


@api_view(['PUT'])
@authentication_classes([JWTAuthentication])
@permission_classes([IsAuthenticated])
def update_house(request: Request,house_id):
    ''' this view function is for updating the house information if the user is authenticated as the house owner'''
    if not request.user.is_authenticated or not request.user.has_perm('houses.change_house'):
        return Response({"msg": "Not Allowed"}, status=status.HTTP_401_UNAUTHORIZED)

    house = House.objects.get(id=house_id)
    print(request.user.id)
    print(house.owner.id)
    if house.owner.id == request.user.id:
        updated_house = HouseSerializerUpdate(instance=house, data=request.data)
        if updated_house.is_valid():
            updated_house.save()
            dataResponse = {
                "msg": "Updated House Successfully",
            }
            return Response(dataResponse)
        else:
            print(updated_house.errors)
            return Response({"msg": "couldn't update the house"}, status=status.HTTP_400_BAD_REQUEST)
    else:
        return Response({"msg": "Not Allowed"}, status=status.HTTP_401_UNAUTHORIZED)



@api_view(['DELETE'])
@authentication_classes([JWTAuthentication])
def delete_house(request: Request, house_id):
    ''' this view function is for deleting the house if the user is authenticated as the admin'''
    if not request.user.is_authenticated or not request.user.has_perm('houses.delete_house'):
        return Response({"msg": "Not Allowed"}, status=status.HTTP_401_UNAUTHORIZED)

    house = House.objects.get(id=house_id)
    house.delete()
    return Response({"msg" : "Deleted House Successfully"})





# House Belongings Views:

@api_view(['POST'])
@authentication_classes([JWTAuthentication])
def add_belonging(request : Request):
    ''' this view function is for adding the house's belongings if the user is authenticated as a packer'''
    if not request.user.is_authenticated or not request.user.has_perm('houses.add_belongings'):
        return Response({"msg": "Not Allowed"}, status=status.HTTP_401_UNAUTHORIZED)

    new_belonging = BelongingsSerializer(data=request.data)
    if new_belonging.is_valid():
        new_belonging.save()
        dataResponse = {
            "msg" : "Created Successfully",
            "house": new_belonging.data
        }
        return Response(dataResponse)
    else:
        print(new_belonging.errors)
        return Response( {"msg": "couldn't add"}, status=status.HTTP_400_BAD_REQUEST)



@api_view(['GET'])
@authentication_classes([JWTAuthentication])
def list_belonging(request : Request):
    ''' this view function is for listing all the house's belongings if the user has permission as packer'''
    if not request.user.is_authenticated or not request.user.has_perm('houses.view_belongings'):
        return Response({"msg": "Not Allowed"}, status=status.HTTP_401_UNAUTHORIZED)

    belongings = Belongings.objects.all()
    belongings_list = BelongingsSerializer(instance=belongings, many=True).data
    dataResponse = {
        "msg": "List of All Houses",
        "houses": belongings_list
    }
    return Response(dataResponse)


@api_view(['PUT'])
@authentication_classes([JWTAuthentication])
@permission_classes([IsAuthenticated])
def update_belonging(request: Request,belong_id):
    ''' this view function is for updating the house's belongings information if the user has permission from packer group '''
    if not request.user.is_authenticated or not request.user.has_perm('houses.change_belongings'):
        return Response({"msg": "Not Allowed"}, status=status.HTTP_401_UNAUTHORIZED)

    belonging = Belongings.objects.get(id=belong_id)
    updated_belonging = BelongingsSerializer(instance=belonging, data=request.data)
    if updated_belonging.is_valid():
        updated_belonging.save()
        dataResponse = {
            "msg": "Updated House belonging Successfully",
        }
        return Response(dataResponse)
    else:
        print(updated_belonging.errors)
        return Response({"msg": "couldn't update the house belonging"}, status=status.HTTP_400_BAD_REQUEST)



@api_view(['DELETE'])
@authentication_classes([JWTAuthentication])
def delete_belonging(request: Request, belong_id):

    if not request.user.is_authenticated or not request.user.has_perm('houses.delete_belongings'):
        return Response({"msg": "Not Allowed"}, status=status.HTTP_401_UNAUTHORIZED)

    belonging = Belongings.objects.get(id=belong_id)
    belonging.delete()
    return Response({"msg" : "Deleted House's belonging Successfully"})

# Appointments Views:


@api_view(['POST'])
@authentication_classes([JWTAuthentication])
@permission_classes([IsAuthenticated])
def add_appointment(request : Request):
    ''' this view function is for adding a appointment if the user is authenticated and has permission from house owner group '''
    if not request.user.is_authenticated or not request.user.has_perm('houses.add_appointment'):
        return Response({"msg": "Not Allowed"}, status=status.HTTP_401_UNAUTHORIZED)

    request.data["users"] = request.user.id
    adding_appointment = AppointmentSerializer(data=request.data)
    if adding_appointment.is_valid():
        adding_appointment.save()
        dataResponse = {
            "msg" : "Created Successfully",
            "appointment": adding_appointment.data
        }
        return Response(dataResponse)
    else:
        print(adding_appointment.errors)
        return Response( {"msg": "couldn't add the appointment"}, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
@authentication_classes([JWTAuthentication])
@permission_classes([IsAuthenticated])
def list_appointment(request : Request):
    ''' this view function is for listing appointments'''
    if not request.user.is_authenticated or not request.user.has_perm('houses.view_appointment'):
        return Response({"msg": "Not Allowed"}, status=status.HTTP_401_UNAUTHORIZED)

    appointment = Appointment.objects.all()
    appointments_list = AppointmentSerializer(instance=appointment, many=True).data
    dataResponse = {
        "msg": "List of All Appointments",
        "appointments": appointments_list
    }
    return Response(dataResponse)


@api_view(['PUT'])
@authentication_classes([JWTAuthentication])
@permission_classes([IsAuthenticated])
def update_appointment(request: Request,appo_id):
    ''' this view function is for updating the appointment if the user is authenticated as the house owner'''
    if not request.user.is_authenticated or not request.user.has_perm('houses.change_appointment'):
        return Response({"msg": "Not Allowed"}, status=status.HTTP_401_UNAUTHORIZED)

    appointment = Appointment.objects.get(id=appo_id)
    print(request.user.id)
    print(appointment.users.id)
    if appointment.users.id == request.user.id:
        updated_appointment = AppointmentSerializerUpdate(instance=appointment, data=request.data)
        if updated_appointment.is_valid():
            updated_appointment.save()
            dataResponse = {
                "msg": "Updated Appointment Successfully",
            }
            return Response(dataResponse)
        else:
            print(updated_appointment.errors)
            return Response({"msg": "couldn't update the appointment"}, status=status.HTTP_400_BAD_REQUEST)
    else:
        return Response({"msg": "Not Allowed"}, status=status.HTTP_401_UNAUTHORIZED)



@api_view(['DELETE'])
@authentication_classes([JWTAuthentication])
def delete_appointment(request: Request, appo_id):

    if not request.user.is_authenticated or not request.user.has_perm('houses.delete_appointment'):
        return Response({"msg": "Not Allowed"}, status=status.HTTP_401_UNAUTHORIZED)

    appointment = Appointment.objects.get(id=appo_id)
    if appointment.users.id == request.user.id:
        appointment.delete()
        return Response({"msg" : "Deleted Appointment Successfully"})
    else:
        return Response({"msg": "Not Allowed"}, status=status.HTTP_401_UNAUTHORIZED)




# Moving Truck:

@api_view(['GET'])
@authentication_classes([JWTAuthentication])
def list_truck(request : Request):
    ''' this view function is for listing all the Trucks if the user has permission as driver'''

    if not request.user.is_authenticated or not request.user.has_perm('houses.view_movingtruck'):
        return Response({"msg": "Not Allowed"}, status=status.HTTP_401_UNAUTHORIZED)

    trucks = MovingTruck.objects.all()
    trucks_list = TrucksSerializer(instance=trucks, many=True).data
    dataResponse = {
        "msg": "List of All Trucks",
        "houses": trucks_list
    }
    return Response(dataResponse)






