# Generated by Django 2.2.11 on 2021-04-02 17:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('snips', '0003_snip_description'),
    ]

    operations = [
        migrations.AlterField(
            model_name='snip',
            name='pinned',
            field=models.BooleanField(default=False),
        ),
    ]
