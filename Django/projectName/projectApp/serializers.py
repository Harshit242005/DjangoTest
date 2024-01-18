# adding serializers 
from rest_framework import serializers

class HelloWorldSerializer(serializers.Serializer):
    message = serializers.CharField(max_length=255)

# serializers.py
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
# Signup seralizer
class SignupSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'email', 'password']
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        # checking if the email exist or not 
        email = validated_data['email']
        print(f'data on signup: {validated_data}')
        if User.objects.filter(email=email).exists():
            raise serializers.ValidationError({'email': 'This email address is already registered.'})
        # creating user object 
        user = User.objects.create_user(
            username=validated_data['username'],
            email=validated_data['email'],
            password=validated_data['password']
        )
        return user

class LoginSerializer(serializers.Serializer):
    username = serializers.CharField()
    email = serializers.EmailField()
    password = serializers.CharField()

    def validate(self, data):
        email = data.get('email')
        password = data.get('password')
        username = data.get('username')
        print(f'user data is {data}')
        if username and password and email:
            user = authenticate(request=self.context.get('request'), username=username, password=password)
            print(f'user auth: {user}')
            if not user:
                print('user not in the database')
                raise serializers.ValidationError("Unable to log in with provided credentials.")

        else:
            raise serializers.ValidationError("Must include 'email' and 'password'.")
        return data