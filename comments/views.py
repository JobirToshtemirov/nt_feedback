from django.contrib.auth.decorators import login_required
from django.shortcuts import render

from comments.forms import CommentForm
from comments.models import CommentModel
from feedback_nt.models import FeedbackModel


@login_required
def createCommentView(request, pk):
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.user.pk = 30
            comment.feedback = FeedbackModel.objects.get(pk=pk)
            comment.save()
            comments = CommentModel.objects.filter(feedback=pk)
            feedback = FeedbackModel.objects.get(pk=pk)
            context = {
                'feedback': feedback,
                'comments': comments
            }
            return render(request, 'comment.html', {'comment': context})
    else:
        try:
            feedback = FeedbackModel.objects.get(pk=pk)
            feedback.see += 1
            feedback.save()
            comments = CommentModel.objects.filter(feedback=feedback)
            context = {
                'feedback': feedback,
                'comments': comments
            }
            return render(request, 'comment.html', context)
        except FeedbackModel.DoesNotExist:
            return render(request, '404.html')
    return render(request, '404.html')
