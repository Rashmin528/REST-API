from django.contrib.auth import authenticate
from django.views.decorators.csrf import csrf_exempt
from rest_framework.authtoken.models import Token
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework import status
from rest_framework.status import (
    HTTP_400_BAD_REQUEST,
    HTTP_404_NOT_FOUND,
    HTTP_200_OK
)
from .models import Photo, Group
from .serializer import PhotoSerializers, GroupSerializers, PhotoIdSerializers
from rest_framework.pagination import LimitOffsetPagination

MAX_PAGE_SIZE = 30
paginator = LimitOffsetPagination()
paginator.default_limit = MAX_PAGE_SIZE


@csrf_exempt
@api_view(["POST"])
@permission_classes((AllowAny,))
def login(request):
    username = request.data.get("username")
    password = request.data.get("password")
    if username is None or password is None:
        return Response({'error': 'Please provide both username and password'},
                        status=HTTP_400_BAD_REQUEST)
    user = authenticate(username=username, password=password)
    if not user:
        return Response({'error': 'Invalid Credentials'},
                        status=HTTP_404_NOT_FOUND)
    token, _ = Token.objects.get_or_create(user=user)
    return Response({'token': token.key},
                    status=HTTP_200_OK)


@csrf_exempt
@api_view(["POST"])
def logout(request):
    request.user.auth_token.delete()
    return Response(status=status.HTTP_200_OK)


@csrf_exempt
@api_view(["POST"])
def groups(request):
    g = GroupSerializers(Group.objects.all(), many=True)
    data = {'groups': g.data }
    return Response(data, status=HTTP_200_OK, content_type='application/json')


@csrf_exempt
@api_view(["POST"])
def group_with_id(request, group_id):
    page_data = paginator.paginate_queryset(PhotoIdSerializers(
        Photo.objects.filter(group_id=group_id), many=True).data, request)
    data = {
        'result': page_data,
        'limit': paginator.limit,
        'offset': paginator.offset,
        'overall_count': paginator.count
    }
    return Response(data, status=HTTP_200_OK, content_type='application/json')


@csrf_exempt
@api_view(["POST"])
def photos(request, photo_id=None):
    if not photo_id and request.GET.get('group'):
        group_id = request.GET.get('group')
        page_data = paginator.paginate_queryset(
            PhotoSerializers(Photo.objects.filter(group_id=group_id), many=True).data,
            request)
        data = {
            'result': page_data,
            'limit': paginator.limit,
            'offset': paginator.offset,
            'overall_count': paginator.count
        }
    else:
        data = PhotoSerializers(Photo.objects.get(id=photo_id), many=False).data
    return Response(data, status=HTTP_200_OK, content_type='application/json')