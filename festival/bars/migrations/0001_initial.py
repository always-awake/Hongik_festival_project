# Generated by Django 2.2.1 on 2019-05-17 06:47

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
            name='Bar',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(max_length=80)),
                ('represent_image', models.ImageField(upload_to='bars')),
                ('first_image', models.ImageField(upload_to='bars')),
                ('second_image', models.ImageField(upload_to='bars')),
                ('third_image', models.ImageField(upload_to='bars')),
                ('summary', models.CharField(max_length=300, null=True)),
                ('text', models.TextField(max_length=200)),
                ('location_url', models.TextField(max_length=200)),
                ('keyword', models.CharField(max_length=80, null=True)),
                ('address', models.CharField(max_length=300, null=True)),
                ('first_menu', models.CharField(blank=True, max_length=150, null=True)),
                ('second_menu', models.CharField(blank=True, max_length=150, null=True)),
                ('third_menu', models.CharField(blank=True, max_length=150, null=True)),
                ('fourth_menu', models.CharField(blank=True, max_length=150, null=True)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='BarLike',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('bar', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='likes', to='bars.Bar')),
                ('creator', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
        ),
    ]