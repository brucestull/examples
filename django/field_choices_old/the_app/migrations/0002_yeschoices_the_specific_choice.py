# Generated by Django 4.0 on 2022-08-25 19:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('the_app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='yeschoices',
            name='the_specific_choice',
            field=models.CharField(choices=[('FRST', 'First'), ('SCND', 'Second')], max_length=4, null=True),
        ),
    ]
