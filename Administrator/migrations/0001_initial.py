# Generated by Django 3.2.13 on 2022-04-16 08:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='add_new_ieee',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('selectplatform', models.CharField(max_length=100)),
                ('uploadpdf', models.FileField(null=True, upload_to='images/', verbose_name='')),
                ('title', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Addnewplatform',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('platformname', models.CharField(max_length=100)),
                ('uploadthumbnail', models.FileField(blank=True, null=True, upload_to='images/')),
                ('description', models.CharField(max_length=300)),
                ('tutorial_discription', models.CharField(max_length=300)),
                ('tutorial_video', models.FileField(default='', upload_to='videos/')),
            ],
        ),
        migrations.CreateModel(
            name='Addnewproject',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('projectname', models.CharField(max_length=100)),
                ('shortdescription', models.TextField(max_length=300)),
                ('uploadthumbnail', models.ImageField(null=True, upload_to='images/', verbose_name='')),
                ('selectplatform', models.CharField(max_length=100)),
                ('languageused', models.CharField(max_length=100)),
                ('database', models.CharField(max_length=100)),
                ('softwares', models.CharField(max_length=100)),
                ('userinterface', models.CharField(max_length=100)),
                ('projectabstract', models.TextField(default='', max_length=100)),
                ('moduledetails', models.TextField(default='', max_length=100)),
                ('uploadvideo', models.FileField(default='', upload_to='videos/')),
                ('uploadscreenshots', models.ImageField(null=True, upload_to='images/', verbose_name='')),
                ('uploadscreenshots1', models.ImageField(null=True, upload_to='images/', verbose_name='')),
                ('uploadscreenshots2', models.ImageField(null=True, upload_to='images/', verbose_name='')),
                ('uploadscreenshots3', models.ImageField(null=True, upload_to='images/', verbose_name='')),
                ('uploadpdf', models.FileField(default='', null=True, upload_to='images/', verbose_name='')),
                ('price', models.CharField(blank=True, default='', max_length=10, null=True)),
            ],
            options={
                'verbose_name': 'video',
                'verbose_name_plural': 'videos',
            },
        ),
        migrations.CreateModel(
            name='applyintershipt',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('emailid', models.EmailField(max_length=100)),
                ('phonenumber', models.CharField(max_length=100)),
                ('platform', models.CharField(max_length=100)),
                ('qualifications', models.CharField(max_length=100)),
                ('location', models.CharField(max_length=100)),
                ('college', models.CharField(default='', max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Course',
            fields=[
                ('courseid', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(default='', max_length=255, null=True)),
                ('shortdescription', models.CharField(default='', max_length=1000, null=True)),
                ('description', models.FileField(default='', null=True, upload_to='files/')),
                ('modules', models.CharField(default='', max_length=1024, null=True)),
                ('level', models.CharField(default='', max_length=255, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Lecture',
            fields=[
                ('lectureid', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(default='', max_length=255, null=True)),
                ('video', models.FileField(default='', null=True, upload_to='files/')),
                ('description', models.CharField(default='', max_length=1024, null=True)),
                ('courseid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Administrator.course')),
            ],
        ),
        migrations.CreateModel(
            name='PhoneOtp',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('otp_verify', models.PositiveIntegerField(max_length=6)),
            ],
        ),
        migrations.CreateModel(
            name='Platform',
            fields=[
                ('platformid', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(default='', max_length=255, null=True)),
                ('description', models.CharField(default='', max_length=10000, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('phone', models.CharField(max_length=100)),
                ('email', models.CharField(max_length=100)),
                ('password', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Q_A',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('platform_name', models.CharField(default='', max_length=200)),
                ('q1', models.CharField(max_length=300)),
                ('a1', models.CharField(max_length=300)),
            ],
        ),
        migrations.CreateModel(
            name='QuesModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question', models.CharField(max_length=200, null=True)),
                ('op1', models.CharField(max_length=200, null=True)),
                ('op2', models.CharField(max_length=200, null=True)),
                ('op3', models.CharField(max_length=200, null=True)),
                ('op4', models.CharField(max_length=200, null=True)),
                ('ans', models.CharField(max_length=200, null=True)),
                ('platform_name', models.CharField(default='', max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='tutorial',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('platform_name', models.CharField(default='', max_length=200)),
                ('videotitle', models.CharField(max_length=300)),
                ('uploadvideo', models.FileField(default='', upload_to='videos/')),
            ],
        ),
        migrations.CreateModel(
            name='User_req_ieeeproject',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('emailid', models.EmailField(max_length=100)),
                ('phonenumber', models.CharField(max_length=100)),
                ('projectname', models.CharField(max_length=100)),
                ('Location', models.CharField(max_length=300)),
            ],
        ),
        migrations.CreateModel(
            name='User_req_inbuilt_project',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('emailid', models.EmailField(max_length=100)),
                ('phonenumber', models.CharField(max_length=100)),
                ('projectname', models.CharField(max_length=100)),
                ('Location', models.CharField(max_length=300)),
            ],
        ),
        migrations.CreateModel(
            name='Userrequestproject',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('emailid', models.EmailField(max_length=100)),
                ('phonenumber', models.CharField(max_length=100)),
                ('projectname', models.CharField(max_length=100)),
                ('projectdescription', models.CharField(max_length=300)),
                ('project_file', models.FileField(blank=True, default='', upload_to='files/')),
            ],
        ),
        migrations.CreateModel(
            name='usersign',
            fields=[
                ('sid', models.AutoField(primary_key=True, serialize=False, verbose_name='SID')),
                ('fullname', models.CharField(max_length=100)),
                ('platformid', models.CharField(max_length=100)),
                ('level', models.CharField(max_length=100)),
                ('email', models.CharField(max_length=100)),
                ('cno', models.CharField(max_length=100)),
                ('password', models.CharField(max_length=100)),
                ('score', models.FloatField(max_length=100)),
                ('course_id', models.IntegerField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Qanda',
            fields=[
                ('qandaid', models.AutoField(primary_key=True, serialize=False)),
                ('question', models.CharField(default='', max_length=255, null=True)),
                ('correct', models.CharField(default='', max_length=255, null=True)),
                ('optiona', models.CharField(default='', max_length=255, null=True)),
                ('optionb', models.CharField(default='', max_length=255, null=True)),
                ('optionc', models.CharField(default='', max_length=255, null=True)),
                ('courseid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Administrator.course')),
                ('lectureid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Administrator.lecture')),
            ],
        ),
        migrations.CreateModel(
            name='GetProject',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('phone', models.CharField(max_length=100)),
                ('email', models.CharField(max_length=100)),
                ('project_Detail', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='Administrator.addnewproject')),
            ],
        ),
        migrations.AddField(
            model_name='course',
            name='platformid',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Administrator.platform'),
        ),
    ]
