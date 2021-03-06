# Generated by Django 2.2.1 on 2019-05-17 06:47

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='letter',
            options={'ordering': ['-created_at']},
        ),
        migrations.RemoveField(
            model_name='letter',
            name='check',
        ),
        migrations.AddField(
            model_name='letter',
            name='check_from',
            field=models.BooleanField(default=False, null=True),
        ),
        migrations.AddField(
            model_name='letter',
            name='check_to',
            field=models.BooleanField(default=False, null=True),
        ),
        migrations.AddField(
            model_name='letter',
            name='delete_from',
            field=models.BooleanField(default=False, null=True),
        ),
        migrations.AddField(
            model_name='letter',
            name='delete_to',
            field=models.BooleanField(default=False, null=True),
        ),
        migrations.AddField(
            model_name='user',
            name='name',
            field=models.CharField(max_length=140, null=True),
        ),
        migrations.AddField(
            model_name='user',
            name='phone',
            field=models.CharField(max_length=225, null=True),
        ),
        migrations.AlterField(
            model_name='letter',
            name='letter_from',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, related_name='letter_from', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='letter',
            name='letter_to',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, related_name='letter_to', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='user',
            name='profile_image',
            field=models.ImageField(blank=True, null=True, upload_to='profile_images'),
        ),
        migrations.AlterField(
            model_name='user',
            name='profile_open',
            field=models.BooleanField(default=True, null=True),
        ),
    ]
