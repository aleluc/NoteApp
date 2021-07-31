from django.db import models
from django.db.models import fields


class Note(models.Model):
    title = fields.CharField(max_length=20)
    content = fields.TextField
    creation_date = fields.TimeField(auto_now_add=True)