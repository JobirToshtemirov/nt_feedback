from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect
from .models import CommentModel, ProblemModel, OfferModel
from .forms import CommentForm, ProblemForm, OfferForm


def home(request):
    return render(request, 'index.html')


def offers(request):
    if request.method == 'POST':
        form = OfferForm(request.POST)
        if form.is_valid():
            offer = form.save(commit=False)
            offer.user = request.user
            offer.save()
            return redirect('offers')
    else:
        form = OfferForm()

    offers_list = OfferModel.objects.all()
    return render(request, 'offers.html', {'form': form, 'offers': offers_list})


def problems(request):
    if request.method == 'POST':
        form = ProblemForm(request.POST)
        if form.is_valid():
            problem = form.save(commit=False)
            problem.user = request.user
            problem.save()
            return redirect('problems')
    else:
        form = ProblemForm()

    problems_list = ProblemModel.objects.all()
    return render(request, 'problems.html', {'form': form, 'problems': problems_list})


def comments(request, offer_id):
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.user = request.user
            comment.offer_id = offer_id
            comment.save()
            return redirect('comments', offer_id=offer_id)
    else:
        form = CommentForm()

    comments_list = CommentModel.objects.filter(offer_id=offer_id)
    return render(request, 'comments.html', {'form': form, 'comments': comments_list})


def auth_view(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('home')
    else:
        form = UserCreationForm()

    return render(request, 'auth.html', {'form': form})


@login_required
def profile(request):
    return render(request, 'profile.html', {'user': request.user})


def page_not_found(request, ):
    return render(request, '404.html', status=404)
