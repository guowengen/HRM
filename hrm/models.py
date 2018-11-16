# _*_ coding:utf-8 _*_
from datetime import datetime
# 继承django内置user表的类AbstractUser
#from django.contrib.auth.models import AbstractUser
from django.conf import settings
from django.db import models

AUTH_USER_MODEL = getattr(settings, 'AUTH_USER_MODEL', 'auth.User')

#class UserProfile(AbstractUser):
#    pass

#    def __str__(self):
#        return self.username

class Department(models.Model):
    name=models.CharField(max_length=20,verbose_name=u"部门名称",default="")
    number=models.IntegerField(verbose_name=u"部门人数")
    manager=models.CharField(max_length=10,verbose_name=u"部门经理",default="")

    class Meta:
        verbose_name=u"部门信息管理"
        verbose_name_plural=verbose_name
        db_table="department_message"

    #def __unicode__(self):
    #    return self.name
    def __str__(self):
        return self.name


class Staff(models.Model):
    department = models.ForeignKey(Department, verbose_name="部门",null=True,blank=True)
    name=models.CharField(max_length=20,verbose_name=u"员工姓名")
    email=models.EmailField(default='11111111111@qq.com',verbose_name=u"邮箱")
    gradSchool = models.CharField(max_length=20,verbose_name=u"毕业学校")
    address=models.CharField(max_length=50,verbose_name=u"住址",default='2')
    sex=models.CharField(max_length=10,choices=(('female',u'女'),('male',u'男')),verbose_name=u"性别")
    age=models.IntegerField(verbose_name=u"年龄")
    birthday=models.DateField(verbose_name=u"生日")
    tel=models.CharField(max_length=20,verbose_name=u"手机号")
    salary_num=models.IntegerField(default=0,verbose_name=u"薪资")
    add_time = models.DateTimeField(default=datetime.now, verbose_name=u"入职时间")
    user = models.OneToOneField(AUTH_USER_MODEL,blank=True,null=True)

    class Meta:
        verbose_name=u"员工信息管理"
        verbose_name_plural = verbose_name
        db_table="staff_message"

    #def __unicode__(self):
    #    return self.name
    def __str__(self):
        return self.name

#考勤信息表
class Attendance(models.Model):
    staff = models.ForeignKey(Staff, verbose_name="员工",null=True,blank=True)
    user = models.ForeignKey(AUTH_USER_MODEL, on_delete = models.CASCADE)
    lateCount = models.IntegerField(verbose_name=u"迟到次数", default=0)
    absenceCount = models.IntegerField(verbose_name=u"旷工次数", default=0)
    leaveCount = models.IntegerField(verbose_name=u"早退次数", default=0)
    workOvertime = models.IntegerField(verbose_name=u"加班时间", default=0)
    comment = models.CharField(max_length=50, verbose_name="评论", blank=True,null=True)

    class Meta:
        verbose_name=u"员工考勤管理"
        verbose_name_plural = verbose_name
        db_table="attendance_message"

    def __unicode__(self):
        return self.name

class Salary(models.Model):
    staff = models.ForeignKey(Staff, verbose_name="员工",null=True,blank=True)
    user = models.ForeignKey(AUTH_USER_MODEL, on_delete=models.CASCADE)
    salary = models.FloatField('本月薪资', default=0)
    delWages = models.IntegerField(verbose_name=u"扣除工资", default=0)
    date = models.DateField('发放日期', blank=True, null=True)
    
    def pension(self):
        return round(self.salary * 0.08, 2)
    def medical(self):
        return round(self.salary * 0.02, 2)
    def unemployment(self):
        return round(self.salary * 0.005, 2)
    def housing(self):
        return round(self.salary * 0.07, 2)
    def tax(self):
        if self.salary >= 5000:
            return (self.salary - 5000) * 0.08
        else:
            return 0
    def real_wages(self):
        if self.salary >= 5000:
            return (self.salary - round(self.salary * 0.08, 2) - round(self.salary * 0.02, 2) - round(self.salary * 0.005, 2) - round(self.salary * 0.07, 2)  - ((self.salary - 5000) * 0.08))
        else:
            return (self.salary - round(self.salary * 0.08, 2) - round(self.salary * 0.02, 2) - round(self.salary * 0.005, 2) - round(self.salary * 0.07, 2))

    pension.short_description = '养老保险'
    medical.short_description = '医疗保险'
    unemployment.short_description = '失业保险'
    housing.short_description = '公积金'
    tax.short_description = '个税'
    real_wages.short_description = '实发工资'

    class Meta:
        verbose_name = '员工薪资管理'
        verbose_name_plural = verbose_name
        db_table="salary"

    def __unicode__(self):
        self.name

class EmailVerifyRecord(models.Model):
    code=models.CharField(max_length=20,verbose_name="验证码")
    email=models.EmailField(max_length=50,verbose_name="邮箱")
    send_type=models.CharField(choices=(("register",u"注册"),("forget",u"忘记密码")),max_length=20,verbose_name="验证码类型")
    send_time=models.DateTimeField(default=datetime.now,verbose_name="验证时间")

    class Meta:
        verbose_name=u"邮箱验证码"
        verbose_name_plural = verbose_name

    def __unicode__(self):
        return '{0}({1})'.format(self.code,self.email)
