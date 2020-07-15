from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.tokens import RefreshToken
from django.core.mail import EmailMultiAlternatives

from shop.models import User
from shop.serializers import UserSerializer


# =====================================================================
#                       Get Logged in User
# =====================================================================
@api_view(['GET'])
@permission_classes([IsAuthenticated])
def current_user(request):
    user = User.objects.get(email=request.user)
    serializer = UserSerializer(user)
    return Response({'success': True, 'data': serializer.data})


# =====================================================================
#                              Register
# =====================================================================
@api_view(['POST'])
def register(request):
    email = request.data['email'].lower()
    password = request.data['password']

    if User.objects.get(email=email):
        return Response(
            {'success': False, 'error': 'Email already in use'},
            status=status.HTTP_400_BAD_REQUEST
        )

    try:
        user = User.objects.create_user(email, password)
        serializer = UserSerializer(user)
        return Response({'success': True, 'data': serializer.data})
    except:
        return Response(
            {'success': False, 'error': 'Something went wrong'},
            status=status.HTTP_500_INTERNAL_SERVER_ERROR
        )


# =====================================================================
#                         Forgot Password
# =====================================================================
@api_view(['POST'])
def forgot_password(request):
    email = request.data['email'] if 'email' in request.data else None

    # Validate
    if not email:
        return Response({'success': False, 'error': 'Email is required'}, status=status.HTTP_400_BAD_REQUEST)

    # If user exists
    user = User.objects.get(email=email)
    if not user:
        return Response({'success': False, 'error': 'User not found'}, status=status.HTTP_400_BAD_REQUEST)

    try:
        # Generate Token
        refresh = RefreshToken.for_user(user)
        reset_token = str(refresh.access_token)
        reset_url = f"http://localhost:8000/api/v1/reset_password/{reset_token}"

        # Sending Mail
        subject = "Reset Password - dj-shop"
        mail_from = 'noreply@dj-shop.com'
        mail_to = email
        text_content = ''
        html_content = (f'<div style="text-align: center; padding: 20px; line-height: 2; font-size: 1.2rem">'
                        f'You are receiving this email because you (or someone else) have requested to reset a password. <br /> Make a PUT request to the following link to reset your password <br /><br />'
                        f'<a href="{reset_url}" style="background-color: #4CAF50; border: none; color: white; padding: 15px 32px; text-align: center; text-decoration: none; display: inline-block; font-size: 1rem; font-weight: bold">'
                        f'RESET PASSWORD'
                        f'</a>'
                        f'<p style="color: red;">This link will expire shortly</p>'
                        f'</div>')

        # send_mail(subject, text_content, mail_from, [mail_to], fail_silently=False)
        msg = EmailMultiAlternatives(subject, text_content, mail_from, [mail_to])
        msg.attach_alternative(html_content, "text/html")
        msg.send()

        return Response({'success': True, 'data': 'Password Reset Email Sent'})

    except Exception as e:
        print('\x1b[91m' + str(e) + '\x1b[0m')
        return Response(
            {'success': False, 'error': 'Something went wrong'},
            status=status.HTTP_500_INTERNAL_SERVER_ERROR
        )
