from .models import User

from django.core.mail import EmailMessage
from django.contrib.auth.hashers import make_password
from django.contrib.auth.base_user import BaseUserManager

from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import AllowAny


class LogoutView(APIView):
    def get(self, request):
        # Don't forgot to remove the access token from browser storage.
        return Response({'detail': 'Logout successful.'}, status=status.HTTP_200_OK)


class RegisterView(APIView):
    permission_classes = [AllowAny, ]

    def post(self, request):
        try:
            first_name = request.data['first_name']
        except KeyError:
            return Response({"error": "first_name required."}, status=status.HTTP_400_BAD_REQUEST)

        try:
            last_name = request.data['last_name']
        except KeyError:
            return Response({"error": "last_name required."}, status=status.HTTP_400_BAD_REQUEST)

        try:
            username = request.data['username']
        except KeyError:
            return Response({"error": "last_name required."}, status=status.HTTP_400_BAD_REQUEST)

        username = BaseUserManager().normalize_email(username)

        prev_users = User.objects.filter(username=username)
        if len(prev_users):
            return Response({"detail": "User already exist."}, status=status.HTTP_406_NOT_ACCEPTABLE)

        # Generates random password.
        password =  BaseUserManager().make_random_password(length=10)

        # Make password hash.
        password_hash = make_password(password)

        # Send generated password in email.
        email_message = EmailMessage(
            'Welcome to Django-JWT-User Example',
            f"Hi {first_name} {last_name},\n\nYou have successfully registered with Django-JWT-User Example.\n\nYour new password is ({password}).\n\n",
            to=[username, ],
        )
        email_message.send()

        User().register_user(first_name=first_name, last_name=last_name, username=username, password=password_hash)

        return Response({"detail": "User account created."}, status=status.HTTP_200_OK)


class DetailsView(APIView):
    def get(self, request):
        data = {
            "first_name": request.user.first_name,
            "last_name": request.user.last_name,
            "username": request.user.username,
        }

        return Response(data, status=status.HTTP_200_OK)

    def put(self, request):
        def update_details(user_id, data):
            user = User.objects.get(pk=user_id)
            if 'first_name' in data:
                user.first_name = data['first_name']
            if 'last_name' in data:
                user.last_name = data['last_name']
            user.save()

        data = request.data.dict()

        if 'first_name' not in data and 'last_name' not in data:
            return Response({'error': "`firstname` and or `last_name` required."}, status=status.HTTP_400_BAD_REQUEST)

        update_details(request.user.id, data)

        return Response({'detail': 'User details are updated.'}, status=status.HTTP_200_OK)
