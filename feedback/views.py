from django.shortcuts import render

def home(request):
    return render(request, 'feedback/home.html')


from django.shortcuts import render, redirect
from .models import Offer
from .forms import OfferForm

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

    offers_list = Offer.objects.all()
    return render(request, 'feedback/offers.html', {'form': form, 'offers': offers_list})


from .models import Problem
from .forms import ProblemForm

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

    problems_list = Problem.objects.all()
    return render(request, 'feedback/problems.html', {'form': form, 'problems': problems_list})


from .models import Comment
from .forms import CommentForm

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

    comments_list = Comment.objects.filter(offer_id=offer_id)
    return render(request, 'feedback/comments.html', {'form': form, 'comments': comments_list})

