from django.http import Http404
from django.shortcuts import redirect, render
from .models import Image, Profile
from .forms import CommentForm, PostForm, ProfileForm
from django.core.exceptions import ObjectDoesNotExist
from django.contrib.auth.decorators import login_required


# Create your views here.
def index(request):
    image = Image.objects.all()
    return render(request, 'index.html', {"image": image})

def home(request):
    image = Image.objects.all()
    profile = Profile.objects.all()
    
    return render(request, 'home.html', {"image": image, "profile": profile})

@login_required(login_url='/accounts/login/')
def search(request):
    if 'image' in request.GET and request.GET['image']:
        searchname = request.GET.get('image')
        searchimage= Image.search_by_image_name(searchname)
        message = f"{searchname}"

        return render(request, 'search.html', {"message": message, "image": searchimage})
    else:
        message ="You havent searched any images "
        return render(request, 'search.html',{"message": message})

@login_required(login_url='/accounts/login/')
def single_image(request, image_id):
    try:
        image = Image.objects.get(id=image_id)
    except ObjectDoesNotExist:
        raise Http404()

    return render(request, 'single_image.html', {'image': image})


@login_required(login_url='/accounts/login/')
def new_post(request):
    current_user = request.user
    if request.method == 'POST':
        form = PostForm(request.POST,request.FILES)
        if form.is_valid():
            image = form.save(commit=False)
            image.profile = current_user
            image.save()
        return redirect('home')
    else:
        form = PostForm()
    return render(request, 'post.html', {'form': form})

@login_required(login_url='/accounts/login/')
def profile(request):
    image = Image.objects.all()
    profile = Profile.objects.all()
    return render(request, 'profile.html', {"profile": profile, "image": image})

@login_required(login_url='/accounts/login/')
def edit_profile(request):
    current_user = request.user
    if request.method == 'POST':
        prof_form = ProfileForm(request.POST, request.FILES)
        if prof_form.is_valid():
            profile = prof_form.save(commit=False)
            profile.user = current_user
            profile.save()
        return redirect('profile')
    else:
        prof_form= ProfileForm()
    return render(request, 'update.html', {'prof_form': prof_form})

@login_required(login_url='/accounts/login/')
def comment(request):
    current_user = request.user
    if request.method == 'POST':
        form = CommentForm(request.POST, request.FILES)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.user = current_user
            comment.save()
        return redirect('home')
    else:
        form= CommentForm()
    return render(request, 'home', {'form': form})
