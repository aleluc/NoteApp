# Generated by Django 3.2.5 on 2021-09-19 18:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('notes', '0016_alter_note_expiration_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='note',
            name='public',
            field=models.BooleanField(default=False),
        ),
    ]