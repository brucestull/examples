# Generated by Django 4.1.3 on 2022-12-11 01:38

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('things', '0002_alter_thing_owner'),
    ]

    operations = [
        migrations.AlterField(
            model_name='thing',
            name='owner',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='owner_related_name_for_things', to=settings.AUTH_USER_MODEL),
        ),
    ]