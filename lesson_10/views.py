from .serializers import UserSerializer

from rest_framework.generics import CreateAPIView
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response
from rest_framework.status import HTTP_200_OK

from rest_framework.authtoken.models import Token
from rest_framework.decorators import api_view, permission_classes
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth import authenticate

from rest_framework.viewsets import ModelViewSet
from .serializers import ProductsModelSerializer
from lesson_5.models import Products

from rest_framework.views import APIView
from datetime import datetime
import pytz


class CreateUser(CreateAPIView):
    permission_classes = (AllowAny,)
    serializer_class = UserSerializer


@csrf_exempt
@api_view(["POST"])
@permission_classes((AllowAny,))
def user_login(request):
    if request.method == 'POST':
        username = request.data.get('username')
        password = request.data.get('password')

        user = authenticate(request, username=username, password=password)
        if user is None:
            return Response({'error': 'Invalid username or password.'})

        token, _ = Token.objects.get_or_create(user=user)

        return Response({'token': token.key}, status=HTTP_200_OK)


class ProductViewSet(ModelViewSet):
    permission_classes = (IsAuthenticated,)
    serializer_class = ProductsModelSerializer

    def get_queryset(self):
        queryset = Products.objects.all().order_by('id', 'delivered_at')

        name = self.request.query_params.get('name')
        if name:
            queryset = queryset.filter(name__contains=name)
        return queryset


@api_view(['GET','POST'])
@permission_classes((AllowAny,))
def get_time(request):
    if request.method == 'GET':
        tz_name = request.query_params.get('tz', 'UTC')
    elif request.method == 'POST':
        tz_name = request.data.get('tz', 'UTC')

    try:
        timezone = pytz.timezone(tz_name)
    except pytz.exceptions.UnknownTimeZoneError:
        return Response({'error': 'Invalid timezone'})

    now = datetime.now(timezone)

    return Response({
        'timezone': tz_name,
        'time': now.strftime('%H:%M:%S')
    })










