from django.shortcuts import render, get_object_or_404
from eventex.core.models import Speaker, Talk, Course
from django.views.generic.list import ListView
from django.views.generic import DetailView


# def home(request):
#     speakers = Speaker.objects.all()

#     return render(request, 'index.html', {'speakers': speakers})
home = ListView.as_view(template_name='index.html', model=Speaker)

# def speaker_detail(request, slug):
#     speaker = get_object_or_404(Speaker, slug=slug)

#     return render(request, 'core/speaker_detail.html', {'speaker': speaker})
speaker_detail = DetailView.as_view(model=Speaker)


# def talk_list(request):
#     context = {
#         'morning_talks': Talk.objects.at_morning(),
#         'afternoon_talks': Talk.objects.at_afternoon(),
#         'courses': Course.objects.all(),
#     }
#     return render(request, 'core/talk_list.html', context)
talk_list = ListView.as_view(model=(Talk, Course))
