from django.shortcuts import render_to_response, redirect
from django.template import RequestContext
from django.contrib import auth
from django.core.context_processors import csrf
from tasks.models import Information, ImageUpload, Middleware
from tasks.forms import InformationForm, ImageUploadForm


def index(request):
    """Gets information from db"""
    data = Information.objects.all()
    args = {'data': data}
    return render_to_response('tasks/index.html', args, context_instance=RequestContext(request))


def login(request):
    """User Authentication"""
    args = {}
    args.update(csrf(request))
    photo = Information.objects.values('photo')
    args['photo'] = photo
    if request.POST:
        username = request.POST.get('username', '')
        password = request.POST.get('password', '')
        user = auth.authenticate(username=username, password=password)
        if user is not None:
            auth.login(request, user)
            return redirect('/tasks/edit/')
        else:
            args['login_error'] = 1
            return render_to_response('tasks/login.html', args, context_instance=RequestContext(request))
    else:
        return render_to_response('tasks/login.html', args, context_instance=RequestContext(request))


def logout(request):
    """Logout function"""
    auth.logout(request)
    return redirect('/')


def edit(request):
    """Function that allows to change information"""
    if not request.user.is_authenticated():
        return redirect('/tasks/login/')
    args = {}
    args.update(csrf(request))
    images = ImageUpload.objects.all()
    args['user'] = auth.get_user(request)
    args['images'] = images
    data = Information.objects.get()
    form_information = InformationForm(instance=data)
    if request.method == 'POST' and request.FILES.get('photo') is None:
        form_post = InformationForm(request.POST, instance=data)
        if form_post.is_valid():
            form_post.save()
            return redirect('/')
        else:
            args['form'] = form_post
    elif request.method == 'POST' and request.FILES.get('photo') is not None:
        form_upload = ImageUploadForm(request.POST, request.FILES)
        if form_upload.is_valid():
            new_img = ImageUpload(photo=request.FILES['photo'])
            new_img.save()
            args['form'] = form_information
            args['success'] = 1
        else:
            args['form'] = form_information
            args['form_upload'] = form_upload
    else:
        args['form'] = form_information
    return render_to_response('tasks/edit.html', args, context_instance=RequestContext(request))


def view_requests(request):
    """Displays HTTP Requests"""
    args = {
        'middleware': Middleware.objects.all().order_by('-id')[:10],
        # Added user object for testing task 6
        'information': Information.objects.get()
    }
    return render_to_response('tasks/requests.html', args, context_instance=RequestContext(request))