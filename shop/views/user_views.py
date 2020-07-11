
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated

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

