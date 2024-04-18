# Generated by Django 4.2.6 on 2024-04-18 14:23

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_election_position_user_profile_picture_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='position',
            name='user',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]