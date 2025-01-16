from django.shortcuts import render, HttpResponse, get_object_or_404

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
    # active_posting = JobPosting.objects.filter(is_active=True)
    active_posting = JobPosting.objects.exclude(company = 'gonbadkabud')
    print('posting ->', active_posting)
    context = {
        'job_postings': active_posting
    }

    return render(request, 'job_board/index.html', context)


def job_detail(request, pk):
    job_posting = get_object_or_404(JobPosting, pk=pk, is_active=True)

    context = {
        'posting': job_posting
    }
    return render(request, 'job_board/detail.html', context)
