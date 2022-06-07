from django.shortcuts import render
from django.shortcuts import get_object_or_404, render,redirect
import datetime as dt
from django.contrib.auth.decorators import login_required
from .models import *
from .models import Image,Profile,Likes,Comments
from django.http  import HttpResponse,Http404
from django.contrib import messages
from .forms import *
from django.contrib.auth import login, authenticate
from .forms import NewUserForm
from django.contrib.auth.forms import AuthenticationForm 


# Create your views here.
# @login_required(login_url='accounts/login/')
def home(request):
    images=Image.objects.all()

    return render(request,'index.html',{'images':images})

def register_request(request):
	if request.method == "POST":
		form = NewUserForm(request.POST)
		if form.is_valid():
			user = form.save()
			login(request, user)
			messages.success(request, "Registration successful." )
			return redirect("main:homepage")
		messages.error(request, "Unsuccessful registration. Invalid information.")
	form = NewUserForm()
	return render (request=request, template_name="/IG/registration/registration_form.html", context={"register_form":form})

def login_request(request):
	if request.method == "POST":
		form = AuthenticationForm(request, data=request.POST)
		if form.is_valid():
			username = form.cleaned_data.get('username')
			password = form.cleaned_data.get('password')
			user = authenticate(username=username, password=password)
			if user is not None:
				login(request, user)
				messages.info(request, f"You are now logged in as {username}.")
				return redirect("main:homepage")
			else:
				messages.error(request,"Invalid username or password.")
		else:
			messages.error(request,"Invalid username or password.")
	form = AuthenticationForm()
	return render(request=request, template_name="/IG/registration/login.html", context={"login_form":form})

# def login_user(request):

#     if request.method == 'POST':
#         email = request.POST.get('email')
#         password = request.POST.get('password')

#     return render(request, 'registration/login.html')



def single_image(request,image_id):
    image=get_object_or_404(Image,id=image_id)
    comments=Comments.objects.filter(image=image).all()
    current_user=request.user
    if request.method =='POST':
        form = CommentForm(request.POST)
        
        if form.is_valid():
            comment = form.save(commit=False)
            comment.user = current_user
            
            comment.image = image
            comment.save()
        return redirect('home')
    else:
        
        form = CommentForm()
    return render(request, 'image.html', {'image': image, 'form':form, 'comments':comments})
    


@login_required
def search_results(request):
  if 'name' in request.GET and request.GET["name"]:
    name = request.GET.get('name')
    users = Profile.search_profiles(name)
    images = Image.search_images(name)
    print(users)
    return render(request, 'search.html', {"users": users, "images": images})
  else:
    return render(request, 'search.html')

# @login_required(login_url='accounts/login/')
def profile(request,user_id):
    current_user=get_object_or_404(User,id=user_id)
    # current_user = request.user
    images = Image.objects.filter(user=current_user)
    profile = get_object_or_404(Profile,id = current_user.id)
    return render(request, 'profile/profile.html', {"images": images, "profile": profile})
# @login_required(login_url='accounts/login/')
def add_image(request):
    if request.method=='POST':
        current_user=request.user
        form=AddImageForm(request.POST,request.FILES)
        if form.is_valid():
            image=form.save(commit=False)
            image.user=current_user
            image.save()
            messages.success(request,('Image was posted successfully!'))
            return redirect('home')
    else:
            form=AddImageForm()
    return render(request,'add_image.html',{'form':form})
def update_profile(request):
  	#Get the profile
    current_user=request.user
    profile = Profile.objects.filter(id=current_user.id).first()
    if request.method == 'POST':
        profileform = UpdateProfileForm(request.POST,request.FILES,instance=profile)
        if  profileform.is_valid:
            profileform.save(commit=False)
            profileform.user=request.user
            profileform.save()
            return redirect('profile')
    else:
        form=UpdateProfileForm()
    return render(request,'profile/update_profile.html',{'form':form})
def like_image(request, image_id):
    image = get_object_or_404(Image,id = image_id)
    like = Likes.objects.filter(image = image ,user = request.user).first()
    if like is None:
        like = Likes()
        like.image = image
        like.user = request.user
        like.save()
    else:
        like.delete()
    return redirect('home')