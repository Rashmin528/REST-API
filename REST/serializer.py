from rest_framework import serializers
from .models import Group, Photo


class GroupSerializers(serializers.ModelSerializer):
    class Meta:
        model = Group
        fields = [
            'group_id',
            'no_photos',
            'group_name'
        ]


class PhotoSerializers(serializers.ModelSerializer):
    class Meta:
        model = Photo
        fields = [
            'id',
            'title',
            'server',
            'secret',
            'farm',
            'group',
            'is_public',
            'is_friend',
            'is_family',
            'date_added',
        ]


class PhotoIdSerializers(serializers.ModelSerializer):
    class Meta:
        model = Photo
        fields = [
            'id'
        ]
