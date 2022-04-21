# Generated by Django 3.2.5 on 2022-04-21 14:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0002_customer_user'),
    ]

    operations = [
        migrations.CreateModel(
            name='Item',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('unit', models.CharField(choices=[{'ea', 'each'}, {'kg', 'kilogram'}, {'g', 'gram'}], default='ea', max_length=15)),
                ('unit_price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('image', models.ImageField(upload_to='myimages')),
                ('description', models.CharField(blank=True, max_length=100, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='OrderItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.IntegerField(default=0)),
                ('customer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myapp.customer')),
                ('item', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myapp.item')),
            ],
        ),
        migrations.CreateModel(
            name='Invoice',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('customer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myapp.customer')),
                ('order_item', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myapp.orderitem')),
            ],
        ),
    ]
