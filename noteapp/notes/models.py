from django.db import models
from django.db.models import fields
from django.contrib.auth.models import User
from django.utils import timezone
import datetime


class Note(models.Model):
    title = fields.CharField(max_length=20)
    content = fields.TextField(default="")
    creation_date = fields.DateTimeField(auto_now=True)
    expires = fields.BooleanField(default=False)
    expiration_date = fields.DateField(default=timezone.now)
    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name='owner')
    shared_with = models.ManyToManyField(User)

    def set_title(self, title):
        self.title = title

    def get_title(self):
        return self.title

    def set_content(self, content):
        self.content = content

    def get_content(self):
        return self.content

    def share_note(self, user_id):
        if user_id != self.owner.id:
            self.shared_with.add(user_id)

    def check_permission(self, user_id):
        users = list(self.shared_with.all())
        users.append(self.owner)
        if user_id in users:
            return True
        return False

    def is_expired(self):
        if self.expires and self.expiration_date < datetime.date.today():
            return True
        else:
            return False
