# Generated by Django 4.1.7 on 2023-03-17 21:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0002_tag_scope'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='tag',
            options={'verbose_name': 'Тэг', 'verbose_name_plural': 'Тэги'},
        ),
    ]
