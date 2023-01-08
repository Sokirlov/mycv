from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound
from .models import Resercher, HardSkills, SoftSkills, Experience, Projects
import pdfkit
from rest_framework import viewsets
from .serializers import AllSerializer, HardSkillsSerializer, SoftSkillsSerializer, ExperienceSerializer, ProjectsSerializer

class AllApiView(viewsets.ModelViewSet):
    queryset = Resercher.objects.all().prefetch_related('hardskills_set', 'softskills_set', 'experience_set', 'projects_set',)
    serializer_class = AllSerializer


def AllViews(request):
    resercher = Resercher.objects.all()
    hardskills = HardSkills.objects.all()
    softskills = SoftSkills.objects.all()
    experience = Experience.objects.all()
    projects = Projects.objects.all()
    return render(request, 'base.html', {'resercher': resercher,
                                         'hardskills': hardskills,
                                         'softskills': softskills,
                                         'experience': experience,
                                         'projects': projects})
def Downloads(request):
    resercher = Resercher.objects.all()
    hardskills = HardSkills.objects.all()
    softskills = SoftSkills.objects.all()
    experience = Experience.objects.all()
    projects = Projects.objects.all()
    return render(request, 'pdf.html', {'resercher': resercher,
                                           'hardskills': hardskills,
                                           'softskills': softskills,
                                           'experience': experience,
                                           'projects': projects})

def pdf(request):
    file_data = pdfkit.from_url(url='http://g.fotka.kiev.ua/print/')
    try:
        response = HttpResponse(file_data, content_type='application/pdf')
        response['Content-Disposition'] = f'attachment; filename="sokolov_kyrylo_python_developer.pdf"'
    except:
        response = HttpResponseNotFound('<h1>File not exist</h1>')
    return response