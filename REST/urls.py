from django.conf.urls import url
from .views import (
    login,
    groups,
    group_with_id,
    photos,
    logout,
)

urlpatterns = [
    url(r'^v1/login', login, name='login'),
    url(r'^v1/groups', groups, name='groups'),
    url(r'^v1/group/(?P<group_id>[@\w]+)', group_with_id, name='group_id'),
    url(r'^v1/photos/(?P<photo_id>[\w]*)', photos, name='photo_id'),
    url(r'^v1/logout', logout, name='logout'),
]

