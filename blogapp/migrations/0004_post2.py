# Generated by Django 3.2.11 on 2022-01-22 08:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blogapp', '0003_rename_imgs_post_image'),
    ]

    operations = [
        migrations.CreateModel(
            name='Post2',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title2', models.CharField(max_length=200)),
                ('image2', models.ImageField(blank=b'I01\n', upload_to='appImage')),
                ('body2', models.TextField()),
            ],
        ),
    ]