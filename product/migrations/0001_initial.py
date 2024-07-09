# Generated by Django 4.2.13 on 2024-06-09 18:27

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('description', models.TextField(blank=True, max_length=200)),
                ('image', models.ImageField(null=True, upload_to='product/%Y/%m/%d/')),
            ],
        ),
    ]
