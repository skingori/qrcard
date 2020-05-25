# Generated by Django 3.0.6 on 2020-05-25 12:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('qrcardapp', '0002_auto_20200525_1220'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='childrendetails',
            options={'ordering': ['service_number'], 'verbose_name': 'Children Details', 'verbose_name_plural': 'Children Details'},
        ),
        migrations.AlterModelOptions(
            name='employmentdetails',
            options={'ordering': ['service_number'], 'verbose_name': 'Employment Details', 'verbose_name_plural': 'Employment Details'},
        ),
        migrations.AlterModelOptions(
            name='instructionalcourses',
            options={'ordering': ['service_number'], 'verbose_name': 'Instructional Courses', 'verbose_name_plural': 'Instructional Courses'},
        ),
        migrations.AlterModelOptions(
            name='leavedetails',
            options={'ordering': ['service_number'], 'verbose_name': 'Leave Details', 'verbose_name_plural': 'Leave Details'},
        ),
        migrations.AlterModelOptions(
            name='regimentaentries',
            options={'ordering': ['service_number'], 'verbose_name': 'Regimenta Entries', 'verbose_name_plural': 'Regimenta Entries'},
        ),
        migrations.AlterModelOptions(
            name='servicerecords',
            options={'ordering': ['service_number'], 'verbose_name': 'Service Records', 'verbose_name_plural': 'Service Records'},
        ),
        migrations.AlterModelOptions(
            name='wifedetails',
            options={'ordering': ['service_number'], 'verbose_name': 'Wife Details', 'verbose_name_plural': 'Wife Details'},
        ),
    ]
