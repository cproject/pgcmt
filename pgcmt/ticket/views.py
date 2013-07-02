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
    return render_to_response("ticket/index.html",{'tickets':tickets,'search_form':search_form,'title':'All Tickets','user':request.user,'fullView':False,'projects':getProjectList()})


@login_required
def createProject(request):
    form = CreateProjectForm(request.POST or None)
    if request.method == 'GET':
        return render(request,"ticket/create_project.html",{'form':form,'title':'Create Project','user':request.user,'projects':getProjectList()})
    elif request.method == 'POST':
        if form.is_valid():
            form.save()
            if request.is_ajax():
                response = {'result':'true','message':'Project created.'}
                return HttpResponse(simplejson.dumps(response),mimetype="application/json");
            return HttpResponseRedirect("/projects/")
        else:
            if request.is_ajax():
                response = {'result':'false','message':'Form is invalid.'}
                return HttpResponse(simplejson.dumps(response),mimetype="application/json");
            return render(request,"ticket/create_project.html",{'form':form,'title':'Create Project','user':request.user,'projects':getProjectList()})

@login_required
def createTicket(request):
    form = CreateTicketForm(request.POST or None)
    if request.method == 'GET':
        return render(request,"ticket/create_ticket.html",{'form':form,'title':'Create Ticket','user':request.user, 'projects':getProjectList()})
    elif request.method == 'POST':
        if form.is_valid():
            ticket = form.save(commit=False)
            ticket.user = request.user
            ticket.save();
            print ticket.project
            if request.is_ajax():
                response = {'result':'true','message':'Project created.','data':{'project':ticket.project.__str__(),'content':ticket.content.__str__()}}
                return HttpResponse(simplejson.dumps(response),mimetype="application/json");
            return HttpResponseRedirect("/")
        else:
            if request.is_ajax():
                response = {'result':'false','message':'Form is invalid.'}
                return HttpResponse(simplejson.dumps(response),mimetype="application/json");
            return render(request,"ticket/create_ticket.html",{'form':form,'title':'Create Ticket','user':request.user,'projects':getProjectList()})    
    

@login_required
def createRequestUser(request):
    form = CreateRequestUser(request.POST or None)
    if request.method == 'GET':
        return render(request,"ticket/create_requestuser.html",{'form':form,'username':request.user,'title':'Create Responsible','projects':getProjectList()})    
    elif request.method == 'POST':
        if form.is_valid():
            form.save()
            if request.is_ajax():
                response = {'result':'true','message':'Project created.'}
                return HttpResponse(simplejson.dumps(response),mimetype="application/json");
            return HttpResponseRedirect("/")
        else:
            if request.is_ajax():
                response = {'result':'false','message':'Form is invalid.'}
                return HttpResponse(simplejson.dumps(response),mimetype="application/json");
            return render(request,"ticket/create_requestuser.html",{'form':form,'username':request.user,'title':'Create Responsible','projects':getProjectList()})    

def getProjectList():
    return Project.objects.all().order_by("name")

def listProjects(request):
    projects = getProjectList().order_by("name")
    return render_to_response("ticket/show_projects.html",{'projects':projects,'title':'Project List','user':request.user})

def showProject(request,project_name):
    project = Project.objects.get(name=project_name)
    tickets = Ticket.objects.filter(project=project).order_by("-id")
    search_form = SearchTicketForm(initial={'project_id':project})
    return render_to_response("ticket/index.html",{'tickets':tickets,'search_form':search_form,'title':project_name+" Project",'user':request.user,'projects':getProjectList()})

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
    return render_to_response("ticket/index.html",{'tickets':tickets,'title':'Tickets done by ' + username,'user':request.user,'projects':getProjectList() })

def showRequestUser(request,requestuser_id):
    requestUser = RequestUser.objects.get(id=requestuser_id)
    tickets = Ticket.objects.filter(requested_by=requestuser_id).order_by("-id")
    return render_to_response("ticket/index.html",{'tickets':tickets,'title':'Tickets requested by ' + requestUser.username,'user':request.user,'projects':getProjectList() })

def showTicket(request,ticketId):
    ticket = Ticket.objects.filter(id=ticketId)

    return render_to_response("ticket/index.html",{'tickets':ticket,'title':'Ticket ','fullView':True,'projects':getProjectList()})



