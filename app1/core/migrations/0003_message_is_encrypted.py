# Generated by Django 5.0.3 on 2024-12-14 04:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_rename_encrypted_content_message_content_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='message',
            name='is_encrypted',
            field=models.BooleanField(default=True),
        ),
    ]
