# -*- coding: utf-8 -*-

from rest_framework import serializers, generics, views, response, permissions
from django_filters import rest_framework as filters
# from django.contrib.auth.models import User
from .models import User
# from rest_framework.decorators import api_view


class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ('id', 'username', 'last_login', 'is_superuser', 'is_staff')

#
# class UserList(generics.ListAPIView):
#     queryset = User.objects.all()
#     serializer_class = UserSerializer
#     filter_backends = (filters.DjangoFilterBackend,)
#     # filterset_fields = ('title', 'severity', 'engine_type')
#


class CurrentUserView(views.APIView):
    # authentication_classes = [SessionAuthentication, BasicAuthentication, JWTAuthentication]
    # permission_classes = [IsAuthenticated]
    # permission_classes = [permissions.IsAdminUser]

    # @api_view(['GET', 'OPTIONS', 'POST'])
    def get(self, request):
        serializer = UserSerializer(request.user, context={'request': request})
        # print(serializer)
        # print(self.check_object_permissions(self.request, serializer))
        return response.Response(serializer.data)