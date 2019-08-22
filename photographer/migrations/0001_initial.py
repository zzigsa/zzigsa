# Generated by Django 2.1.7 on 2019-08-22 19:03

from django.db import migrations, models
import django.db.models.deletion
import imagekit.models.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('first', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ProductRegistration',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('summary', models.CharField(max_length=400)),
                ('image', imagekit.models.fields.ProcessedImageField(upload_to='images/product')),
                ('detail', models.TextField()),
                ('options', models.CharField(max_length=400)),
                ('option_price', models.IntegerField()),
                ('writerid', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='first.Writer')),
            ],
        ),
        migrations.CreateModel(
            name='Reply',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('writer', models.CharField(max_length=20)),
                ('content', models.CharField(max_length=400)),
                ('rating', models.IntegerField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('productid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='photographer.ProductRegistration')),
            ],
        ),
    ]
