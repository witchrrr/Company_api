# Generated by Django 4.2.6 on 2023-10-23 08:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0005_remove_company_active_employee'),
    ]

    operations = [
        migrations.RenameField(
            model_name='company',
            old_name='comapny_id',
            new_name='company_id',
        ),
        migrations.RemoveField(
            model_name='employee',
            name='added_date',
        ),
        migrations.RemoveField(
            model_name='employee',
            name='exprience',
        ),
        migrations.RemoveField(
            model_name='employee',
            name='location',
        ),
        migrations.RemoveField(
            model_name='employee',
            name='type',
        ),
        migrations.AddField(
            model_name='company',
            name='active',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='employee',
            name='about',
            field=models.TextField(default=True),
        ),
        migrations.AddField(
            model_name='employee',
            name='email',
            field=models.CharField(default=False, max_length=50),
        ),
        migrations.AddField(
            model_name='employee',
            name='phone',
            field=models.CharField(default=False, max_length=10),
        ),
        migrations.AddField(
            model_name='employee',
            name='position',
            field=models.CharField(choices=[('Manager', 'manager'), ('Software Developer', 'sd'), ('Project Leader', 'pl')], default=False, max_length=50),
        ),
        migrations.AlterField(
            model_name='company',
            name='about',
            field=models.TextField(default=True),
        ),
        migrations.AlterField(
            model_name='company',
            name='added_date',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AlterField(
            model_name='company',
            name='type',
            field=models.CharField(choices=[('IT', 'IT'), ('Non IT', 'Non IT'), ('Mobiles Phones', 'Mobile Phones')], max_length=100),
        ),
        migrations.AlterField(
            model_name='employee',
            name='name',
            field=models.CharField(max_length=100),
        ),
    ]
