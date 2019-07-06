from django.shortcuts import render
from django.http import JsonResponse,HttpResponse
from APP01 import models
import requests,json


# Create your views here.
# 登录函数
def login(request):
    responses = []
    response={}
    if request.method == "GET":
        return render(request, 'login.html')
    elif request.method == "POST":
        u = request.POST.get('username')
        p = request.POST.get('password')
        i = request.POST.get('identify')
        print(u, p, i)
        obj = models.Accounts.objects.filter(user_id=u, user_password=p, identity=i).first()        # 数据库验证
        if obj:
            request.session['user_id'] = obj.user_id
            request.session['identify'] = "root"
            response['msg'] = 'success'
            responses.append(response)
            return render(request, 'index(1).html')
        else:
            print(obj)
            response['msg'] = "fail"
            responses.append(response)
            return JsonResponse(data=responses, safe=False)


# 学生查询课程信息
def show_course_information(request):
    responses = []
    response = {}
    if request.method == "GET":
        sno = request.GET.get('sno')   # 获取学号
        stu = models.StudentInformation.objects.filter(sno=sno).first()
        if stu:     # 如果有该学生
            cno = models.StudentSubject.objects.filter(student_id=stu.sno).all()    # 课程号列表
            for item in cno:        # 通过cno把课程信息装进列表
                print(item.subject_id)
                response['subject_id'] = item.subject_id.subject_id
                response['subject_name'] = item.subject_id.subject_name
                response['start_time'] = item.subject_id.start_time
                response['end_time'] = item.subject_id.end_time
                response['classroom_id'] = item.subject_id.classroom_id.classroom_name
                responses.append(response)
    return JsonResponse(data=responses, safe=False)


# 学生查成绩
def show_myscore(request):
    responses = []
    response = {}
    if request.method == "GET":
        sno = request.GET.get('sno')
        scores = models.StudentSubject.objects.filter(student_id=sno).all()
        for score in scores:
            response['student_id'] = score.student_id.sno
            response['student_name'] = score.student_id.sname
            response['course_name'] = score.subject_id.subject_name
            response['score'] = score.score
            response['times'] = score.times
            responses.append(response)
    return JsonResponse(data=responses, safe=False)


# 学生进行课程设计选择
def select_mydesign(request):
    responses = []
    response = {}
    if request.method == "GET":
        sno = request.GET.get('sno')
        student = models.StudentInformation.objects.filter(sno=sno).first()
        designs = models.CurriculumInformation.objects.filter(major_id=student.major_id)
        if designs:
            for item in designs:
                response['curriculum_id'] = item.curriculum_id
                response['curriculum_name'] = item.curriculum_name
                response['curriculum_content'] = item.curriculum_content
                response['last_number'] = item.last_number
                response['major_name'] = item.major_id.major_name
                response['employee_name'] = item.employee_id.ename
                responses.append(response)
        else:
            response['msg'] = "没有可选课程"
        return JsonResponse(data=response, safe=False)
    elif request == "POST":
        sno = request.GET.get('sno')
        curriculum_id = request.GET.get('curriculum_id')
        try:
            models.StudentInformation.objects.filter(sno=sno).update(curriculum_id=curriculum_id)
            last_number = models.CurriculumInformation.objects.filter(curriculum_id=curriculum_id).first()\
                .last_number
            models.CurriculumInformation.objects.filter(curriculum_id=curriculum_id).update(last_number=
                                                                                            last_number-1)
            return JsonResponse(data="success", safe=False)
        except Exception as e:
            return JsonResponse(data="fail", safe=False)


# 显示所有的课程设计情况
def show_alldesigns(request):
    responses = []
    response = {}
    if request.method == "GET":
        desgins = models.CurriculumInformation.objects.filter().all()
        for item in desgins:
            response['curriculum_id'] = item.curriculum_id
            response['curriculum_name'] = item.curriculum_name
            response['curriculum_content'] = item.curriculum_content
            response['major_name'] = item.major_id.major_name
            response['employee_name'] = item.employee_id.ename
            responses.append(response)
    return JsonResponse(data=responses, safe=False)


# 学生查看自己选择的课程设计
def show_mydesign(request):
    response = {}
    if request.method == "GET":
        sno = request.GET.get('sno')
        student = models.StudentInformation.objects.filter(sno=sno).first()
        # print(student.curriculum_id.curriculum_name)
        design = models.CurriculumInformation.objects.filter(curriculum_id=student.curriculum_id.curriculum_id).first()
        print(design)
        if design:
            response['curriculum_id'] = design.curriculum_id
            response['curriculum_name'] = design.curriculum_name
            response['curriculum_content'] = design.curriculum_content
            response['major_name'] = design.major_id.major_name
            response['employee_name'] = design.employee_id.ename
            response['score'] = student.curriculum_grade
            print(response)
    return JsonResponse(data=response, safe=False)


# 课程合作人查看自己教授的课程
def show_class(request):
    response = {}
    if request.method == "GET":
        e_id = request.GET.get('employee_id')
        course = models.EmployeeInformation.objects.filter(employee_id=e_id).first()
        c_info = course.subject_id
        response['subject_id'] = c_info.subject_id
        response['subject_name'] = c_info.subject_name
        response['start_time'] = c_info.start_time
        response['end_time'] = c_info.end_time
        response['classroom'] = c_info.classroom_id.classroom_name
    return JsonResponse(data=response, safe=False)


# 课程合作人给学生打分(课程)
def mark_course_score(request):
    responses = []
    response = {}
    if request.method == "GET":
        e_id = request.GET.get('employee_id')
        cno = models.EmployeeInformation.objects.filter(employee_id=e_id).first().subject_id
        records = models.StudentSubject.objects.filter(subject_id=cno).all()
        for record in records:
            response['student_id'] = record.student_id.sno
            response['student_name'] = record.student_id.sname
            response['subject_name'] = record.subject_id.subject_name
            response['times'] = record.times
            response['score'] = record.score
            responses.append(response)
        return JsonResponse(data=responses, safe=False)
    elif request.method == "POST":
        sno = request.POST.get('sno')
        cno = request.POST.get('cno')
        score = request.POST.get('score')
        record = models.StudentSubject.objects.filter(student_id=sno, subject_id=cno).first()
        if record.times > 0:    # 有补考机会
            record.update(score=score, times=record.times-1)
            return JsonResponse(data="success", safe=False)
        else:       # 3次机会已用光，不可重新考试
            return JsonResponse(data="fail", safe=False)


# 课程合作人查看学生成绩
def show_score(request):
    responses = []
    response = {}
    if request.method == "GET":
        e_id = request.GET.get('employee_id')
        subject = models.EmployeeInformation.objects.filter(employee_id=e_id).first().subject_id
        records = models.StudentSubject.objects.filter(subject_id=subject).all()
        for record in records:
            response['student_id'] = record.student_id.sno
            response['student_name'] = record.student_id.sname
            response['subject_name'] = record.subject_id.subject_name
            response['times'] = record.times
            response['score'] = record.score
            responses.append(response)
    return JsonResponse(data=responses, safe=False)


# 显示自己指导的学生信息
def show_mystudent(request):
    if request.method == 'GET':
        # 获取教师id
        teacher_id = request.GET.get('user_id')
        responses = []
        response = {}
        # 找到指导老师所管理的学生
        students = models.StudentInformation.objects.filter(teacher_id=teacher_id)
        for student in students:
            major_id = student.major_id
            major_name = models.MajorInformation.objects.get(major_id=major_id).major_name
            response['major_name'] = major_name
            response['sno'] = student.sno
            response['sname'] = student.sname
            response['ssex'] = student.ssex
            response['admission'] = student.admission
            response['birthdate'] = student.birthdate
            responses.append(response)
        return JsonResponse(data=responses, safe=False)


# 课程合作人上传自己的课设项目
def upload_design(request):
    if request.method == 'POST':
        curriculum_id = request.POST.get('curriculum_id')
        curriculum_name = request.POST.get('curriculum_name')
        curriculum_content = request.POST.get('curriculum_content')
        major_id = request.POST.get('major_id')
        employee_id = request.POST.get('user_id')
        models.CurriculumInformation.objects.create(curriculum_id=curriculum_id, curriculum_name=curriculum_name,
                                                    curriculum_content=curriculum_content, major_id=major_id,
                                                    employee_id=employee_id)
        response_dict = {
            'status': True
        }
        return JsonResponse(date=response_dict, safe=False)


# 显示自己的课设的选课情况
def show_mydesign(request):
    if request.method == 'GET':
        employee_id = request.GET.get('user_id')
        curriculums = models.CurriculumInformation.objects.filter(employee_id=employee_id)
        responses = []
        response = {}
        for curriculum in curriculums:
            response['curriculum_id'] = curriculum.curriculum_id
            response['curriculum_name'] = curriculum.curriculum_name
            response['curriculum_content'] = curriculum.curriculum_content
            response['last_number'] = curriculum.last_number
            responses.append(response)
        return JsonResponse(data=responses, safe=False)


# 查看选择自己课设的学生的信息
def mydesign_student(request):
    if request.method == 'GET':
        curriculum_id = request.GET.get('curriculum_id')
        students = models.StudentInformation.objects.filter(curriculum_id=curriculum_id)
        responses = []
        response = {}
        for student in students:
            major_id = student.major_id
            major_name = models.MajorInformation.objects.get(major_id=major_id).major_name
            response['major_name'] = major_name
            response['sno'] = student.sno
            response['sname'] = student.sname
            response['ssex'] = student.ssex
            response['admission'] = student.admission
            response['birthdate'] = student.birthdate
            responses.append(response)
        return JsonResponse(data=responses, safe=False)


# 课程合作人查看学生成绩
def show_score(request):
    responses = []
    response = {}
    if request.method == "GET":
        e_id = request.GET.get('employee_id')
        subject = models.EmployeeInformation.objects.filter(employee_id=e_id).first().subject_id
        records = models.StudentSubject.objects.filter(subject_id=subject).all()
        for record in records:
            response['student_id'] = record.student_id.sno
            response['student_name'] = record.student_id.sname
            response['subject_name'] = record.subject_id.subject_name
            response['times'] = record.times
            response['score'] = record.score
            responses.append(response)
    return JsonResponse(data=responses, safe=False)


# 显示课设成绩
def show_design_score(request):
    if request.method == 'GET':
        curriculum_id = request.GET.get('curriculum_id')
        students = models.StudentInformation.objects.filter(curriculum_id=curriculum_id)
        responses = []
        response = {}
        for student in students:
            curriculum_name = models.CurriculumInformation.objects.get(curriculum_id=curriculum_id).curriculum_name
            response['curriculum_name'] = curriculum_name
            response['sno'] = student.sno
            response['sname'] = student.sname
            response['curriculum_grade'] = student.curriculum_grade
            responses.append(response)
        return JsonResponse(data=responses, safe=False)


# 给课设成绩打分
def mark_design_score(request):
    if request.method == 'POST':
        curriculum_id = request.POST.get('curriculum_id')
        sno = request.POST.get('sno')
        curriculum_grade = request.GET.get('curriculum_grade')
        models.StudentInformation.objects.create(curriculum_id=curriculum_id, curriculum_grade=curriculum_grade, sno=sno)
        response_dict = {
            'status': True
        }
        return JsonResponse(date=response_dict, safe=False)
