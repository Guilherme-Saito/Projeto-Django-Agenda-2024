# Generated by Django 5.0.3 on 2024-03-19 14:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('contact', '0003_cadegory_contact_cadegory'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='cadegory',
            options={'verbose_name': 'Category', 'verbose_name_plural': 'Categories'},
        ),
    ]
