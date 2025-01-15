from django.shortcuts import render, HttpResponse

from .models import JobPosting
# Create your views here.


# def index(request):
#     context = {
#         'movies':['gladiator','anything','test']
#     }
#     return render(request, 'movies/index.html', context)

# app/templates/app/index.html


# def about(request):
#     return render(request, 'movies/about.html')


def index(request):
    active_posting = JobPosting.objects.filter(is_active=True)
    context = {
        'job_postings': active_posting
    }

    return render(request, 'job_board/index.html', context)


def job_detail(request, pk):
    job_posting = JobPosting.objects.get(pk=pk)
    context = {
        'posting': job_posting
    }
    return render(request, 'job_board/detail.html', context)
