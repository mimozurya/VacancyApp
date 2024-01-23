from django.db import models


class Main(models.Model):
    content = models.TextField(blank=True, verbose_name='Описание профессии')
    photo = models.ImageField(upload_to='images_db/%Y/%m/%d', blank=False, verbose_name='Фото')


class Info(models.Model):
    graph_salary_level = models.ImageField(upload_to='images_db/%Y/%m/%d', blank=False,
                                           verbose_name='График уровень зарплат по годам')
    graph_num_vacancy = models.ImageField(upload_to='images_db/%Y/%m/%d', blank=False,
                                          verbose_name='График количество вакансий по годам')
    table = models.TextField(blank=False, verbose_name='Таблица')


class Location(models.Model):
    graph_salary_level_by_city = models.ImageField(upload_to='images_db/%Y/%m/%d', blank=False,
                                                   verbose_name='График уровень зарплат по городам')
    graph_vacancy_fraction_by_city = models.ImageField(upload_to='images_db/%Y/%m/%d', blank=False,
                                                       verbose_name='График доля вакансий по городам')
    table = models.TextField(blank=False, verbose_name='Таблица')


class Ability(models.Model):
    table_name = models.TextField(blank=False, verbose_name='Название таблицы', max_length=30)
    table = models.TextField(blank=False, verbose_name='Таблица')
    graph_skills = models.ImageField(upload_to='images_db/%Y/%m/%d', blank=False, verbose_name='График по скиллам')


