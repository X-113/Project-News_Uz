from django.core.paginator import Paginator
from django.shortcuts import render, redirect
from django.template.defaultfilters import title

from .models import Category, New, Comment, Subscription
from django.db.models import Q
from .forms import ContactForm
from django.http import JsonResponse




# Create your views here.

def index(request):
    news = New.objects.all().order_by('-id')
    actual = news.filter(Q(title__icontains='tramp') | Q(description__icontains='tramp'))

    ctx = {
        "news": news,
        "actual": actual
    }
    return render(request, "index.html", ctx)


def category(request, slug):
    ctg = Category.objects.filter(slug=slug).first()
    if not ctg:
        return render(request, 'category.html', {"error": 404})

    news = New.objects.filter(ctg=ctg).order_by('-id')
    if len(news) == 0:
        return render(request, 'category.html', {"error": 404})


    paginator = Paginator(news, per_page=5)
    page = int(request.GET.get('page', 1))
    natija = paginator.get_page(page)


    ctx = {
        "ctg": ctg,
        "news": natija,
        "page": page,
        "paginator": paginator

    }
    return render(request, "category.html", ctx)


def search(request):
    savol = request.GET.get('search', None)
    if not savol:
        return render(request, 'category.html', {"error": 404})

    # (|)-> or, (&)-> and, (~)-> not
    news = New.objects.filter(
        Q(title__icontains=savol) |
        Q(short_desc__icontains=savol) |
        Q(description__icontains=savol) |
        Q(tags__icontains=savol) |
        Q(ctg__name__icontains=savol)
    )

    paginator = Paginator(news, per_page=5)
    page = int(request.GET.get('page', 1))
    natija = paginator.get_page(page)


    ctx = {
        "news": natija,
        "page": page,
        "paginator": paginator,
        "key": savol
    }
    return render(request, "search.html", ctx)

def view(request, pk):
    new = New.objects.filter(id=pk).first()
    if not new:
        return render(request, 'category.html', {'error': 404})
    new.increase_view()

    if request.POST:
        user = request.POST['user']
        message = request.POST['message']
        parent_id = request.POST.get('parent_id', None)

        Comment.objects.create(
            parent_id = parent_id,
            user = user,
            message = message,
            is_sub = True if parent_id else False,
            new = new
        )

    # commentlar:
    comments = Comment.objects.filter(new=new, is_sub=False).order_by('-id')

    ctx = {
        "new": new,
        "comments": comments,
        "count": len(comments)
    }
    return render(request, "view.html", ctx)

def contact(request):
    ctx = {}
    if request.POST:
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            ctx['javob'] = "Xabaringiz muvaffaqiyatli yuborildi!"
        else:
            print(form.errors)

    return render(request, "contact.html", ctx)


def add_subs(request):
    path = request.GET['path']
    if request.POST:
        try:
            Subscription.objects.get_or_create(email=request.POST['email'])
        except:
            return render(request, 'category.html', {'error': 404})

    return redirect(path)





# def api_test(request):
#     ctx = {
#         "xabar": "Bu test API"
#     }
#     return JsonResponse(ctx, status=200)
























