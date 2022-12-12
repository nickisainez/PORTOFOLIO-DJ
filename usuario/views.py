from django.shortcuts import render, redirect, get_object_or_404
from .models import Project
from .forms import ProjectForm, NewUserForm
from django.views.generic import CreateView
from django.contrib.auth.decorators import login_required
from django.core.mail import EmailMessage

def viewProjects(request):
    projects = Project.objects.all()
    return render(request, 'home.html', {'projects' : projects})

def detailsProjects(request, project_id):
    projecto = get_object_or_404(Project, pk=project_id)
    return render(request, 'projects_detail.html', {'project':projecto})


@login_required   
def createProject(request):
    if request.method == 'POST':
        form = ProjectForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            img_obj = form.instance
            return redirect('home')
    else:
        form = ProjectForm()
    return render(request, 'vers.html', {'form': form})

class RegisterView(CreateView):
    template_name = "registration/register.html"
    form_class = NewUserForm

    def form_valid(self,form):
        form.save()
        return redirect('crear')

def aboutMe(request):
    return render(request,"about.html")

def contact(request):
    return render(request,"contact.html")
            


