from django.db.models import fields
from snips.models import *
from rest_framework import serializers

class LanguageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Language
        fields = '__all__'
        extra_kwargs = {
            'id': {'read_only': False, 'required': False},
            'language': {'validators': []}
            }

class LanguagesSerializer(serializers.Serializer):
    languages = LanguageSerializer(many=True)

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
    language = LanguageSerializer()
    tags = TagSerializer(many = True)
    class Meta:
        model = Snip
        fields = '__all__'
        extra_kwargs = {
            'id': {'read_only': False, 'required': False},
            'title': {'validators': []}
        }

    def create(self, validated_data):
        # print(validated_data)
        tags = validated_data.pop("tags")
        language = validated_data.pop("language")
        snip = Snip(**validated_data)
        languageObj, created = Language.objects.get_or_create(**language)
        snip.language = languageObj
        snip.save()
        for tag in tags:
            tagObj, created = Tag.objects.get_or_create(**tag)
            # print(tagObj)
            snip.tags.add(tagObj)        
        return SnipSerializer(snip).data

    def update(self, validated_data):
        id = validated_data.pop("id")
        tags = validated_data.pop("tags")
        language = validated_data.pop("language")
        snip = Snip.objects.get(pk = id)
        snip.title = validated_data['title']
        snip.description = validated_data['description']
        snip.snippet = validated_data['snippet']
        snip.pinned = validated_data['pinned']
        languageObj, created = Language.objects.get_or_create(**language)
        snip.language = languageObj
        snip.save()
        tagObjList = []
        for tag in tags:
            tagObj, created = Tag.objects.get_or_create(**tag)
            tagObjList.append(tagObj)
        for tag_ in snip.tags.all():
            if tag_ not in tagObjList:
                # print(f"{tag_} is to be remove()ed.")
                snip.tags.remove(tag_)
        for tag in tagObjList:
            if tag not in snip.tags.all():
                # print(f"{tag} is to be add()ed.")
                snip.tags.add(tag)
        return SnipSerializer(snip).data

class SnipsSerializer(serializers.Serializer):
    snips = SnipSerializer(many = True)

class ShallowSnipSerializer(serializers.ModelSerializer):

    class Meta:
        model = Snip
        fields = '__all__'
        extra_kwargs = {
            'id': {'read_only': False, 'required': False},
            'title': {'validators': []}
        }

    def create(self, validated_data):
        # print(validated_data)
        tags = validated_data.pop("tags")
        language = validated_data.pop("language")
        snip = Snip(**validated_data)
        # languageObj, created = Language.objects.get_or_create(**language)
        snip.language = Language.objects.get(pk=language)
        snip.save()
        for tag in tags:
            # tagObj, created = Tag.objects.get_or_create(**tag)
            # print(tagObj)
            snip.tags.add(Tag.objects.get(pk=tag))        
        return ShallowSnipSerializer(snip).data

    def update(self, validated_data):
        id = validated_data.pop("id")
        tags = validated_data.pop("tags")
        language = validated_data.pop("language")
        snip = Snip.objects.get(pk = id)
        snip.title = validated_data['title']
        snip.description = validated_data['description']
        snip.snippet = validated_data['snippet']
        snip.pinned = validated_data['pinned']
        # languageObj, created = Language.objects.get_or_create(**language)
        snip.language = Language.objects.get(pk=language)
        snip.save()
        tagObjList = []
        for tag in tags:
            # tagObj, created = Tag.objects.get_or_create(**tag)
            tagObjList.append(Tag.objects.get(pk=tag))
        for tag_ in snip.tags.all():
            if tag_ not in tagObjList:
                # print(f"{tag_} is to be remove()ed.")
                snip.tags.remove(tag_)
        for tag in tagObjList:
            if tag not in snip.tags.all():
                # print(f"{tag} is to be add()ed.")
                snip.tags.add(tag)
        return ShallowSnipSerializer(snip).data

class ShallowSnipsSerializer(serializers.Serializer):
    snips = ShallowSnipSerializer(many = True)