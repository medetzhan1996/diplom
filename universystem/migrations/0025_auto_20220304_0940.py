# Generated by Django 3.2.7 on 2022-03-04 03:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('universystem', '0024_code'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Lab',
        ),
        migrations.RemoveField(
            model_name='code',
            name='name',
        ),
        migrations.AddField(
            model_name='code',
            name='code',
            field=models.TextField(default=1),
            preserve_default=False,
        ),
        migrations.DeleteModel(
            name='Plan',
        ),
    ]