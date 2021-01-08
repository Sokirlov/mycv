from django.contrib.auth.models import User, Group
from .models import Resercher, HardSkills, SoftSkills, Experience, Projects
from rest_framework import serializers



class HardSkillsSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = HardSkills
        fields = ['idsort', 'name', 'raite', 'resercher']

class SoftSkillsSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = SoftSkills
        fields = ['idsort', 'name', 'raite', 'resercher']

class ExperienceSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Experience
        fields = ['name', 'postion', 'start_work', 'end_work', 'link', 'description']

class ProjectsSerializer(serializers.HyperlinkedModelSerializer):
    skils = serializers.PrimaryKeyRelatedField(queryset=HardSkills.objects.all(), many=True)
    class Meta:
        model = Projects
        fields = ['idsort', 'name', 'link', 'skils', 'description']
        # fields = '__all__'



# class AllSerializer(serializers.HyperlinkedModelSerializer):
class AllSerializer(serializers.ModelSerializer):
    hardskills_set = HardSkillsSerializer(many=True, read_only=True)
    softskills_set = SoftSkillsSerializer(many=True, read_only=True)
    experience_set = ExperienceSerializer(many=True, read_only=True)
    projects_set = ProjectsSerializer(many=True, read_only=True)
    # projects_set = serializers.StringRelatedField(many=True, read_only=True)

    class Meta:
        model = Resercher
        fields = '__all__'
        # fields = ['name', 'profession', 'avatar', 'telephone', 'country', 'city', 'adress', 'introduction', 'hardskills', 'softskills', 'experience', 'projects']