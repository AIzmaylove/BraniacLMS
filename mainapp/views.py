import json

from django.conf import settings
from django.http import HttpResponseRedirect, JsonResponse
from django.urls import reverse_lazy
from django.views.generic import TemplateView, ListView, UpdateView, DeleteView, DetailView, CreateView
from datetime import datetime
from django.contrib.auth.mixins import PermissionRequiredMixin
from mainapp.forms import CourseFeedbackForm
from mainapp.models import Course, CourseFeedback, CoursesTeachers, Lesson, News
from django.shortcuts import get_object_or_404
from django.template.loader import render_to_string


class ContactsView(TemplateView):
    template_name = 'mainapp/contacts.html'

    def get_context_data(self, **kwargs):
        context_data = super().get_context_data(**kwargs)
        context_data['contacts'] = [
            {
                'mapa': 'https://yandex.ru/map-widget/v1/-/CCUAZHcrhA',
                'city': 'Санкт-Петербург',
                'phone': '+7-999-111-11-11',
                'adress': 'территория Петропавловская крепость, 3Ж',
                'email': 'geekbrains@spb.ru'
            },{
                'mapa': 'https://yandex.ru/map-widget/v1/-/CCUAZHX3xB',
                'city': 'Казань',
                'phone': '+7-999-222-22-22',
                'adress':'территория Кремль, 11, Казань, Республика Татарстан, Россия',
                'email': 'geekbrains@kzn.ru'
            },{
                'mapa': 'https://yandex.ru/map-widget/v1/-/CCUAZHh9kD',
                'city': 'Москва',
                'phone': '+7-999-333-33-33',
                'adress': 'Красная площадь, 7, Москва, Россия',
                'email': 'geekbrains@msk.ru'
            }
            
        ]
        return context_data


class CoursesListView(ListView):
    template_name = 'mainapp/courses_list.html'
    model = Course


class DocSiteView(TemplateView):
    template_name = 'mainapp/doc_site.html'
    
class IndexView(TemplateView):
    template_name = 'mainapp/index.html'
    
class LoginView(TemplateView):
    template_name = 'mainapp/login.html'
    
class NewsListView(ListView):
    model = News
    paginate_by = 5

    def get_queryset(self):
        return super().get_queryset().filter(deleted=False)

class NewsDetailView(DetailView):
    model = News

class NewsCreateView(PermissionRequiredMixin, CreateView):
    model = News
    fields = '__all__'
    success_url = reverse_lazy('mainapp:news')
    permmission_required = ('mainapp.add_news',)


class NewsUpdateView(PermissionRequiredMixin, UpdateView):
    model = News
    fields = '__all__'
    success_url = reverse_lazy('mainapp:news')
    permmission_required = ('mainapp.change_news',)

class NewsDeleteView(PermissionRequiredMixin ,DeleteView):
    model = News
    success_url = reverse_lazy('mainapp:news')
    permission_required = ('mainapp.delete_news',)



    # def get_context_data(self, **kwargs):
    #     context_data = super().get_context_data(**kwargs)
    #     # with open(settings.BASE_DIR / 'news.json') as news_file:
    #     #     context_data['object_list'] = json.load(news_file)   
    #     context_data['object_list'] = News.objects.all()
    #     return context_data

    # def get(self, *args, **kwargs):
    #     query = self.request.GET.get('q', None)
    #     if query:
    #         return HttpResponseRedirect(f'https://google.ru/search?q={query}')

    #     return super().get(*args, **kwargs)


class CourseDetailView(TemplateView):
    template_name = 'mainapp/courses_detail.html'

    def get_context_data(self, **kwargs):
        context_data = super().get_context_data(**kwargs)
        context_data['course_object'] = get_object_or_404(Course, pk=self.kwargs['pk'])
        context_data['lessons'] = Lesson.objects.filter(course=context_data['course_object'])
        context_data['teachers'] = CoursesTeachers.objects.filter(courses=context_data['course_object'])
        context_data['feedback_list'] = CourseFeedback.objects.filter(course=context_data['course_object'])
            
        if self.request.user.is_authenticated:
            context_data['feedback_form'] = CourseFeedbackForm(course=context_data['course_object'], user=self.request.user)

        return context_data


class CourseFeedbackCreateView(CreateView):
    model = CourseFeedback
    form_class = CourseFeedbackForm

    def form_valid(self, form):
        self.object = form.save()
        rendered_template = render_to_string('mainapp/includes/feedback_card.html', context={'item': self.object})
        return JsonResponse({'card': rendered_template})