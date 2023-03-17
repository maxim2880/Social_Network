from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated, AllowAny, IsAdminUser

from pc_app.models import User, Post, Comment
from pc_app.permissions import PermissionPolicyMixin, AdminOrOwnerPermission
from pc_app.serializers import UserSerializer, PostSerializer, CommentSerializer


class UserViewSet(PermissionPolicyMixin, viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    permission_classes_per_method = {
        'list': [IsAdminUser, IsAuthenticated],
        'create': [AllowAny],
        'update': [AdminOrOwnerPermission],
        'destroy': [IsAdminUser],
    }


class PostViewSet(PermissionPolicyMixin, viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

    permission_classes_per_method = {
        'list': [AllowAny],
        'create': [IsAuthenticated],
        'update': [AdminOrOwnerPermission],
        'destroy': [AdminOrOwnerPermission],
    }


class CommentViewSet(PermissionPolicyMixin, viewsets.ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer

    permission_classes_per_method = {
        'list': [AllowAny],
        'create': [IsAuthenticated],
        'update': [AdminOrOwnerPermission],
        'destroy': [AdminOrOwnerPermission],
    }

    def perform_destroy(self, instance: Comment):
        instance.is_active = False
        instance.save()
