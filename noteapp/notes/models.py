from django.db import models
from django.db.models import fields


class Note(models.Model):
    title = fields.CharField(max_length=20)
    content = fields.TextField(default="")
    creation_date = fields.DateTimeField(auto_now=True)
