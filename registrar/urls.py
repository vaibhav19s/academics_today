from django.conf.urls import *

from registrar.views import courses
from registrar.views import enrollment
from registrar.views import teaching
from registrar.views import transcript
from registrar.views import certificate

urlpatterns = (
    # Courses
    url(r'^courses$', courses.courses_page),
    url(r'^enroll$', courses.enroll),

    # Enrollment(s)
    url(r'^enrollment$', enrollment.enrollment_page),
    url(r'^enrollment_table$', enrollment.enrollment_table),
    url(r'^disenroll_modal$', enrollment.disenroll_modal),
    url(r'^disenroll', enrollment.disenroll),
         
    # Teaching
    url(r'^teaching$', teaching.teaching_page),
    url(r'^refresh_teaching_table$', teaching.refresh_teaching_table),
                       
    url(r'^course_modal$', teaching.course_modal),
    url(r'^save_course$', teaching.save_course),
    url(r'^delete_course_modal$', teaching.delete_course_modal),
    url(r'^course_delete$', teaching.course_delete),
                    

)
