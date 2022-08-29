from argparse import ArgumentDefaultsHelpFormatter
from ast import arg
from distutils.util import Mixin2to3
from urllib import request
from rest_framework import authentication,generics,mixins, permissions
from rest_framework.decorators import api_view
from rest_framework.response import Response

from django.shortcuts import get_object_or_404

from api.mixins import StaffEditorPermissionMixin
from api.authentication import TokenAuthentication
from api.permissions import IsStaffEditorPermission
from .models import Profile
from .serializers import ProfileSerializer 

# class ProfileCreateAPIView(StaffEditorPermissionMixin,generics.CreateAPIView):
#     queryset = Profile.objects.all()
#     serializer_class = ProfileSerializer

#     def perform_create(self,serializer):
#         # serializer.save(user=self.request.user)
#         serializer.save()
        
# profile_create_view = ProfileCreateAPIView.as_view()

class ProfileListCreateAPIView(StaffEditorPermissionMixin, generics.ListCreateAPIView):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer

    def perform_list_create(self,serializer):
        serializer.save(user=self.request.user)
    def get_queryset(self, *args, **kwargs):
        request = self.request
        user= request.user
        if not user.is_authenticated:
            return Profile.objects.none()
        print(request.user)
        return super().get_queryset(*args, **kwargs)
profile_list_create_view = ProfileListCreateAPIView.as_view()

class ProfileDetailAPIView(StaffEditorPermissionMixin, generics.RetrieveAPIView):
    queryset=Profile.objects.all()
    serializer_class = ProfileSerializer

profile_detail_view = ProfileDetailAPIView.as_view()

class ProfileUpdateAPIView(StaffEditorPermissionMixin, generics.UpdateAPIView):
    queryset=Profile.objects.all()
    serializer_class = ProfileSerializer
    lookup_field = 'pk'

    # def get_queryset(self):
    #     user=self.request.user
    #     return user.accounts.all()

    def perform_update(self, serializer):
        serializer.save(self.request.user)  
         

profile_update_view = ProfileUpdateAPIView.as_view()

class ProfileDestroyAPIView(StaffEditorPermissionMixin, generics.DestroyAPIView):
    queryset=Profile.objects.all()
    serializer_class = ProfileSerializer
    lookup_field = 'pk'

    def perform_destroy(self, instance):
        return super().perform_destroy(instance) 

profile_delete_view = ProfileDestroyAPIView.as_view()
