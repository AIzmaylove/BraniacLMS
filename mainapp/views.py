import json

from django.conf import settings
from django.http import HttpResponseRedirect
from django.views.generic import TemplateView
from datetime import datetime

from mainapp.models import News

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


class CoursesListView(TemplateView):
    template_name = 'mainapp/courses_list.html'
    
class DocSiteView(TemplateView):
    template_name = 'mainapp/doc_site.html'
    
class IndexView(TemplateView):
    template_name = 'mainapp/index.html'
    
class LoginView(TemplateView):
    template_name = 'mainapp/login.html'
    
class NewsView(TemplateView):
    template_name = 'mainapp/news.html'

    def get_context_data(self, **kwargs):
        context_data = super().get_context_data(**kwargs)
        # with open(settings.BASE_DIR / 'news.json') as news_file:
        #     context_data['object_list'] = json.load(news_file)   
        context_data['object_list'] = News.objects.all()
        return context_data

    def get(self, *args, **kwargs):
        query = self.request.GET.get('q', None)
        if query:
            return HttpResponseRedirect(f'https://google.ru/search?q={query}')

        return super().get(*args, **kwargs)