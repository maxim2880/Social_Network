from rest_framework.permissions import BasePermission


class PermissionPolicyMixin:
    def check_permissions(self, request):
        try:
            handler = getattr(self, request.method.lower())
        except AttributeError:
            handler = None

        if handler and self.permission_classes_per_method and self.permission_classes_per_method.get(handler.__name__):
            self.permission_classes = self.permission_classes_per_method.get(handler.__name__)

        super().check_permissions(request)


class AdminOrOwnerPermission(BasePermission):
    message = 'Совершать действие может только администратор и сам пользователь'

    def has_object_permission(self, request, view, user):
        return bool(request.user == user or request.user.is_staff)
