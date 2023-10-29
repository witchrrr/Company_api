# Generated by Django 4.2.6 on 2023-10-23 04:26

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0004_remove_company_city'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='company',
            name='active',
        ),
        migrations.CreateModel(
            name='employee',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('exprience', models.IntegerField()),
                ('location', models.CharField(max_length=40)),
                ('type', models.CharField(choices=[('software engineer', 'se'), ('manager', 'mgr'), ('intern', 'intern'), ('Developer', 'dev')], max_length=50)),
                ('added_date', models.DateField(auto_now=True)),
                ('company', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.company')),
            ],
        ),
    ]
