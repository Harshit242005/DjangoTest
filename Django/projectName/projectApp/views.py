# projectApp/views.py
from django.http import HttpResponse
from django.shortcuts import render
from itsdangerous import Serializer

# using rest framework for the api endpoint handling
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .serializers import HelloWorldSerializer

def home_view(request):
    return HttpResponse("Welcome to the home page!")

def about_view(request):
    return HttpResponse("This is the about page.")

def contact_view(request):
    return render(request, 'contact.html')

# hello world view as a get request for data to fetch
@api_view(['GET', 'POST'])
def hello_world(request):
    if request.method == 'GET':
        return Response({'message': 'Hello, world! this is some new data sent from hello world page'})
    if request.method == 'POST':
        return handle_post_request(request)


def handle_post_request(request):
    serializer = HelloWorldSerializer(data=request.data)
    if serializer.is_valid():
        # Valid data, perform your desired actions
        received_message = serializer.validated_data['message']
        # sending a response that message is received
        return Response({'message': f'Received message: {received_message}'}, status=status.HTTP_201_CREATED)
    # handling the error on the serializers not matching
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# adding up the signup and login views
# views.py

from rest_framework.decorators import permission_classes
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import AllowAny
from .serializers import SignupSerializer, LoginSerializer

@api_view(['POST'])
@permission_classes([AllowAny])
def signup(request):
    serializer = SignupSerializer(data=request.data)
    try:
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    except Serializer.ValidationError as e:
        # Extract the error details from the exception and send in the response
        errors = dict(e.detail)
        print(f'the errors we faced are: {errors}')
        return Response(errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['POST'])
@permission_classes([AllowAny])
def login(request):
    print(f'login data: {request.data}')
    serializer = LoginSerializer(data=request.data, context={'request': request})
    if serializer.is_valid():
        print('user is validated correctly')
        print(f'seralized validated data: {serializer.validated_data}')
        username = serializer.validated_data['username']
        # Customize the response data as needed
        response_data = {'user_name': username}
        return Response(response_data, status=status.HTTP_200_OK)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
