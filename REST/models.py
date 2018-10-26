from django.db import models


class Photo(models.Model):
    title = models.CharField(blank=True, max_length=100)
    id = models.CharField(primary_key=True, max_length=100)
    group = models.ForeignKey('Group', on_delete=models.DO_NOTHING, related_name=None, default=None)
    server = models.CharField(max_length=100)
    secret = models.CharField(max_length=100)
    farm = models.IntegerField()
    is_public = models.IntegerField()
    is_friend = models.IntegerField()
    is_family = models.IntegerField()
    date_added = models.CharField(max_length=100)

    class Meta:
        db_table = 'photos'


class Group(models.Model):
    group_id = models.CharField(primary_key=True,max_length=100)
    group_name = models.CharField(max_length=100)
    no_photos = models.IntegerField()

    class Meta:
        db_table = 'group'
