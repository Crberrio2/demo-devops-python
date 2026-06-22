from django.db import connection
from rest_framework import viewsets, status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from .serializers import UserSerializer
from .models import User


@api_view(['GET'])
@permission_classes([AllowAny])
def liveness(request):
    return Response({'status': 'ok'})


@api_view(['GET'])
@permission_classes([AllowAny])
def readiness(request):
    try:
        connection.ensure_connection()
    except Exception:
        return Response({'status': 'unavailable'}, status=status.HTTP_503_SERVICE_UNAVAILABLE)
    return Response({'status': 'ready'})


class UserViewSet(viewsets.ModelViewSet):
    serializer_class = UserSerializer
    queryset = User.objects.all()

    def list(self, request):
        serializer = self.get_serializer(self.get_queryset(), many=True)
        return Response(serializer.data)

    def retrieve(self, request, pk):
        serializer = self.get_serializer(self.get_object())
        return Response(serializer.data)

    def create(self, request):
        data = request.data

        if self.get_queryset().filter(dni=data.get('dni', '')).exists():
            return Response({'detail': 'User already exists'}, status=400)

        serializer = self.get_serializer(data=data)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response(serializer.data, status=201)
