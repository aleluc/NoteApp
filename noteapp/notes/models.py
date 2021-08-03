from django.db import models
from django.db.models import fields
from django.contrib.auth.models import User


class Note(models.Model):
    title = fields.CharField(max_length=20)
    content = fields.TextField(default="")
    creation_date = fields.DateTimeField(auto_now=True)
    owner = models.ForeignKey(User)
    shared_with = models.ManyToManyField(User)

    def share_note(self, user_id):
        self.shared_with.add(user_id)
