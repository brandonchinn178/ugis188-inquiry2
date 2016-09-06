from django.views.generic import FormView

import random

from base.forms import SurveyForm

class MainView(FormView):
    """
    The main view that tracks users by their cookies and renders the same
    template to them consistently.
    """
    template_name = 'survey.html'
    form_class = SurveyForm

    def dispatch(self, request, *args, **kwargs):
        """
        Try to get the version from the session, falling back on the cookie
        if the session has expired. Sets the session and cookie afterwards.
        """
        version = request.session.get('version', request.COOKIES.get('version'))
        if version is None:
            version = random.randint(1, 4)
        request.session['version'] = version

        response = super(MainView, self).dispatch(request, *args, **kwargs)
        response.set_cookie('version', version)
        return response

    def get_context_data(self, **kwargs):
        context = super(MainView, self).get_context_data(**kwargs)
        context['version'] = request.session['version']
        return context
