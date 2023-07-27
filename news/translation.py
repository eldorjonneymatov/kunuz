from modeltranslation.translator import translator, TranslationOptions
from .models import TextNewsModel

class NewsTranslationOptions(TranslationOptions):
    fields = (
            'created_at',
            'updated_at',
            'title',
            'view_count',
            'author',
            'category',
            'region',
            'cover_img',
            'body'
        )

translator.register(TextNewsModel, NewsTranslationOptions)