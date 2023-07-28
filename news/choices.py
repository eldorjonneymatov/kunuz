from django.db.models import TextChoices
from django.utils.translation import gettext_lazy as _

class Regions(TextChoices):
    CAPITAL = 'tashkent-city', _("Tashkent city")
    TASHKENT = 'tashkent-reg', _("Tashkent region")
    KARAKALPAKSTAN = 'karakalpakstan', _("Karakalpakstan")
    ANDIJAN = 'andijan', _("Andijan")
    FERGANA = 'fergana', _("Fergana")
    NAMANGAN = 'namangan', _("Namangan")
    SAMARKAND = 'samarkand', _("Samarkand")
    BUKHARA = 'bukhara', _("Bukhara")
    KHORAZM = 'khorazm', _("Khorazm")
    SURKHANDARYA = 'surkhandarya', _("Surkhandarya")
    KASHKADARYA = 'kashkadarya', _("Kashkadarya")
    JIZZAKH = 'jizzakh', _("Jizzakh")
    SIRDARYA = 'sirdarya', _("Sirdarya")
    NAVOI = 'navoi', _("Navoi")
    OTHER = 'other', _("Other")


class Categories(TextChoices):
    UZBEKISTAN = 'uzbekistan', _('UZBEKISTAN')
    WORLD = 'world', _('WORLD')
    FINANCE = 'finance', _('FINANCE')
    SOCIETY = 'society', _('SOCIETY')
    SCIENCE = 'science-techno', _('SCIENCE-TECHNOLOGY')
    SPORTS = 'sport', _("SPORTS")
    VIEW = 'point-of-view', _("POINT OF VIEW")
    ADVERTISEMENT = 'ad', _("ADVERTISEMENT")