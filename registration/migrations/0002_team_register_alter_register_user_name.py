# Generated by Django 4.0.1 on 2023-01-18 14:20

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('registration', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='team_register',
            fields=[
                ('team_id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('team_name', models.CharField(max_length=10)),
                ('team_email', models.CharField(max_length=20)),
                ('team_password', models.CharField(max_length=10)),
            ],
        ),
        migrations.AlterField(
            model_name='register',
            name='user_name',
            field=models.CharField(max_length=20),
        ),
    ]
