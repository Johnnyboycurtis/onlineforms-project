# Generated by Django 2.2.1 on 2019-08-21 20:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('billing', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='billheader',
            name='submitted',
            field=models.BooleanField(default=False),
        ),
    ]
