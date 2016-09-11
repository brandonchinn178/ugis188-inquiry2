from django.views.generic import FormView
from django.shortcuts import redirect

import random

from base.forms import SurveyForm

class MainView(FormView):
    """
    The main view that tracks users by their cookies and renders the same
    template to them consistently.
    """
    form_class = SurveyForm

    def dispatch(self, request, *args, **kwargs):
        """
        Try to get the version from the session, falling back on the cookie
        if the session has expired. Sets the session and cookie afterwards.
        """
        self.version = request.session.get('version', request.COOKIES.get('version'))
        if self.version is None:
            self.version = random.randint(1, 4)
        request.session['version'] = self.version

        # same UIs use same template
        template_version = (self.version + 1) / 2
        self.template_name = 'survey-%d.html' % template_version

        response = super(MainView, self).dispatch(request, *args, **kwargs)
        response.set_cookie('version', self.version)
        return response

    def get_context_data(self, **kwargs):
        context = super(MainView, self).get_context_data(**kwargs)

        # 1 and 2: 'base-1.css'
        # 3 and 4: 'base-2.css'
        context['base_style'] = 'base-%d.css' % self.template_version

        # 2: 'style-1.css'
        # 4: 'style-2.css'
        context['design_style'] = 'style-%d.css' % self.template_version

        context['good_design'] = self.version in [2, 4]

        return context

    def form_valid(self, form):
        form.save(self.version)
        return redirect('submitted')

class SubmittedView(TemplateView):
    """
    The view to display after finishing a survey.
    """
    def dispatch(self, request, *args, **kwargs):
        try:
            self.version = request.session['version']
        except KeyError:
            return redirect('home')

        template_version = (self.version + 1) / 2
        self.template_name = 'submitted-%d.html' % template_version

    def get_context_data(self, **kwargs):
        context = super(SubmittedView, self).get_context_data(**kwargs)

        context['messages'] = [
            'Your survey has been successfully submitted!',
            'Thank you for your participation.',
        ]

        return context
