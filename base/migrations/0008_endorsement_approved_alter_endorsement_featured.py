# Generated by Django 4.0.3 on 2022-03-14 14:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0007_endorsement'),
    ]

    operations = [
        migrations.AddField(
            model_name='endorsement',
            name='approved',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='endorsement',
            name='featured',
            field=models.BooleanField(default=False, null=True),
        ),
    ]
