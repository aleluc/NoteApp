# Generated by Django 3.2.5 on 2021-09-05 19:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('notes', '0011_alter_note_expiration_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='note',
            name='expiration_date',
            field=models.DateField(),
        ),
    ]
