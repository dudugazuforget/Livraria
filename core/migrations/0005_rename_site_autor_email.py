# Generated by Django 5.0.2 on 2024-03-19 11:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("core", "0004_autor"),
    ]

    operations = [
        migrations.RenameField(
            model_name="autor",
            old_name="site",
            new_name="email",
        ),
    ]
