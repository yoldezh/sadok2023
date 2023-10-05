from django.http import HttpResponse, HttpRequest
from django.shortcuts import render, redirect
from django.contrib import messages
from django.forms import modelformset_factory
from .forms import PostForm, MediaForm
from .models import Post, Media

def create(request: HttpRequest) -> HttpResponse:
    template_name: str  = 'app/post/create.html'
    context:  dict[str,any] = {}
    mediaFormset = modelformset_factory(model=Media, form=MediaForm, extra=2)

    if request.method == 'POST':
        form_text = PostForm(request.POST)
        form_media = mediaFormset(request.POST, request.FILES)
        text = form_text.data
        media = form_text.data


        if form_text.is_valid() and form_media.is_valid():  
            pub = form_text.save(commit=False)
            pub.owner = request.user
            pub.save()

            new_media = form_media.save(commit=False)  
            for f in new_media:
                f.post = pub
                f.save()  

            messages.success(request, 'Post was added successfully')
            return redirect('list.html') 
        else:
            messages.error(request, "Oops, try again later")
    else:
        form_text = PostForm()
        form_media = mediaFormset(queryset=Media.objects.none())
        messages.error(request, "Oops, populate these files")

    context['form_text'] = form_text
    context['form_media'] = form_media
    return render(request, template_name, context)

def post_list(request):
    template_name = 'app/post/list.html'
    context = {}

    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('post_list')
    else:
     form = PostForm()
    posts = Post.objects.all()
    post_media= Media.objects.all()

    context['posts'] = posts
    context['form'] = form
    context['media.image'] = post_media 


    return render(request, template_name, context)