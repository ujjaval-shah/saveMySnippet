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

@api_view(['GET'])
def get_snip(request, id):
    snip = Snip.objects.get(pk=id)
    serializer = SnipSerializer(snip)
    return Response(serializer.data)