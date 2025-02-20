# Generated by Django 4.2.16 on 2024-11-15 23:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_documentupload_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='documentupload',
            name='land_area',
            field=models.DecimalField(decimal_places=2, default=1, max_digits=10),
            preserve_default=False,
        ),
    ]
