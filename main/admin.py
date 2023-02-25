from django.contrib import admin
from .models import Resercher, HardSkills, SoftSkills, Experience, Projects, HardSkillCategory, Navigations

# Register your models here.
class SoftSkillsInline(admin.TabularInline):
    model = SoftSkills
    extra = 0
    ordering = ['idsort', ]
    list_editable = ['idsort', ]
    classes = ('grp-collapse grp-closed',)
    inline_classes = ('grp-collapse grp-closed',)
    sortable_field_name = "idsort"

class HardSkillsInline(admin.TabularInline):
    model = HardSkillCategory
    extra = 0
    ordering = ['idsort', ]
    list_editable = ['idsort', 'name', 'raite',]
    classes = ('grp-collapse grp-open',)
    inline_classes = ('grp-collapse grp-open',)
    sortable_field_name = "idsort"
    fieldsets = (
        ('Навыки',
         {'fields': (
             ('idsort', 'name', 'raite',),)}),
    )

class ResercherAdmin(admin.ModelAdmin):
    list_display = ['name', 'profession', 'telephone', 'skype', 'linkedin', 'country', 'city', 'adress',]
    list_display_links = ['name', 'profession', 'telephone', 'country', 'city', 'adress',]
    inlines = [
        SoftSkillsInline,
        # HardSkillsInline,
    ]
admin.site.register(Resercher, ResercherAdmin)



class ProjectsAdmin(admin.ModelAdmin):
    list_display = ['idsort', 'name', 'link',]
    list_display_links = ['idsort', 'name', 'link',]
admin.site.register(Projects, ProjectsAdmin)

class ExperienceAdmin(admin.ModelAdmin):
    list_display = ['name', 'postion', 'start_work', 'end_work', 'link',]
    list_display_links = ['name', 'postion', 'start_work', 'end_work', 'link',]
    ordering = ['-end_work', ]
admin.site.register(Experience, ExperienceAdmin)

@admin.register(HardSkills)
class HardSkillsAdmin(admin.ModelAdmin):
    list_display = ['id', 'idsort', 'name', 'raite', 'category',]
    list_editable = ['idsort', 'name', 'raite', 'category', ]
    ordering = ('-category', 'idsort')
# admin.site.register(HardSkills, HardSkillsAdmin)

@admin.register(HardSkillCategory)
class HardSkillCategoryAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'idsort']
    list_display_links = ['id', 'name',]
    list_editable = ['idsort',]



@admin.register(Navigations)
class NavigationsAdmin(admin.ModelAdmin):
    list_display = ['id', 'link', 'idsort', 'variant',]
    list_display_links = ['id', 'link',]
    list_editable = ['idsort',]
    prepopulated_fields = {'link':('variant',)}