
from rest_framework import permissions


class IsStaffEditorPermission(permissions.DjangoModelPermissions):
    perms_map = {
        'GET': ['%(app_label)s.view_%(model_name)s'],
        'OPTIONS': [],
        'HEAD': [],
        'POST': ['%(app_label)s.add_%(model_name)s'],
        'PUT': ['%(app_label)s.change_%(model_name)s'],
        'PATCH': ['%(app_label)s.change_%(model_name)s'],
        'DELETE': ['%(app_label)s.delete_%(model_name)s'],
    }


    def has_permission(self, request, view):
        if not request.user.is_staff:
            return False
        return super().has_permission(request, view)
    
    
    # def has_permission(self, request, view):
    #     user = request.user
    #     print(user.get_all_permissions())
    #     if request.user.is_staff:
    #         if user.has_perm("profile.add_profile"):         # "app_name".verb_"model_name"
    #             return True
    #         if user.has_perm("profile.change_profile"):
    #             return True
    #         if user.has_perm("profile.delete_profile"):
    #             return True
    #         if user.has_perm("profile.view_profile"):
    #             return True
    #         return False
    #     return False
    