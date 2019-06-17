# Generated by Django 2.2.2 on 2019-06-17 10:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('newsapp', '0002_auto_20190611_1708'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='newssubcategory',
            name='root',
        ),
        migrations.AlterField(
            model_name='news',
            name='main_category',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='newsapp.NewsCategory'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='news',
            name='video_link',
            field=models.URLField(blank=True, max_length=500, null=True),
        ),
    ]
