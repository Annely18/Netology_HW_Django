# Generated by Django 4.1.7 on 2023-03-17 21:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0003_alter_tag_options'),
    ]

    operations = [
        migrations.AddField(
            model_name='tag',
            name='tag_name',
            field=models.CharField(blank=True, max_length=10, null=True, verbose_name='Раздел'),
        ),
    ]
