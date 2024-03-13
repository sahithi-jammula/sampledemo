from django.shortcuts import render

from .models import Student


# Create your views here.
def home(request):
   return render(request,'home.html')
def addStudent(request):
    if request.method == 'POST':
        sname = request.POST['sname']
        course = request.POST['course']
        fees=request.POST['fees']
        request.POST['fees']
        st = Student(sname=sname, course= course, fees=fees)
        st.save()
        return render(request, 'addStudent.html', {'saved': True})
    return render(request, 'addStudent.html')


