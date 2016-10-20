from __future__ import unicode_literals
from django.db import models
  # Create your models here.
class Course(models.Model):
      name = models.CharField(max_length = 100)
      description = models.TextField(max_length = 1000)
    #   first_name = models.CharField(max_length=45)
    #   last_name = models.CharField(max_length=45)
    #   password = models.CharField(max_length=100)
      created_at = models.DateTimeField(auto_now_add = True)
      updated_at = models.DateTimeField(auto_now = True)
# class Comment(models.Model):
#     #   title = models.CharField(max_length = 100)
#       comment = models.TextField(max_length = 1000)
#       blog = models.ForeignKey(Blog)
#     #   first_name = models.CharField(max_length=45)
#     #   last_name = models.CharField(max_length=45)
#     #   password = models.CharField(max_length=100)
#       created_at = models.DateTimeField(auto_now_add = True)
#       updated_at = models.DateTimeField(auto_now = True)
# # Create your models here.

