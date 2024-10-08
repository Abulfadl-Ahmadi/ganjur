# Generated by Django 5.1.1 on 2024-10-03 14:22

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cut',
            fields=[
                ('cut_code', models.CharField(max_length=100, primary_key=True, serialize=False)),
                ('create_date', models.DateField()),
                ('model_name', models.CharField(max_length=100)),
                ('model_code', models.CharField(max_length=100)),
                ('lai_per_unit', models.PositiveSmallIntegerField()),
                ('product_per_layer', models.PositiveSmallIntegerField()),
                ('size', models.CharField(blank=True, choices=[('1', 'Free'), ('2', '2'), ('3', '3'), ('4', '4')], default='1', max_length=1, null=True, verbose_name='سایز')),
                ('length_of_layers', models.DecimalField(decimal_places=2, max_digits=3)),
                ('cutting_price', models.PositiveSmallIntegerField()),
                ('sewing_price', models.PositiveSmallIntegerField()),
                ('cutting_price_raw', models.PositiveSmallIntegerField()),
                ('sewing_price_raw', models.PositiveSmallIntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Person',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('phone_number', models.CharField(max_length=15)),
                ('person_type', models.CharField(choices=[('producer', 'Producer'), ('sewing_worker', 'Sewing House Worker'), ('cut_worker', 'Cut House Worker')], max_length=15)),
            ],
        ),
        migrations.CreateModel(
            name='CutHouseWorker',
            fields=[
                ('person', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='core.person')),
                ('payment_card_number', models.CharField(max_length=16)),
            ],
        ),
        migrations.CreateModel(
            name='Producer',
            fields=[
                ('person', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='core.person')),
                ('brand_name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='SewingHouseWorker',
            fields=[
                ('person', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='core.person')),
                ('payment_card_number', models.CharField(max_length=16)),
            ],
        ),
        migrations.CreateModel(
            name='Roll',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('color', models.CharField(max_length=50)),
                ('length', models.DecimalField(decimal_places=2, max_digits=3)),
                ('layers', models.PositiveSmallIntegerField()),
                ('products', models.PositiveSmallIntegerField()),
                ('type_fabric', models.CharField(blank=True, max_length=128, null=True, verbose_name='جنس پارچه')),
                ('cut', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='rolls', to='core.cut')),
            ],
        ),
        migrations.AddField(
            model_name='cut',
            name='owner',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.producer'),
        ),
        migrations.AddField(
            model_name='cut',
            name='sewer',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='cuts', to='core.sewinghouseworker'),
        ),
    ]
