# Create your views here.
from django.shortcuts import render_to_response, render, HttpResponseRedirect, HttpResponse, get_object_or_404
from ticket.models import Ticket,Project,RequestUser
from ticket.forms import CreateProjectForm, CreateTicketForm, SearchTicketForm, CreateRequestUser
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.template.defaultfilters import slugify as slugify_original
from django.core.urlresolvers import reverse
from django.utils import simplejson
from django.db.models import Count


TEMPLATE_REQUESTUSER_FORM = "ticket/form_requestuser.html"
TEMPLATE_PROJECT_FORM = "ticket/form_project.html"
TEMPLATE_TICKET_FORM = "ticket/form_ticket.html"
TEMPLATE_TICKET_LIST = "ticket/list_tickets.html"
TEMPLATE_PROJECT_LIST = "ticket/list_projects.html"

def slugify(value):
    value = value.replace(u'\u0131', 'i')
    return slugify_original(value)

def home(request):
    tickets = Ticket.objects.all().order_by("-id")
    search_form = SearchTicketForm()
    context = {
        'tickets': tickets,
        'search_form': search_form,
        'title': 'All Tickets',
        'user': request.user,
        'fullView': False,
        'projects': getProjectList()
        }
    return render_to_response( TEMPLATE_TICKET_LIST, context )

@login_required
def createProject(request):
    form = CreateProjectForm(request.POST or None)
    if request.method == 'GET':
        context = {
            'form': form,
            'title': 'Create Project',
            'user': request.user,
            'projects': getProjectList()
            }
        return render( request, TEMPLATE_PROJECT_FORM, context)
    elif request.method == 'POST':
        if form.is_valid():
            form.save()
            if request.is_ajax():
                response = {
                    'result': 'true',
                    'message': 'Project created.'
                    }
                return HttpResponse(simplejson.dumps(response), mimetype="application/json");
            return HttpResponseRedirect(reverse("ListProjects"))
        else:
            if request.is_ajax():
                response = {
                    'result': 'false',
                    'message': 'Form is invalid.'
                    }
                return HttpResponse(simplejson.dumps(response), mimetype="application/json");
            context = {
                'form': form,
                'title': 'Create Project',
                'user': request.user,
                'projects': getProjectList()
                }
            return render_to_response( TEMPLATE_PROJECT_FORM, context )

@login_required
def createTicket(request):
    form = CreateTicketForm(request.POST or None)
    if request.method == 'GET':
        context = {
            'form': form,
            'title': 'Create Ticket',
            'user': request.user, 
            'projects': getProjectList() 
            }
        return render( request, TEMPLATE_TICKET_FORM, context )
    elif request.method == 'POST':
        if form.is_valid():
            ticket = form.save(commit=False)
            ticket.user = request.user
            ticket.save();
            if request.is_ajax():
                response = {
                    'result': 'true',
                    'message': 'Ticket created.',
                    'redirect': reverse("ShowTicket",args=(str(ticket.id),) ) 
                    }
                return HttpResponse(simplejson.dumps(response),mimetype="application/json");
            return HttpResponseRedirect(reverse("ShowTicket",args=(str(ticket.id),)) )
        else:
            if request.is_ajax():
                response = {'result':'false','message':'Form is invalid.'}
                return HttpResponse(simplejson.dumps(response),mimetype="application/json");
            context = {
                'form': form,
                'title': 'Create Ticket',
                'user': request.user,
                'projects': getProjectList()
                }
            return render( request, TEMPLATE_TICKET_FORM, context)
    
@login_required
def createRequestUser(request):
    form = CreateRequestUser(request.POST or None)
    if request.method == 'GET':
        context = {
            'form': form,
            'username': request.user,
            'title': 'Create Responsible',
            'projects': getProjectList()
            }
        return render( request, TEMPLATE_REQUESTUSER_FORM, context )
    elif request.method == 'POST':
        if form.is_valid():
            form.save()
            if request.is_ajax():
                response = {
                    'result': 'true',
                    'message': 'User created.'
                    }
                return HttpResponse(simplejson.dumps(response),mimetype="application/json");
            return HttpResponseRedirect( reverse("Home") )
        else:
            if request.is_ajax():
                response = {
                    'result': 'false',
                    'message': 'Form is invalid.'
                    }
                return HttpResponse(simplejson.dumps(response),mimetype="application/json");
            context = {
                'form': form,
                'username': request.user,
                'title': 'Create Responsible',
                'projects': getProjectList()
                }
            return render( request, TEMPLATE_REQUESTUSER_FORM, context )

def getProjectList():
    return Project.objects.all().order_by("name").annotate(ticket_count=Count('ticket'))

def listProjects(request):
    projects = getProjectList()
    context = {
        'projects': projects,
        'title': 'Project List',
        'user': request.user
        }
    return render_to_response( TEMPLATE_PROJECT_LIST, context )

def showProject(request,project_name):
    project = Project.objects.get(name=project_name)
    tickets = Ticket.objects.filter(project=project).order_by("-id")
    search_form = SearchTicketForm(initial={'project_id':project})
    context = {
        'tickets': tickets,
        'search_form': search_form,
        'title': project_name+" Project",
        'user': request.user,
        'projects': getProjectList(),
        'currentProject': project
        }
    return render_to_response( TEMPLATE_TICKET_LIST, context )

def searchTicket(request):
    request_query = request.GET["query"]
    request_project = request.GET["project"]
    print "HEHEHE: " + request_project 
    if  len(request_project) > 0 and request_project != 'ALL':
        tickets = Ticket.objects.filter(
                            content__icontains=request_query, \
                            project=Project.objects.get(name=request_project) ) \
                                .order_by("-id")
        project = Project.objects.get(name=request_project).__str__()
    else:
        tickets = Ticket.objects.filter(content__icontains=request_query) \
                                .order_by("-id")
        project = "ALL"
    form = SearchTicketForm()
    context = {
        'tickets': tickets,
        'search_form': form,
        'title': 'Search for ' + request.GET["query"] + ' in ' + project,
        'user': request.user,
        'projects': getProjectList(),
        'query': request_query,
        'currentProject': project
        }
    return render_to_response( TEMPLATE_TICKET_LIST, context )

def showUser(request,username):
    tickets = Ticket.objects.filter(user=User.objects.filter(username=username)) \
                            .order_by("-id")
    context = {
        'tickets': tickets,
        'title': 'Tickets done by ' + username,
        'user': request.user,
        'projects': getProjectList() 
        }
    return render_to_response( TEMPLATE_TICKET_LIST, context )

def showRequestUser(request,requestuser_id):
    requestUser = RequestUser.objects.get(id=requestuser_id)
    tickets = Ticket.objects.filter(requested_by=requestuser_id).order_by("-id")
    context = {
        'tickets': tickets,
        'title': 'Tickets requested by ' + requestUser.username,
        'user': request.user,
        'projects': getProjectList() 
        }
    return render_to_response( TEMPLATE_TICKET_LIST, context )

def showTicket(request,ticketId):
    ticket = Ticket.objects.filter(id=ticketId)
    context = {
        'tickets': ticket,
        'title': 'Ticket ',
        'fullView': True,
        'user': request.user,
        'projects': getProjectList()
        }
    return render_to_response( TEMPLATE_TICKET_LIST, context )

def editTicket(request,ticketId):
    ticket = get_object_or_404(Ticket,id=ticketId)
    form = CreateTicketForm(request.POST or None,instance=ticket)
    if request.method == 'GET':
        context = {
            'form': form,
            'title': 'Edit Ticket',
            'user': request.user,
            'projects': getProjectList(),
            'ticketId': ticketId
            }
        return render( request, TEMPLATE_TICKET_FORM, context)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            if request.is_ajax():
                response = {
                    'result':'true',
                    'message':'Ticket has changed.',
                    'redirect':reverse("ShowTicket",args=(ticketId,))
                    }
                return HttpResponse(simplejson.dumps(response),mimetype="application/json");
            return HttpResponseRedirect( reverse("ShowTicket",args=(ticketId,)) )
        else:
            if request.is_ajax():
                response = {'result':'false','message':'Form is invalid.'}
                return HttpResponse(simplejson.dumps(response),mimetype="application/json");
            context = {
                'form':form,
                'title':'Edit Ticket',
                'user':request.user,
                'projects':getProjectList(),
                'ticketId':ticketId
                }
            return render( request, TEMPLATE_TICKET_FORM, context )

def deleteTicket(request):
    print request
    ticket = get_object_or_404(Ticket,id=request.POST["ticketId"])
    
    if request.method == 'POST':
        if request.is_ajax():
            ticket.delete()        
            response = { 
                'result':'true',
                'message':'Ticket has deleted!' ,
                'redirect': '/'
                }
            return HttpResponse(simplejson.dumps(response),mimetype="application/json");
    else:
        context = {
            'title':'Edit Ticket',
            'user':request.user,
            'projects':getProjectList(),
            'ticketId':request.POST.ticketId
            }
        return render( request, TEMPLATE_TICKET_FORM, context )






















