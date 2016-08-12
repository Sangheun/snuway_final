from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.http import Http404, HttpResponse, HttpResponseRedirect
from django.contrib import messages
from django.utils import timezone



from .forms import PostForm, SearchForm
from django.contrib.auth.models import User
from .models import Post, Rating, Date

# Create your views here.
def index(request):
    return render(request, 'blog/index.html', {})

@login_required
def lend_list(request):
    lend_list=Post.objects.all()
    if request.method=='GET':
        s=SearchForm(request.GET)

        machine=request.GET.get('machine', None)
        if machine:
            lend_list=lend_list.filter(vehicle=machine)

        location=request.GET.get('location', None)
        if location:
            lend_list=lend_list.filter(location=location)

        price=request.GET.get('price', None)
        if price:
            lend_list=lend_list.filter(price__lte=price)




    return render(request, 'blog/lend_list.html', {'lend_list':lend_list, 'form':s})

@login_required
def lend_detail(request, lend_id):
    instance = get_object_or_404(Post, pk=lend_id)
    context = {
        "instance":instance,
    }
    return render(request, 'blog/lend_detail.html', context)

# form 사용
@login_required
def lend(request):
    if request.method == "POST":
        form = PostForm(request.POST or None, request.FILES or None)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.user = request.user
            instance.save()

            return redirect("blog:lend_list")
    else:
        form = PostForm()

    return render(request, 'blog/lend.html', {
        "form": form,
        })

@login_required
def lend_edit(request, lend_id):
    instance = get_object_or_404(Post, pk=lend_id)

    if (not request.user.is_staff) and (not request.user != instance.author):
        messages.warning(request, "본인 게시물만 수정 가능합니다.")
    form = PostForm(request.POST or None, request.FILES or None, instance=instance)
    if form.is_valid():
        instance = form.save(commit=False)
        instance.user = request.user
        instance.save()

        return redirect("blog:lend_list")
    context = {
        "form":form,
        "instance":instance,
    }
    return render(request, "blog/lend.html", context)

@login_required
def my_page(request, pk):
    user = User.objects.get(pk=pk)
    ratings = Rating.objects.filter(user=pk)
    user_posts = Post.objects.filter(author=pk)

    if (not request.user.is_staff) and (request.user != user):
        raise Http404

    context = {
    "user":user,
    "user_posts":user_posts,
    'ratings':ratings
    }
    return render(request, "blog/my.html", context)

