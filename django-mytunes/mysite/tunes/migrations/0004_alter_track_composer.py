# Generated by Django 4.1.2 on 2022-12-02 18:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tunes', '0003_album_artist'),
    ]

    operations = [
        migrations.AlterField(
            model_name='track',
            name='composer',
            field=models.CharField(blank=True, max_length=220, null=True),
        ),
    ]