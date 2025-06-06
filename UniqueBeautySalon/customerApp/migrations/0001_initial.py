# Generated by Django 5.2 on 2025-04-06 14:56

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Service',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('category', models.CharField(choices=[('Hair Care', 'Hair Care'), ('Skin Care', 'Skin Care'), ('Makeup', 'Makeup'), ('Nail Care', 'Nail Care'), ('Spa', 'Spa & Massage')], max_length=50)),
                ('description', models.TextField()),
                ('price', models.DecimalField(decimal_places=2, max_digits=6)),
                ('duration', models.CharField(max_length=50)),
                ('image', models.ImageField(blank=True, null=True, upload_to='services/')),
            ],
        ),
    ]
