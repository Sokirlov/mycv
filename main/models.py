from django.db import models
from io import BytesIO
from PIL import Image


class Resercher(models.Model):
    name = models.CharField('Фмилия Имя Отчество', max_length=500)
    profession = models.CharField('Профессия', max_length=150)
    avatar = models.ImageField('Фотография', upload_to='img/', blank=True, null=True)
    telephone = models.CharField('Номер телефона', max_length=10, default='0000000000')
    country = models.CharField('Страна', max_length=50)
    city = models.CharField('Город', max_length=50)
    adress = models.CharField('Адрес', max_length=250)
    introduction = models.TextField('Приветствие', max_length=1000, blank=True, null=True)

    class Meta:
        verbose_name = 'Cоискатель'
        verbose_name_plural = 'Соискатель'

    def __str__(self):
        return self.name


class HardSkills(models.Model):
    SKILL_RAITE = (
        ('20', 'Знаком',),
        ('40', 'Вник',),
        ('60', 'Уверенно знаю',),
        ('80', 'Хорошо знаю',),
        ('100', 'Отлично знаю',),
    )
    idsort = models.PositiveSmallIntegerField('Сортировка', auto_created=True)
    name = models.CharField('Название навыка', max_length=100)
    raite = models.CharField('Уровень навыка', choices=SKILL_RAITE, max_length=14)
    resercher = models.ForeignKey(Resercher, on_delete=models.CASCADE)

    class Meta:
        ordering = ['idsort']
        verbose_name = 'Знания'
        verbose_name_plural = 'Знания'

    def __str__(self):
        return self.name


class SoftSkills(models.Model):
    SKILL_RAITE_CHOICES = (
        ('20', 'Знаком'),
        ('40', 'Разбираюсь'),
        ('60', 'Уверенно'),
        ('80', 'Хорошо'),
        ('100', 'Отлично'),
    )
    idsort = models.PositiveSmallIntegerField('Сортировка', auto_created=True)
    name = models.CharField('Название навыка', max_length=100)
    raite = models.CharField('Уровень навыка', choices=SKILL_RAITE_CHOICES, max_length=14)
    resercher = models.ForeignKey(Resercher, on_delete=models.CASCADE)

    class Meta:
        ordering = ['idsort']
        verbose_name = 'Характеристики'
        verbose_name_plural = 'Характеристики'

    def __str__(self):
        return self.name


class Experience(models.Model):
    name = models.CharField('Название компании', max_length=250)
    postion = models.CharField('Занимаемайя должность', max_length=500, blank=True, null=True)
    start_work = models.DateField('Начало работы в компании')
    end_work = models.DateField('Конец работы в компании')
    link = models.URLField('Сайт компании')
    description = models.TextField('Чем занимался, за что отвечал', max_length=1000)
    resercher = models.ForeignKey(Resercher, on_delete=models.CASCADE)

    class Meta:
        ordering = ['-start_work']
        verbose_name = 'Опыт работы'
        verbose_name_plural = 'Опыт работы'

    def __str__(self):
        return self.name


class Projects(models.Model):
    idsort = models.PositiveSmallIntegerField('Сортировка', auto_created=True)
    name = models.CharField('Название проекта', max_length=250)
    link = models.URLField('адрес проекта')
    skils = models.ManyToManyField(HardSkills, related_name='Знания')  #, related_name='Используемые навыки', on_delete=models.SET_NULL, null=True, blank=True)
    description = models.TextField('В чем суть проекта ?\nКакие ососбенности ?', max_length=1000)
    resercher = models.ForeignKey(Resercher, on_delete=models.CASCADE)

    class Meta:
        ordering = ['idsort']
        verbose_name = 'Проекты'
        verbose_name_plural = 'Проекты'

    def __str__(self):
        return self.name

