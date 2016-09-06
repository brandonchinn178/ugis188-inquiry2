from django.views.generic import TemplateView

class MainView(TemplateView):
    """
    The main view that tracks users by their cookies and renders the same
    template to them consistently.
    """
    template_name = 'survey.html'
