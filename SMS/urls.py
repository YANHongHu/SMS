"""SMS URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.conf.urls import url
from APP01 import views

urlpatterns = [
    # 学生功能
    path('admin/', admin.site.urls),
    url(r'^login/', views.login),  # 登录界面 判断身份
    url(r'^show_course_information/', views.show_course_information),  # 学生查询课程信息(授课老师、时间等)
    url(r'^show_myscore/', views.show_myscore),  # 学生查询成绩
    url(r'^select_mydesign/', views.select_mydesign),  # 学生进行课程设计选择
    url(r'^show_alldesigns/', views.show_alldesigns),  # 显示所有的课程设计情况
    url(r'^show_mydesign/', views.show_mydesign),  # 学生查看自己选择的课程设计
    # 课程设计人功能
    url(r'^show_clss/', views.show_class),  # 课程合作人查看自己教授的课程
    url(r'^mark_course_score/', views.mark_course_score),  # 课程合作人给学生打分(课程)
    url(r'^show_score/', views.show_score),  # 课程合作人查看学生成绩
    # path('change_member/', views.change_member),  # 部门负责人修改部门成员
    # path('show_department/', views.change_department),  # 成员查看部门情况
    url(r'^upload_design/', views.upload_design),  # 课程合作人上传自己的课设项目
    url(r'^show_mydesigin/', views.show_mydesign),  # 显示自己的课设的选课情况
    url(r'^mydesign_student/', views.mydesign_student),  # 查看选择自己课设的学生的信息
    url(r'^show_design_score/', views.show_design_score),  # 显示课设成绩
    url(r'^mark_design_score/', views.mark_design_score),  # 给课设成绩打分
    # 指导老师功能
    url(r'^show_mystudent/', views.show_mystudent),  # 显示自己指导的学生信息
    # # 管理员功能
    # path('register/', views.register),  # 账户注册功能
    # path('change/', views.change),  # 信息编辑
    # path('show_student/', views.show_students),  # 学生信息显示
    # path('show_teacher/', views.show_teacher),  # 指导老师信息显示
    # path('show_employee/', views.show_employee),  # 课程合作人信息显示
    # path('show_employee/', views.show_employee),  # 课程合作人信息显示
]
