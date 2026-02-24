from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.views import APIView
from rest_framework import viewsets

from .serializers import ClientSerializer, ProductsSerializer
from lesson_5.models import Client, Products


@api_view(['GET', 'POST'])
def ping(request):
    if request.method == 'POST':
        return Response(request.data)
    return Response({'message': 'PONG'})


class PongView(APIView):
    def get(self, request):
        return Response({'message': 'PONG'})

    def post(self, request):
        return Response(request.data)


class ClientViewSet(viewsets.ModelViewSet):
    queryset = Client.objects.all()
    serializer_class = ClientSerializer


class ProductsViewSet(viewsets.ModelViewSet):
    queryset = Products.objects.all()
    serializer_class = ProductsSerializer



