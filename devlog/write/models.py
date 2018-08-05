from __future__ import unicode_literals
from django.db import models
from datetime import datetime

class comments(models.Model):
    comment_ID = models.BigIntegerField(primary_key=True)
    comment_post_ID = models.BigIntegerField(default=0)
    comment_author = models.CharField(max_length=255)
    comment_author_email = models.CharField(max_length=100, default='')
    comment_date = models.DateTimeField(default=datetime.now)
    comment_date_gmt = models.DateTimeField(default=datetime.now)
    comment_content = models.TextField(default=datetime.now)
    comment_type = models.CharField(max_length=20, default='')
    user_id = models.BigIntegerField(default=0)
    def __int__(self):
        return self.comment_ID
    def __str__(self):
        return str(self.comment_ID)

class users (models.Model):
    ID = models.BigIntegerField(primary_key=True)
    user_login = models.CharField(max_length=60, default='')
    user_pass = models.CharField(max_length=255, default='')
    user_nickname = models.CharField(max_length=50, default='')
    user_email = models.CharField(max_length=100, default='')
    user_registered = models.DateTimeField(default=datetime.now)
    user_status = models.IntegerField(default=0)
    display_name = models.CharField(max_length=250, default='')
    def __int__(self):
        return self.ID
    def __str__(self):
        return str(self.ID)

class posts (models.Model):
    ID = models.BigIntegerField(primary_key=True)
    post_author = models.CharField(max_length=20)
    post_date = models.DateTimeField(default=datetime.now)
    post_content = models.TextField()
    post_title = models.TextField()
    post_status = models.CharField(max_length=20, default='publish')
    comment_status = models.CharField(max_length=20, default='open')
    post_password = models.CharField(max_length=255, default='')
    post_name = models.CharField(max_length=250, default='')
    post_modified = models.DateTimeField(default=datetime.now)
    post_type = models.CharField(max_length=20, default='post')
    comment_count = models.BigIntegerField(default=0)
    category_ID2 = models.BigIntegerField()
    def __int__(self):
        return self.ID
    def __str__(self):
        return str(self.ID)

class categories (models.Model):
    category_ID = models.BigIntegerField(primary_key=True)
    category_name = models.CharField(max_length=100)
    category_level = models.IntegerField()
    category_line = models.IntegerField()
    def __int__(self):
        return self.category_ID
    def __str__(self):
        return str(self.category_ID)
