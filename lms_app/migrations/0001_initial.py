# Generated by Django 4.0.4 on 2022-05-27 12:40

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=225)),
            ],
            options={
                'db_table': 'category',
            },
        ),
        migrations.CreateModel(
            name='Department',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=225, null=True)),
            ],
            options={
                'db_table': 'department',
            },
        ),
        migrations.CreateModel(
            name='Leave_type',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=255, null=True)),
                ('is_active', models.BooleanField(default=True)),
            ],
            options={
                'db_table': 'leave_type',
            },
        ),
        migrations.CreateModel(
            name='Permission',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=255, null=True, unique=True)),
                ('is_active', models.BooleanField(default=True)),
            ],
            options={
                'db_table': 'permission',
            },
        ),
        migrations.CreateModel(
            name='Role',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=225, null=True)),
                ('is_active', models.BooleanField(default=True)),
                ('Permission', models.ManyToManyField(to='lms_app.permission')),
            ],
            options={
                'db_table': 'role',
            },
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('contact_no', models.CharField(max_length=50)),
                ('leave_assign', models.IntegerField(blank=True, null=True)),
                ('gender', models.CharField(choices=[('M', 'Male'), ('F', 'Female')], max_length=2)),
                ('Permission', models.ManyToManyField(to='lms_app.permission')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='lms_app.category')),
                ('departmant', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='lms_app.department')),
                ('profile_user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='profile_user', to=settings.AUTH_USER_MODEL)),
                ('reporting_manager', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('role', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='lms_app.role')),
            ],
            options={
                'db_table': 'profile',
            },
        ),
        migrations.CreateModel(
            name='LeaveBank',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('start_date', models.DateField(help_text='    leave start date is on ..', null=True)),
                ('end_date', models.DateField(help_text='   coming back on ...', null=True)),
                ('reason', models.CharField(blank=True, help_text='add additional information for leave', max_length=255, null=True)),
                ('status', models.CharField(default='pending', max_length=12)),
                ('is_approved', models.BooleanField(default=False)),
                ('leavetype', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='lms_app.leave_type')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
