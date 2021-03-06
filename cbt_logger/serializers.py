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

class CbtLogSerializer(serializers.ModelSerializer):
    class Meta:
        model = CbtLog
        fields = ('id', 'title', 'published', 'log_type')
        

    def create(self, validated_data):
        """
        Create and return a new `Snippet` instance, given the validated data.
        """
        return CbtLog.objects.create(**validated_data)

    def update(self, instance, validated_data):
        """
        Update and return an existing `Snippet` instance, given the validated data.
        """
        instance.title = validated_data.get('title', instance.title)
        instance.published = validated_data.get('published', instance.published)
        instance.log_type = validated_data.get('log_type', instance.log_type)
        instance.save()
        return instance
