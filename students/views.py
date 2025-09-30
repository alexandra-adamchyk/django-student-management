from django.shortcuts import render, redirect
from django.http import HttpResponse
from students.models import Student
# Create your views here together with the teacher during code along.
# - index (show all entities in the database)
# - detail (show details of a single entity)
# - edit (load form to edit)
# - delete 
# - new (creating a new entity/resource)

# Create a new student
def new(request):
    return render(request, 'students/new.html')

# Error driven development

def create(request):
    if request.method == 'POST':
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        nickname = request.POST.get('nickname')

        # create a student 
        student = Student.objects.create(first_name=first_name, last_name=last_name, nickname=nickname)
        return redirect('/students/')
    else:
        return HttpResponse("This method is not supported!")
    

def student_list(request):
    return render(request, 'students/index.html', {'students': Student.objects.all()})    