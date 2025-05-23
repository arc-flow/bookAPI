# Generated by Django 5.0.6 on 2024-10-01 15:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='books',
            name='author',
            field=models.CharField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='books',
            name='category',
            field=models.CharField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='books',
            name='image',
            field=models.CharField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='books',
            name='publisher',
            field=models.CharField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='books',
            name='rating',
            field=models.CharField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='books',
            name='title',
            field=models.CharField(blank=True, null=True),
        ),
    ]
