from rest_framework.decorators import api_view, permission_classes, parser_classes
from rest_framework.response import Response
from snips.models import *
from api.serializers import *

@api_view(['GET'])
def get_tag(request, id):
    tag = Tag.objects.get(pk=id)
    serializer = TagSerializer(tag)
    return Response(serializer.data)

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
        return Response({"error": True, "message": "data not in valid format."})

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
        tag = Tag.objects.get (pk = id)
        # print(tag)
        tag.delete()
        return Response({"message": "object deleted successfully."})
    except:
        return Response({"error": "tag does not exist."})

@api_view(['GET'])
def get_snip(request, id):
    snip = Snip.objects.get(pk=id)
    serializer = SnipSerializer(snip)
    return Response(serializer.data)