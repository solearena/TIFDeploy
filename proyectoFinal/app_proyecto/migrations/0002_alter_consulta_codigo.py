# Generated by Django 4.2.3 on 2023-07-06 23:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_proyecto', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='consulta',
            name='codigo',
            field=models.PositiveSmallIntegerField(primary_key=True, serialize=False),
        ),
    ]
