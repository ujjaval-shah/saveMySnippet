from django.db.models import fields
from snips.models import *
from rest_framework import serializers

class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = '__all__'
        extra_kwargs = {
            'id': {'read_only': False, 'required': False},
            'tag': {'validators': []}
            }

    def create(self, validated_data):
        tag, created = Tag.objects.get_or_create( **validated_data )
        # print(tag)
        return TagSerializer(tag).data

    def update(self, validated_data):
        id = validated_data.pop("id")
        tag = Tag.objects.get(pk = id)
        tag.tag = validated_data["tag"]
        tag.save()
        return TagSerializer(tag).data

class TagsSerializer(serializers.Serializer):
    tags = TagSerializer(many = True)

class SnipSerializer(serializers.ModelSerializer):
    tags = TagSerializer(many = True)
    class Meta:
        model = Snip
        fields = '__all__'
