# Generated by Django 3.2.3 on 2022-03-04 09:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cricket', '0002_batsman'),
    ]

    operations = [
        migrations.AddField(
            model_name='batsman',
            name='bowls',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='batsman',
            name='run',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
