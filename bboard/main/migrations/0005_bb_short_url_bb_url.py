# Generated by Django 4.2.5 on 2023-09-28 11:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0004_comment'),
    ]

    operations = [
        migrations.AddField(
            model_name='bb',
            name='short_url',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='bb',
            name='url',
            field=models.URLField(blank=True, max_length=700, null=True),
        ),
    ]