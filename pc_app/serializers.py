from rest_framework import serializers

from .models import User, Comment, Post
from .validators import PasswordValidator, EmailValidator, ForbiddenWordsValidator, AgeValidator


class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(validators=[PasswordValidator()])
    email = serializers.CharField(validators=[EmailValidator()])

    def create(self, validated_data):
        user = super().create(validated_data)

        user.set_password(user.password)
        user.save()

        return user

    def update(self, instance, validated_data):
        user = super().update(instance, validated_data)
        user.set_password(user.password)
        user.save()

        return user

    class Meta:
        model = User
        exclude = ['id', 'created_at', 'updated_at']


class CommentSerializer(serializers.ModelSerializer):
    author = serializers.SlugRelatedField(queryset=User.objects.all(), slug_field='username')

    class Meta:
        model = Comment
        exclude = ['id', 'created_at', 'updated_at']


class PostSerializer(serializers.ModelSerializer):
    comments = serializers.SlugRelatedField(queryset=Comment.objects.all(), slug_field='text', many=True)
    author = serializers.SlugRelatedField(queryset=User.objects.all(), slug_field='username', validators=[AgeValidator()])
    header = serializers.CharField(validators=[ForbiddenWordsValidator()])

    class Meta:
        model = Post
        exclude = ['id', 'created_at', 'updated_at']
