from django.shortcuts import render
from .models import Resercher, HardSkills, SoftSkills, Experience, Projects

from rest_framework import viewsets
from rest_framework import permissions
from rest_framework import generics

from .serializers import AllSerializer, HardSkillsSerializer, SoftSkillsSerializer, ExperienceSerializer, ProjectsSerializer


# class AllApiView(generics.ListCreateAPIVie):
class AllApiView(viewsets.ModelViewSet):
    queryset = Resercher.objects.all().prefetch_related('hardskills_set', 'softskills_set', 'experience_set', 'projects_set',)
    serializer_class = AllSerializer




# class AllApiView(viewsets.ModelViewSet):
#     """
#     API endpoint that allows users to be viewed or edited.
#     """
#     # resercher = Resercher.objects.all()
#     # hardskills = HardSkills.objects.all()
#     # softskills = SoftSkills.objects.all()
#     # experience = Experience.objects.all()
#     # projects = Projects.objects.all()
#
#     queryset = Resercher.objects.all().prefetch_related()
#     serializer_class = AllSerializer
#     # permission_classes = [permissions.IsAuthenticated]


# Create your views here.
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

# def Test(request):
#     resercher = Resercher.objects.all().prefetch_related('hardskills_set', 'softskills_set', 'experience_set',
#                                                         'projects_set')
#     return render(request, 'base1.html', {'resercher': resercher})