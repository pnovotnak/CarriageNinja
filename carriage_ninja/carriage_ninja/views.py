from django.views.generic import TemplateView

class HomeView(TemplateView):
    template_name = "home.html"

class FAQView(TemplateView):
    template_name = "faq.html"
