# Generated by Django 5.0.1 on 2024-01-10 09:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_shortcourse_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='shortcourse',
            name='discription',
            field=models.TextField(),
        ),
    ]
