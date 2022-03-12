# Generated by Django 4.0.3 on 2022-03-14 15:10

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0010_comment_created'),
    ]

    operations = [
        migrations.CreateModel(
            name='Question',
            fields=[
                ('answer', models.CharField(choices=[('backend', 'backend'), ('frontend', 'frontend'), ('fullstack', 'fullstack')], max_length=200)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True)),
            ],
        ),
    ]