# Generated by Django 4.2.7 on 2023-11-30 17:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('contact', '0003_category_alter_contact_picture_contact_category'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='category',
            options={'verbose_name': 'Categoria'},
        ),
    ]
