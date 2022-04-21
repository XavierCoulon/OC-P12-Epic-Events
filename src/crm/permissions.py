from rest_framework import permissions
from rest_framework.permissions import DjangoModelPermissions, BasePermission, SAFE_METHODS


# class SalesPermission(BasePermission):
#     def has_permission(self, request, view):
#         if request.method in SAFE_METHODS:
#             return True
#         return request.user.groups.filter(name="Sales").exists()
#
#
# class SupportPermission(BasePermission):
#     def has_permission(self, request, view):
#         if request.method in SAFE_METHODS:
#             return True
#         return request.user.groups.filter(name="Support").exists()


class CustomDjangoModelPermissions(DjangoModelPermissions):

    perms_map = {
        'GET': ['%(app_label)s.view_%(model_name)s'],
        'OPTIONS': [],
        'HEAD': [],
        'POST': ['%(app_label)s.add_%(model_name)s'],
        'PUT': ['%(app_label)s.change_%(model_name)s'],
        'PATCH': ['%(app_label)s.change_%(model_name)s'],
        'DELETE': ['%(app_label)s.delete_%(model_name)s'],
    }

    def get_required_permissions(self, method, model_cls):
        """
        Given a model and an HTTP method, return the list of permission
        codes that the user is required to have.
        """

        kwargs = {
            'app_label': model_cls._meta.app_label,
            'model_name': model_cls._meta.model_name
        }

        print(kwargs)

        if method not in self.perms_map:
            raise exceptions.MethodNotAllowed(method)

        print([perm % kwargs for perm in self.perms_map[method]])

        return [perm % kwargs for perm in self.perms_map[method]]

    def has_permission(self, request, view):
        # Workaround to ensure DjangoModelPermissions are not applied
        # to the root view when using DefaultRouter.
        if getattr(view, '_ignore_model_permissions', False):
            return True

        if not request.user or (
           not request.user.is_authenticated and self.authenticated_users_only):
            return False

        queryset = self._queryset(view)
        perms = self.get_required_permissions(request.method, queryset.model)
        print(perms)
        print(request.user.has_perms(perms))
        print(request.user)
        print(request.user.get_all_permissions())
        return request.user.has_perms(perms)
