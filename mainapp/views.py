from django.views.generic import TemplateView
from datetime import datetime

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
        context_data['object_list'] = [
            {
                'title': 'Новость раз',
                'preview': 'Превью для новости раз',
                'date': datetime.now()
            },{
                'title': 'Новость два',
                'preview': 'Превью для новости два',
                'date': datetime.now()
            },{
                'title': 'Новость три',
                'preview': 'Превью для новости три',
                'date': datetime.now()
            },{
                'title': 'Новость четыре',
                'preview': 'Превью для новости четрые',
                'date': datetime.now()
            },{
                'title': 'Новость пять',
                'preview': 'Превью для новости пять',
                'date': datetime.now()
            }
        ]
        
        return context_data