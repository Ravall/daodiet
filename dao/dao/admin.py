from articles.forms import ArticleAdminForm
from articles.models import Article
from articles.admin import ArticleAdmin
from django.contrib import admin
from markitup.widgets import AdminMarkItUpWidget
from django.db import models

class ArticleAdminForm(ArticleAdminForm):
    class Media:
        css = {
            'all': ('/static/css/jquery.autocomplete.css',),
        }
        js = (
            '/static/js/jquery-1.4.1.min.js',
            '/static/js/jquery.bgiframe.min.js',
            '/static/js/jquery.autocomplete.pack.js',
            '/static/js/tag_autocomplete.js',
        )

#class Article(Article):
#     content = forms.CharField(widget=MarkItUpWidget())


class ArticleAdmin(ArticleAdmin):
    #formfield_overrides = {
    #    models.TextField: {'widget': AdminMarkItUpWidget}
    #}
    form = ArticleAdminForm


    def formfield_for_dbfield(self, db_field, **kwargs):
        if db_field.name == 'content':
            kwargs['widget'] = AdminMarkItUpWidget()
        return super(ArticleAdmin, self).formfield_for_dbfield(db_field, **kwargs)



admin.site.unregister(Article)
admin.site.register(Article, ArticleAdmin)