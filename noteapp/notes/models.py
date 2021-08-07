from django.db import models
from django.db.models import fields
from django.contrib.auth.models import User


class Note(models.Model):
    title = fields.CharField(max_length=20)
    content = fields.TextField(default="")
    creation_date = fields.DateTimeField(auto_now=True)
    owner = models.ForeignKey(User)
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
        self.shared_with.add(user_id)

    def check_permission(self, user_id):
        if user_id in [self.owner, list(self.shared_with.all())]:
            return True
        return False
