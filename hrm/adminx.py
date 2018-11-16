# _*_ coding:utf-8 _*_
__author__='qbss'

from xadmin import views
import xadmin

from .models import Department,Staff,Attendance,EmailVerifyRecord,Salary

class GlobalSetting(object):
    site_title = '宏图科技人事信息管理系统'   #设置头标题
    site_footer = '版权所有'
    menu_style = 'accordion'

xadmin.site.register(views.CommAdminView, GlobalSetting)

class DepartmentAdmin(object):
    list_display=('name','number','manager')

xadmin.site.register(Department,DepartmentAdmin)


class StaffAdmin(object):
    list_display = ('name','department','gradSchool','tel','add_time')

    def get_readonly_fields(self):
        """  重新定义此函数，限制普通用户所能修改的字段  """
        if self.user.is_superuser:
            self.readonly_fields = []
        
        return self.readonly_fields

    readonly_fields = ('department','name','gradSchool','sex','birthday','salary_num','add_time','user')
    
    def queryset(self):
        qs = super(StaffAdmin, self).queryset()
    
        if self.request.user.is_superuser:
            return qs
        else: 
            return qs.filter(user=self.request.user)

xadmin.site.register(Staff,StaffAdmin)

class AttendanceAdmin(object):
    list_display = ('staff','user','lateCount','absenceCount','leaveCount','workOvertime')

xadmin.site.register(Attendance,AttendanceAdmin)

class SalaryAdmin(object):
    list_display = ('staff','user','salary','date','pension', 'medical', 'unemployment', 'housing', 'tax','real_wages')

xadmin.site.register(Salary,SalaryAdmin)

#class EmailVerifyRecordAdmin(object):
#    list_display = ('code', 'email')
#
#xadmin.site.register(EmailVerifyRecord,EmailVerifyRecordAdmin)


