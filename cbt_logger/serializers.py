from django.contrib.auth.models import User, Group

from rest_framework import serializers
from cbt_logger.models import CbtLog, LOG_TYPE_CHOICES

class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('url', 'username', 'email', 'groups')


class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ('url', 'name')

class CbtLogSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    title = serializers.CharField(required=False, allow_blank=True, max_length=100)
    published = serializers.BooleanField(required=False)
    log_type = serializers.ChoiceField(choices=LOG_TYPE_CHOICES, default='quick_add')

    def create(self, validated_data):
        """
        Create and return a new `Snippet` instance, given the validated data.
        """
        return Snippet.objects.create(**validated_data)

    def update(self, instance, validated_data):
        """
        Update and return an existing `Snippet` instance, given the validated data.
        """
        instance.title = validated_data.get('title', instance.title)
        instance.published = validated_data.get('published', instance.published)
        instance.log_type = validated_data.get('log_type', instance.log_type)
        instance.save()
        return instance
