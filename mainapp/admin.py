from django.contrib import admin
from mainapp.models import News, Course, CoursesTeachers, Lesson 


# admin.site.register(Course)
# admin.site.register(CoursesTeachers)
# admin.site.register(Lesson)


@admin.register(News)
class NewsAdmin(admin.ModelAdmin):
    list_display = ('pk', 'title', 'slug', 'deleted')
    list_per_page = 2
    search_fields = ('title', 'intro', 'body')
    actions = ('mark_as_delete',)


    def slug(self, obj):
        return obj.title.lower().replace(' ', '-')

    slug.short_description = 'Слаг'

    def mark_as_delete(self, request, queryset):
        queryset.update(deleted=True)

    mark_as_delete.short_description = 'Пометить удаленным'


@admin.register(Lesson)
class LessonAdmin(admin.ModelAdmin):
    list_display = ('title', 'pk', 'course', 'num', 'deleted' )
    list_per_page = 1
    list_filter = ('created_at',)
    search_fields = ('title', 'course', 'description')
    actions = ('mark_as_delete',)

    def mark_as_delete(self, request, queryset):
        queryset.update(deleted=True)

    mark_as_delete.short_description = 'Пометить удаленным'

@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = ('name', 'pk', 'cost', 'deleted' )
    # list_per_page = 1
    list_filter = ('created_at',)
    search_fields = ('name', 'description')
    actions = ('mark_as_delete',)

    # def mark_as_delete(self, request, queryset):
    #     queryset.update(deleted=True)

    # mark_as_delete.short_description = 'Пометить удаленным'

@admin.register(CoursesTeachers)
class CoursesTeachersAdmin(admin.ModelAdmin):
    list_display = ('name_second', 'name_first', 'day_birth')
    # list_per_page = 2
    search_fields = ('name_second', 'name_first', 'courses')
    actions = ('mark_as_delete',)
    
    def mark_as_delete(self, request, queryset):
        queryset.update(deleted=True)

    mark_as_delete.short_description = 'Пометить удаленным'
