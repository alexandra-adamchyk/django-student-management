from django.contrib import admin
from django.urls import path

# Methods in the projects views and students views will in principle 
# be the same because of what they do behind the scenes in a database
# - CRUD
# It is common for developers to recyle the names of such functions
# - Let's explore some of the techniques to solve this

from students.views import new, create, student_list

# e-commerce selling dresses, shoes, etc.
# /2024-season
# /2030-season

urlpatterns = [
    path('admin/', admin.site.urls),
    path('students/new/', new, name='new-student'),
    path('students/create/', create), 
    path('students/', student_list, name='ekaterina'),
]
