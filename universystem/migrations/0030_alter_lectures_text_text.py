# Generated by Django 3.2.7 on 2022-03-04 05:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('universystem', '0029_rename_code_lectures_text_lectures_cod'),
    ]

    operations = [
        migrations.AlterField(
            model_name='lectures_text',
            name='text',
            field=models.TextField(blank=True, null=True),
        ),
    ]