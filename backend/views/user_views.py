from django.core.exceptions import ValidationError, ObjectDoesNotExist
from django.core.mail import EmailMultiAlternatives
from django.core.validators import validate_email
from django.shortcuts import render
from django.urls import reverse
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework_simplejwt.tokens import RefreshToken, AccessToken

from backend.models import User
from backend.serializers import UserSerializer, RegisterSerializer


class UserSignUpView(APIView):
    serializer_class = RegisterSerializer

    def post(self, request):
        serializer = RegisterSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class UserCurrentView(APIView):
    permission_classes = [IsAuthenticatedOrReadOnly]
    serializer_class = UserSerializer

    def get(self, request):
        user = User.objects.get(email=request.user)
        serializer = UserSerializer(user)
        return Response(serializer.data)

    def put(self, request):
        user = User.objects.get(pk=request.user.id)
        serializer = UserSerializer(user, data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['POST'])
def password_forgot(request):
    email = request.data.get('email', None)

    # Validate
    try:
        validate_email(email)
    except ValidationError as err:
        return Response(err, status=status.HTTP_400_BAD_REQUEST)

    # If user exists
    try:
        user = User.objects.get(email=email)
    except ObjectDoesNotExist:
        return Response('Record not found!', status=status.HTTP_404_NOT_FOUND)

    try:
        # Generate Token
        refresh = RefreshToken.for_user(user)
        reset_token = str(refresh.access_token)
        # reset_url = f"http://{request.get_host()}/api/v1/password/reset/{reset_token}/"
        reset_url = f"http://{request.get_host()}{reverse('password-reset-form', args=[reset_token])}"

        # Sending Mail
        subject = "Reset Password - appName"
        mail_from = 'noreply@appName.com'
        mail_to = email
        text_content = ''
        html_content = (f'<div style="text-align: center; padding: 20px; line-height: 2; font-size: 1.2rem">'
                        f'You are receiving this email because you (or someone else) have requested to reset a password. <br /> Click the following link to reset your password. <br /><br />'
                        f'<a href="{reset_url}" style="background-color: #4CAF50; border: none; color: white; padding: 15px 32px; text-align: center; text-decoration: none; display: inline-block; font-size: 1rem; font-weight: bold">'
                        f'RESET PASSWORD'
                        f'</a>'
                        f'<p style="color: red;">This link will expire shortly</p>'
                        f'</div>')

        # send_mail(subject, text_content, mail_from, [mail_to], fail_silently=False)
        msg = EmailMultiAlternatives(subject, text_content, mail_from, [mail_to])
        msg.attach_alternative(html_content, "text/html")
        msg.send()

        return Response('Password Reset Email Sent')

    except Exception as e:
        print('\x1b[91m' + str(e) + '\x1b[0m')
        return Response('Something went wrong', status=status.HTTP_500_INTERNAL_SERVER_ERROR)


@api_view(['GET'])
def password_reset_form_view(request, token):
    context = {'token': token}
    return render(request, 'password_reset.html', context)


@api_view(['PUT'])
def password_reset(request):
    password = request.data.get('password', None)
    token = request.data.get('token', None)

    # Validate
    if not password or not token:
        return Response('Invalid credentials', status=status.HTTP_400_BAD_REQUEST)

    try:
        # Decoding/validating the token
        access_token = AccessToken(token)
        user = User.objects.get(id=access_token['user_id'])
        # Change the password
        user.set_password(password)
        user.save()
        return Response('Password Changed Successfully!')

    except Exception as e:
        print('\x1b[1;31m ' + 'Exception: ' + str(e) + ' \x1b[0m')
        if str(e) == "Token is invalid or expired":
            return Response(str(e), status=status.HTTP_400_BAD_REQUEST)
        return Response('Something went Wrong!', status=status.HTTP_500_INTERNAL_SERVER_ERROR)
