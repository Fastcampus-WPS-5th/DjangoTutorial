from django.contrib import admin

from .models import Question, Choice


class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 2


class QuestionAdmin(admin.ModelAdmin):
    list_display = (
        'question_text',
        'pub_date',
        'was_published_recently',
    )
    list_filter = (
        'pub_date',
    )
    search_fields = (
        'question_text',
    )
    fieldsets = [
        (None, {
            'fields': [
                'question_text',
            ]
        }),
        ('Date Information', {
            'fields': [
                'pub_date',
            ]
        })
    ]
    inlines = (ChoiceInline,)


# admin.site.register(Question)
admin.site.register(Question, QuestionAdmin)
admin.site.register(Choice)
