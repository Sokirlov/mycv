from django.shortcuts import render
from .models import Resercher, HardSkills, SoftSkills, Experience, Projects


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
