# Generated by Django 2.2.1 on 2019-08-14 20:26

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Contacts',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('email', models.CharField(default='something-712@gmail.com', max_length=100)),
                ('age', models.IntegerField(default=44)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name_plural': 'Contacts',
            },
        ),
        migrations.CreateModel(
            name='Sports',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('skill', models.CharField(choices=[('Beginner', 'Beginner'), ('Moderate', 'Moderate'), ('Expert', 'Expert')], max_length=100)),
                ('contact', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mainapp.Contacts')),
            ],
            options={
                'verbose_name_plural': 'Sports',
            },
        ),
        migrations.CreateModel(
            name='ProgrammingLanguages',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('skill', models.CharField(choices=[('Beginner', 'Beginner'), ('Moderate', 'Moderate'), ('Expert', 'Expert')], max_length=100)),
                ('contact', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mainapp.Contacts')),
            ],
            options={
                'verbose_name_plural': 'ProgrammingLanguages',
            },
        ),
    ]
