from django.views.generic import FormView, TemplateView
from django.shortcuts import redirect

import random

from base.forms import SurveyForm
from base.models import MEMES

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
        # never let a user resubmit a form, to prevent against multiple people
        # filling out a survey on one computer and unproportionally increasing
        # the number of survey responses for that design
        if request.session.get('submitted'):
            #### DEBUGGING: TAKE OUT LATER ####
            pass
            ###################################
            # return redirect('submitted')

        self.version = request.session.get('version', request.COOKIES.get('version'))
        if self.version is None:
            self.version = random.randint(1, 4)
        request.session['version'] = self.version

        #### DEBUGGING: TAKE OUT LATER ####
        if 'version' in kwargs:
            self.version = int(kwargs['version'])
        ###################################

        # same UIs use same template
        self.template_version = (self.version + 1) / 2
        self.template_name = 'survey-%d.html' % self.template_version

        response = super(MainView, self).dispatch(request, *args, **kwargs)
        response.set_cookie('version', self.version)
        return response

    def get_context_data(self, **kwargs):
        context = super(MainView, self).get_context_data(**kwargs)

        # randomize order of memes
        memes = [
            (slug, 'img/memes/%s.jpg' % slug)
            for slug in MEMES
        ]
        random.shuffle(memes)
        context['memes'] = memes

        # 1 and 2: 'base-1.css'
        # 3 and 4: 'base-2.css'
        context['base_style'] = 'base-%d.css' % self.template_version

        # 2: 'style-1.css'
        # 4: 'style-2.css'
        context['design_style'] = 'style-%d.css' % self.template_version

        context['good_design'] = self.version in [2, 4]

        return context

    def form_valid(self, form):
        """
        Parse out mock survey data and save the MockSurvey object. Each meme's data
        comes in the keys "meme-<slug>-funny" and "meme-<slug>-match".
        """
        data = {
            slug: {
                'funny': int(self.request.POST['meme-%s-funny' % slug]),
                'match': int(self.request.POST['meme-%s-match' % slug]),
            }
            for slug in MEMES
        }
        form.save(self.version, data)
        self.request.session['submitted'] = True
        return redirect('submitted')

    def form_invalid(self, form):
        print form.errors.as_data()
        raise Exception('Survey had errors: see console for more details.')

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

        return super(SubmittedView, self).dispatch(request, *args, **kwargs)
