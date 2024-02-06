# Generated by Django 4.2.9 on 2024-02-06 13:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('common', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='About',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('experience', models.TextField()),
                ('total_products', models.IntegerField()),
                ('salary', models.DecimalField(decimal_places=2, max_digits=2, max_length=5)),
            ],
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('author', models.CharField(max_length=255)),
                ('title', models.TextField()),
                ('description', models.TextField(blank=True, null=True)),
                ('count_views', models.PositiveBigIntegerField(default=1)),
                ('image', models.ImageField(upload_to='post/')),
            ],
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('full_name', models.CharField(max_length=255)),
                ('image', models.ImageField(upload_to='profile/')),
                ('bio', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Service',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.TextField(blank=True, null=True)),
                ('icon', models.CharField(max_length=255)),
                ('description', models.TextField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Portfolio',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('link', models.CharField(max_length=255)),
                ('completed_at', models.DateTimeField(auto_now=True)),
                ('description', models.TextField(blank=True, null=True)),
                ('image', models.ImageField(upload_to='portfolio/')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='common.category')),
                ('used_tools', models.ManyToManyField(to='common.skill')),
            ],
        ),
    ]
