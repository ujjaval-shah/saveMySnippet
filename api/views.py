from rest_framework.decorators import api_view, permission_classes, parser_classes
from rest_framework.response import Response
from snips.models import *
from api.serializers import *
from rest_framework import status
from django.core.exceptions import ObjectDoesNotExist

@api_view(['GET'])
def get_languages(request):
    languages = Language.objects.all()
    serializer = LanguagesSerializer({"languages":languages})
    return Response(serializer.data)

@api_view(['POST'])
def create_languages(request):
    languages_serializer = LanguagesSerializer(data=request.data)
    if languages_serializer.is_valid():
        totalCreated = 0
        for langDict in languages_serializer.data['languages']:
            langObj, created = Language.objects.get_or_create(**langDict)
            totalCreated += int(created)
        return Response({"message": f"{totalCreated} new languages added."}, status= status.HTTP_201_CREATED)
    else:
        return Response({"error": True, "message": "data not in valid format."}, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
def get_tag(request, id):
    try:
        tag = Tag.objects.get(pk=id)
        serializer = TagSerializer(tag)
        return Response(serializer.data)
    except ObjectDoesNotExist:
        return Response({"error": "tag does not exist."}, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
def get_tags(request):
    tags = Tag.objects.all()
    serializer = TagsSerializer({"tags":tags})
    return Response(serializer.data)

@api_view(['POST'])
def create_tag(request):
    tag_serializer = TagSerializer(data= request.data)
    if tag_serializer.is_valid():
        return Response(tag_serializer.create(tag_serializer.validated_data))
    else:
        print(tag_serializer.errors)
        return Response({"error": True, "message": "data not in valid format."}, status=status.HTTP_400_BAD_REQUEST)

@api_view(['PUT'])
def update_tag(request):
    tag_serializer = TagSerializer(data= request.data)
    if tag_serializer.is_valid():
        return Response(tag_serializer.update(tag_serializer.validated_data))
    else:
        print(tag_serializer.errors)
        return Response({"error": True, "message": "data not in valid format."})

@api_view(['DELETE'])
def delete_tag(request, id):
    try:
        tag = Tag.objects.get(pk = id)
        # print(tag)
        tag.delete()
        return Response({"message": "object deleted successfully."})
    except ObjectDoesNotExist:
        return Response({"error": "tag does not exist."}, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
def get_snip(request, id):
    try:
        snip = Snip.objects.get(pk=id)
        serializer = ShallowSnipSerializer(snip)
        return Response(serializer.data)
    except ObjectDoesNotExist:
        return Response({"error": "snip does not exist."}, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
def get_snips(request):
    snips = Snip.objects.all()
    serializer = ShallowSnipsSerializer({"snips":snips})
    return Response(serializer.data)    

@api_view(['GET'])
def get_snips_by_tag(request, id):
    try:
        tag = Tag.objects.get(pk=id)
        snips = tag.snip_set.all()
        serializer = ShallowSnipsSerializer({"snips":snips})
        return Response(serializer.data)
    except ObjectDoesNotExist:
        return Response({"error": "tag does not exist."}, status=status.HTTP_400_BAD_REQUEST)

@api_view(['POST'])
def create_snip(request):
    snip_serializer = ShallowSnipSerializer(data= request.data)
    if snip_serializer.is_valid():
        return Response(snip_serializer.create(snip_serializer.validated_data))
    else:
        print(snip_serializer.errors)
        return Response({"error": True, "message": "data not in valid format."})

@api_view(['PUT'])
def update_snip(request):
    snip_serializer = ShallowSnipSerializer(data= request.data)
    if snip_serializer.is_valid():
        return Response(snip_serializer.update(snip_serializer.validated_data))
    else:
        print(snip_serializer.errors)
        return Response({"error": True, "message": "data not in valid format."})

@api_view(['DELETE'])
def delete_snip(request, id):
    try:
        snip = Snip.objects.get(pk = id)
        # print(tag)
        snip.delete()
        return Response({"message": "object deleted successfully."})
    except ObjectDoesNotExist:
        return Response({"error": "snip does not exist."}, status=status.HTTP_400_BAD_REQUEST)

@api_view(['PUT'])
def pin_snip(request, id):
    try:
        snip = Snip.objects.get(pk=id)
        snip.pinned = True
        snip.save()
        return Response({"message": "Action Successful."})
    except ObjectDoesNotExist:
        return Response({"error": "snip does not exist."}, status=status.HTTP_400_BAD_REQUEST)

@api_view(['PUT'])
def unpin_snip(request, id):
    try:
        snip = Snip.objects.get(pk=id)
        snip.pinned = False
        snip.save()
        return Response({"message": "Action Successful."})
    except ObjectDoesNotExist:
        return Response({"error": "snip does not exist."}, status=status.HTTP_400_BAD_REQUEST)