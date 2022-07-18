# Generated by Django 4.0.5 on 2022-07-17 22:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0002_alter_member_phone'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='member',
            options={'ordering': ['updated', 'created']},
        ),
        migrations.AlterField(
            model_name='member',
            name='role',
            field=models.CharField(choices=[(1, "Regular - Can't delete members"), (2, 'Admin - Can delete members')], default=1, max_length=2),
        ),
    ]