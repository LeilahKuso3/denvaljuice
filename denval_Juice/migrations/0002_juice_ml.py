# Generated by Django 5.1.3 on 2024-11-09 14:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('denval_Juice', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='juice',
            name='ml',
            field=models.TextField(blank=True, null=True),
        ),
    ]