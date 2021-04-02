from django.db.models import fields
from snips.models import *
from rest_framework import serializers

class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = '__all__'

class TagsSerializer(serializers.Serializer):
    tags = TagSerializer(many = True)

class SnipSerializer(serializers.ModelSerializer):
    tags = TagSerializer(many = True)
    class Meta:
        model = Snip
        fields = '__all__'
