# Generated by Django 2.1.1 on 2018-10-04 19:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0025_auto_20181003_0119'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]
