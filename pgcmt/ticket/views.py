# Create your views here.
from django.shortcuts import render_to_response, render,HttpResponseRedirect, HttpResponse
from ticket.models import Ticket,Project,RequestUser
from ticket.forms import CreateProjectForm, CreateTicketForm, SearchTicketForm, CreateRequestUser
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.utils import timesince
from django.template.defaultfilters import slugify as slugify_original

def slugify(value):
    value = value.replace(u'\u0131', 'i')
    return slugify_original(value)

from django.utils import simplejson

def home(request):
    tickets = Ticket.objects.all().order_by("-id")
    search_form = SearchTicketForm()
    return render_to_response("ticket/index.html",{'tickets':tickets,'search_form':search_form,'title':'All Tickets','user':request.user,'fullView':False})

@login_required
def createProject(request):
    form = CreateProjectForm()
    if request.method == 'POST':
        form = CreateProjectForm(request.POST)
        if form.is_valid():
            project = Project()
            project.name = form.cleaned_data["name"]
            project.save()
            tickets = Ticket.objects.all()
            return HttpResponseRedirect("/projects/")
        else:
            return render(request,"ticket/create_project.html",{'form':form,'title':'Create Project','user':request.user})
    else:
        return render(request,"ticket/create_project.html",{'form':form,'title':'Create Project','user':request.user})

def createProjectAjax(request):
    if request.is_ajax():
        form = CreateProjectForm(request.POST)
        if form.is_valid():
            project = Project()
            project.name = form.cleaned_data["name"]
            project.save()
            tickets = Ticket.objects.all()
            response = 1
            return HttpResponse(response)
        else:
            response = -1
            #return HttpResponse("Form is invalid.")
            return HttpResponse(response)

@login_required
def createTicket(request):
    form = CreateTicketForm()
    if request.method == 'POST':
        form = CreateTicketForm(request.POST)
        if form.is_valid():
            ticket = Ticket()
            ticket.user = User.objects.get(username=request.user)
            ticket.project = Project.objects.get(name=form.cleaned_data["project_id"])
            ticket.content = form.cleaned_data["content"]
            ticket.requested_by = RequestUser.objects.get(username=form.cleaned_data["requested_by_id"])
            ticket.save()
            return HttpResponseRedirect("/")
        else:
            return render(request,"ticket/create_ticket.html",{'form':form,'title':'Create Ticket','user':request.user})    
    else:
        return render(request,"ticket/create_ticket.html",{'form':form,'title':'Create Ticket','user':request.user})

@login_required
def createRequestUser(request):
    form = CreateRequestUser(request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            requestUser = RequestUser()
            requestUser.username = form.cleaned_data["name"]
            requestUser.save()
            return HttpResponseRedirect("/")
        else:
            pass
    else:
            pass
    return render(request,"ticket/create_requestuser.html",{'form':form,'username':request.user,'title':'Create Responsible'})

def listProjects(request):
    projects = Project.objects.all().order_by("name")
    return render_to_response("ticket/show_projects.html",{'projects':projects,'title':'Project List','user':request.user})

def showProject(request,project_name):
    project = Project.objects.get(name=project_name)
    tickets = Ticket.objects.filter(project=project).order_by("-id")
    search_form = SearchTicketForm(initial={'project_id':project})
    return render_to_response("ticket/index.html",{'tickets':tickets,'search_form':search_form,'title':project_name+" Project",'user':request.user})

def searchTicket(request):
    if len(request.GET["project_id"]) > 0:
        tickets = Ticket.objects.filter(content__icontains=request.GET["query"],project=request.GET["project_id"]).order_by("-id")
        project = Project.objects.get(id=request.GET["project_id"]).__str__()
    else:
        tickets = Ticket.objects.filter(content__icontains=request.GET["query"]).order_by("-id")
        project = "all"
    search_form = SearchTicketForm(request.GET)
    return render_to_response("ticket/index.html",{'tickets':tickets,'search_form':search_form,'title':'Search for ' + request.GET["query"] + ' in ' + project,'user':request.user })


def showUser(request,username):
    tickets = Ticket.objects.filter(user=User.objects.filter(username=username)).order_by("-id")
    return render_to_response("ticket/index.html",{'tickets':tickets,'title':'Tickets done by ' + username,'user':request.user })

def showRequestUser(request,requestuser_id):
    requestUser = RequestUser.objects.get(id=requestuser_id)
    tickets = Ticket.objects.filter(requested_by=requestuser_id).order_by("-id")
    return render_to_response("ticket/index.html",{'tickets':tickets,'title':'Tickets requested by ' + requestUser.username,'user':request.user })

def showTicket(request,ticketId):
    ticket = Ticket.objects.filter(id=ticketId)

    return render_to_response("ticket/index.html",{'tickets':ticket,'title':'Ticket ','fullView':True})



