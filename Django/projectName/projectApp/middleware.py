# middleware.py
from rest_framework_simplejwt.tokens import TokenError, RefreshToken
from rest_framework.response import Response
from rest_framework import status
from rest_framework_simplejwt.tokens import TokenError


class TokenValidationMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        # Retrieve Access Token from Request
        access_token = request.headers.get('Authorization', '').split('Bearer ')[-1]

        # Validate Access Token
        is_valid_token = self.validate_token(access_token)
        # If the token is not valid, return an error response
        if not is_valid_token:
            return Response({'error': 'Invalid token'}, status=status.HTTP_401_UNAUTHORIZED)

        # If the token is valid, continue processing the request
        response = self.get_response(request)
        return response

    def validate_token(self, access_token):
        try:
            # Validate the access token using SimpleJWT library
            RefreshToken(access_token).access_token
            return True
        except TokenError:
            # Token validation failed
            return False
        

import logging

class LoggingMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        # Log information about the incoming request to the request log file
        self.log_request_info(request)

        response = self.get_response(request)

        # Log information about the outgoing response to the response log file
        self.log_response_info(response)

        return response

    def log_request_info(self, request):
        # Configure a logger for request logging
        request_logger = logging.getLogger('django.request')
        request_logger.setLevel(logging.INFO)  # Set the log level as needed

        # Log information about the incoming request to the request log file
        with open('request_log.txt', 'a') as f_request:
            f_request.write(f"Incoming Request: {request.method} {request.path}\n")

    def log_response_info(self, response):
        # Configure a logger for response logging
        response_logger = logging.getLogger('django.response')
        response_logger.setLevel(logging.INFO)  # Set the log level as needed

        # Log information about the outgoing response to the response log file
        with open('response_log.txt', 'a') as f_response:
            f_response.write(f"Outgoing Response: {response.status_code}\n")
