# Generated by Django 3.1.1 on 2020-10-28 22:34

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('hackathon', '0020_merge_20201026_2056'),
    ]

    operations = [
        migrations.AddField(
            model_name='hackathon',
            name='participants',
            field=models.ManyToManyField(blank=True, related_name='hackathon_participants', to=settings.AUTH_USER_MODEL),
        ),
    ]