# Create your views here.
from django.shortcuts import render_to_response, render
from pgcmt.ticket.models import Ticket,Project
from pgcmt.ticket.forms import CreateProjectForm, CreateTicketForm
from django.contrib.auth.models import User

def home(request):
    tickets = Ticket.objects.all()
    return render_to_response("ticket/index.html",{'tickets':tickets})

def createProject(request):
    form = CreateProjectForm()
    if request.method == 'POST':
        form = CreateProjectForm(request.POST)
        if form.is_valid():
            project = Project()
            project.name = form.cleaned_data["name"]
            project.save()
            tickets = Ticket.objects.all()
            return render_to_response("ticket/index.html",{'tickets':tickets})
    else:
        return render(request,"ticket/create_project.html",{'form':form})
def createTicket(request):
    form = CreateTicketForm()
    if request.method == 'POST':
        form = CreateTicketForm(request.POST)
        if form.is_valid():
            ticket = Ticket()
            ticket.user_id = User.objects.get(id=1)
            ticket.project_id = Project.objects.get(name=form.cleaned_data["project_id"])
            ticket.content = form.cleaned_data["content"]
            ticket.save()
            tickets = Ticket.objects.all()
            return render_to_response("ticket/index.html",{'tickets':tickets})
    else:
        return render(request,"ticket/create_ticket.html",{'form':form})

def listProjects(request):
    projects = Project.objects.all()
    return render_to_response("ticket/show_projects.html",{'projects':projects})

def showProject(request,project_name):
    tickets = Ticket.objects.filter(project_id=(Project.objects.filter(name=project_name)))
    return render_to_response("ticket/index.html",{'tickets':tickets})
