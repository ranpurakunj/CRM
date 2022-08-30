from rest_framework import generics

from api.mixins import StaffEditorPermissionMixin

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
    #     return user.objects.filter(pk=self.lookup_field)

    def perform_update(self, serializer):
        serializer.save(user=self.request.user)  
         

profile_update_view = ProfileUpdateAPIView.as_view()

class ProfileDestroyAPIView(StaffEditorPermissionMixin, generics.DestroyAPIView):
    queryset=Profile.objects.all()
    serializer_class = ProfileSerializer
    lookup_field = 'pk'

    def perform_destroy(self, instance):
        return super().perform_destroy(instance) 

profile_delete_view = ProfileDestroyAPIView.as_view()
