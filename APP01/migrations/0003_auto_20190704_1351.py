# Generated by Django 2.2.3 on 2019-07-04 05:51

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('APP01', '0002_auto_20190704_0958'),
    ]

    operations = [
        migrations.AlterField(
            model_name='curriculuminformation',
            name='employee_id',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='APP01.EmployeeInformation', verbose_name='员工号'),
        ),
        migrations.AlterField(
            model_name='curriculuminformation',
            name='major_id',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='APP01.MajorInformation', verbose_name='专业号'),
        ),
        migrations.AlterField(
            model_name='departmentinformation',
            name='principal',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='APP01.EmployeeInformation', verbose_name='负责人'),
        ),
        migrations.AlterField(
            model_name='employeeinformation',
            name='department_id',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='APP01.DepartmentInformation', verbose_name='所属部门号'),
        ),
        migrations.AlterField(
            model_name='employeeinformation',
            name='subject_id',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='APP01.SubjectInformation', verbose_name='本学期所授课程号'),
        ),
        migrations.AlterField(
            model_name='majorsubject',
            name='major_id',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='APP01.MajorInformation', verbose_name='专业号'),
        ),
        migrations.AlterField(
            model_name='majorsubject',
            name='subject_id',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='APP01.SubjectInformation', verbose_name='课程号'),
        ),
        migrations.AlterField(
            model_name='studentinformation',
            name='curriculum_id',
            field=models.ForeignKey(default='', null=True, on_delete=django.db.models.deletion.CASCADE, to='APP01.CurriculumInformation', to_field='curriculum_id', verbose_name='课程设计编号'),
        ),
        migrations.AlterField(
            model_name='studentinformation',
            name='major_id',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='APP01.MajorInformation', verbose_name='专业号'),
        ),
        migrations.AlterField(
            model_name='studentinformation',
            name='teacher_id',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='APP01.TeacherInformation', verbose_name='指导教师编号'),
        ),
        migrations.AlterField(
            model_name='studentsubject',
            name='student_id',
            field=models.ForeignKey(null=True, on_delete=models.Model, to='APP01.StudentInformation', verbose_name='学生号'),
        ),
        migrations.AlterField(
            model_name='studentsubject',
            name='subject_id',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='APP01.SubjectInformation', verbose_name='课程号'),
        ),
        migrations.AlterField(
            model_name='subjectinformation',
            name='classroom_id',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='APP01.ClassroomInformation', verbose_name='教室号'),
        ),
    ]