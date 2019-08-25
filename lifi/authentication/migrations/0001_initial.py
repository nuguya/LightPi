# Generated by Django 2.2.4 on 2019-08-25 14:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='UserInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('login_id', models.CharField(default=None, max_length=100)),
                ('login_pw', models.CharField(default=None, max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='ModelInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('model_code', models.CharField(default=None, max_length=100)),
                ('model_name', models.CharField(default=None, max_length=100)),
                ('key_value', models.CharField(default=None, max_length=100)),
                ('master_user_info_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='authentication.UserInfo')),
            ],
        ),
        migrations.CreateModel(
            name='ConnectInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('connect_flag', models.IntegerField(default=0)),
                ('model_info_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='authentication.ModelInfo')),
                ('user_info_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='authentication.UserInfo')),
            ],
        ),
    ]