from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework_simplejwt.authentication import JWTAuthentication
from api_user.serializers import *


class MyTokenObtainPairView(TokenObtainPairView):
    serializer_class = MyTokenObtainPairSerializer

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    authentication_classes = [JWTAuthentication]
    serializers = {
        'list': UserListSerializer,
        'create': UserCreateSerializer,
        'update': UserCreateSerializer,
    }

    def get_serializer_class(self):
        return self.serializers.get(self.action, self.serializers['list'])

    def create(self, request, *args, **kwargs):
        user = request.data
        user_serializer = self.get_serializer(data=user)
        try:
            if user_serializer.is_valid(raise_exception=True):
                user_serializer.save()
                return Response(user_serializer.data, status=status.HTTP_200_OK)
        except Exception as e:
            return Response(e, status=status.HTTP_400_BAD_REQUEST)
        return Response(user_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def update(self, request, *args, **kwargs):
        user = self.get_object()
        data = request.data
        serializer = self.get_serializer(user, data=data, partial=True)
        try:
            if serializer.is_valid(raise_exception=True):
                serializer.save()
                return Response(serializer.data, status=status.HTTP_200_OK)
        except Exception as e:
            return Response(e, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_200_OK)

    def destroy(self, request, *args, **kwargs):
        # id_user = kwargs.get('pk', None)
        user = self.get_object()
        if user.place:
            Place.objects.get(pk=user.place.id).delete()
        if user:
            user.delete()
            return Response('User is deleted.', status=status.HTTP_200_OK)
        return Response('User is not exist!', status=status.HTTP_404_NOT_FOUND)


class RoleViewSet(viewsets.ModelViewSet):
    serializer_class = RoleSerializer
    queryset = Role.objects.all()
    authentication_classes = [JWTAuthentication]

class PlaceViewSet(viewsets.ModelViewSet):
    serializer_class = PlaceSerializer
    queryset = Place.objects.all()
    authentication_classes = [JWTAuthentication]

    def destroy(self, request, *args, **kwargs):
        return Response("FORBIDDEN",status=status.HTTP_403_FORBIDDEN)
