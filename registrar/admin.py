from django.contrib import admin

## Special Thanks:
## http://www.djangobook.com/en/2.0/chapter06.html
#
from registrar.models import FileUpload
from registrar.models import Course
from registrar.models import CourseSubmission
from registrar.models import CourseDiscussionPost
from registrar.models import CourseDiscussionThread
from registrar.models import CourseSetting
from registrar.models import CourseFinalMark
from registrar.models import Announcement
from registrar.models import Syllabus
from registrar.models import Policy
from registrar.models import Lecture
from registrar.models import Assignment
from registrar.models import AssignmentSubmission
from registrar.models import Exam


admin.site.register(FileUpload)
admin.site.register(Course)
admin.site.register(CourseSubmission)
admin.site.register(CourseDiscussionPost)
admin.site.register(CourseDiscussionThread)
admin.site.register(CourseSetting)
admin.site.register(CourseFinalMark)
admin.site.register(Announcement)
admin.site.register(Syllabus)
admin.site.register(Policy)
admin.site.register(Lecture)
admin.site.register(Assignment)
admin.site.register(AssignmentSubmission)
admin.site.register(Exam)
