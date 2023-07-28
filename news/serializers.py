from rest_framework import serializers
from taggit.serializers import (TagListSerializerField,
                                TaggitSerializer)
from .models import TextNewsModel, AudioNewsModel

class TextNewsSerializer(serializers.ModelSerializer):
    tags = TagListSerializerField()
    class Meta:
        model = TextNewsModel
        fields = (
            'id',
            'created_at',
            'updated_at',
            'title',
            'view_count',
            'author',
            'category',
            'region',
            'cover_img',
            'tags',
            'body',
        )
    
    def get_tags(self, obj):
        return [tag.name for tag in obj.tags.all()]


class TextNewsPostSerializer(serializers.ModelSerializer):
    tags = TagListSerializerField()
    class Meta:
        model = TextNewsModel
        fields = (
            'id',
            'created_at',
            'updated_at',
            'title',
            'category',
            'region',
            'cover_img',
            'tags',
            'body',
        )


class AudioNewsSerializer(serializers.ModelSerializer):
    class Meta:
        model = AudioNewsModel
        fields = (
            'id',
            'created_at',
            'updated_at',
            'title',
            'view_count',
            'author',
            'audio'
        )


class AudioNewsPostSerializer(serializers.ModelSerializer):
    class Meta:
        model = AudioNewsModel
        fields = (
            'id',
            'created_at',
            'updated_at',
            'title',
            'audio'
        )