from .models import Resercher, HardSkills, SoftSkills, Experience, Projects, HardSkillCategory, Navigations
from rest_framework import serializers




class HardSkillsSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = HardSkills
        fields = ['id', 'idsort', 'name',]

class HardSkillCategorySerializer(serializers.HyperlinkedModelSerializer):
    skill = HardSkillsSerializer(source='hardskills_set', many=True)
    class Meta:
        model = HardSkillCategory
        fields = ['id', 'idsort', 'name', 'skill']

class SoftSkillsSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = SoftSkills
        fields = ['id', 'idsort', 'name', 'description', 'resercher']

class ExperienceSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Experience
        fields = ['id', 'name', 'postion', 'start_work', 'end_work', 'link', 'description']

class ProjectsSerializer(serializers.HyperlinkedModelSerializer):
    skils = serializers.PrimaryKeyRelatedField(queryset=HardSkills.objects.all(), many=True)
    class Meta:
        model = Projects
        fields = ['idsort', 'name', 'link', 'skils', 'description']

class NavigationsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Navigations
        fields = '__all__'

class AllSerializer(serializers.HyperlinkedModelSerializer):
    navigations_set = NavigationsSerializer(many=True, read_only=True)
    softskills_set = SoftSkillsSerializer(many=True, read_only=True)
    hardskillcategory_set = HardSkillCategorySerializer(many=True, read_only=True)
    experience_set = ExperienceSerializer(many=True, read_only=True)
    projects_set = ProjectsSerializer(many=True, read_only=True)

    class Meta:
        model = Resercher
        fields = '__all__'