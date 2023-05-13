from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.http import Http404
from rest_framework.permissions import IsAuthenticatedOrReadOnly

from shop.models import Category
from shop.serializers import CategorySerializer


class CategoryList(APIView):
    permission_classes = [IsAuthenticatedOrReadOnly]

    def get(self, request, format=None):
        categories = Category.objects.all()
        serializer = CategorySerializer(categories, many=True)
        return Response({'success': True, 'data': serializer.data})

    def post(self, request, format=None):
        serializer = CategorySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'success': True, 'data': serializer.data}, status=status.HTTP_201_CREATED)
        return Response({'success': False, 'error': serializer.errors}, status=status.HTTP_400_BAD_REQUEST)


class CategoryDetail(APIView):
    permission_classes = [IsAuthenticatedOrReadOnly]

    def get(self, request, pk, format=None):
        category = self._get_object(pk)
        serializer = CategorySerializer(category)
        return Response({'success': True, 'data': serializer.data})

    def put(self, request, pk, format=None):
        category = self._get_object(pk)
        serializer = CategorySerializer(category, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'success': True, 'data': serializer.data})
        return Response(
            {'success': False, 'error': serializer.errors},
            status=status.HTTP_400_BAD_REQUEST
        )

    def delete(self, request, pk, format=None):
        category = self._get_object(pk)
        print("\n\nperforming delete\n\n")
        category.delete()
        return Response({'success': True}, status=status.HTTP_204_NO_CONTENT)

    def _get_object(self, pk):
        try:
            return Category.objects.get(pk=pk)
        except Category.DoesNotExist:
            raise Http404


# @api_view(['GET', 'POST'])
# @permission_classes([IsAuthenticatedOrReadOnly])
# def category_list(request):

#     if request.method == 'GET':
#         categories = Category.objects.all()
#         serializer = CategorySerializer(categories, many=True)
#         return Response({'success': True, 'data': serializer.data})

#     elif request.method == 'POST':
#         serializer = CategorySerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# @api_view(['GET', 'PUT', 'DELETE'])
# @permission_classes([IsAuthenticatedOrReadOnly])
# def category_detail(request, pk):

#     try:
#         category = Category.objects.get(pk=pk)
#     except Category.DoesNotExist:
#         return Response(
#             {'success': False, 'error': 'Not Found'},
#             status=status.HTTP_404_NOT_FOUND
#         )

#     if request.method == 'GET':
#         serializer = CategorySerializer(category)
#         return Response({'success': True, 'data': serializer.data})

#     elif request.method == 'PUT':
#         serializer = CategorySerializer(category, data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response({'success': True, 'data': serializer.data})
#         return Response(
#             {'success': False, 'error': serializer.errors},
#             status=status.HTTP_400_BAD_REQUEST
#         )

#     elif request.method == 'DELETE':
#         category.delete()
#         return Response({'success': True}, tatus=status.HTTP_204_NO_CONTENT)


