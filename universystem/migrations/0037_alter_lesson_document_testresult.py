# Generated by Django 4.0 on 2024-04-19 05:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
        ('universystem', '0036_lesson_comment'),
    ]

    operations = [
        migrations.AlterField(
            model_name='lesson',
            name='document',
            field=models.FileField(blank=True, null=True, upload_to='pdf/document'),
        ),
        migrations.CreateModel(
            name='TestResult',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('score', models.IntegerField()),
                ('total', models.IntegerField()),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='auth.user')),
            ],
        ),
    ]
