__author__ = "Ashok Ragavendran"
__license__ = "GPL"
__version__ = "1.0.1"
__email__ = "ashok.ragavendran@gmail.com"
__maintainer__ = "Ashok Ragavendran"
__status__ = "Production"

from django.core.urlresolvers import reverse
from django.http import HttpResponse, HttpResponseRedirect
from django.views.decorators.csrf import csrf_exempt
from jinja2 import Environment, FileSystemLoader
##from talkLims.projectinitiation import InitiationForm
from talkLims.rnaseqsubmission.rnaseqsubmission import RequestForm
from talkLims.models import ProjectInfo
import datetime


def environment(**options):
    env = Environment(**options)
    env.globals.update({
        ##'static': staticfiles_storage.url,
        ##'static': "file://Users/ashok//Documents/Research/CHGR/CSSForR/bootstrap-3.3.5-dist/css/bootstrap.min.cyborg.css",
        'static': "https://maxcdn.bootstrapcdn.com/bootswatch/3.3.7/slate/bootstrap.min.css",
        ##'static': "https://maxcdn.bootstrapcdn.com/bootswatch/3.3.7/bootstrap.min.css",
        'url': reverse,
    })
    return env


@csrf_exempt
def initiate_request(request):
    # if this is a POST request we need to process the form data
    env = environment(loader=FileSystemLoader('/Users/ashok/PycharmProjects/talkLims/templates'))
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        outForm = RequestForm(request.POST)
        # check whether it's valid:
        if outForm.is_valid():

            ##print outForm.cleaned_data
            # process the data in form.cleaned_data as required
            # ...
            # redirect to a new URL:
            outForm_dict = {}
            for item in outForm.cleaned_data.keys():
                if type(outForm.cleaned_data[item]) is not datetime.date:
                    outForm_dict[item] = outForm.cleaned_data[item]

            p = ProjectInfo.objects.filter(project_id=str(outForm_dict['project_id'])).values()[0]

            for k in p.keys():
                if type(p[k]) is not datetime.date and k not in outForm_dict.keys():
                    outForm_dict[k] = p[k]

            print "final dict"
            print outForm_dict
            request.session['outForm'] = outForm_dict
            ##url = project_initiation_verify(request, outForm_dict)
            ##return HttpResponse(url)
            return HttpResponseRedirect('verify-request-form')
            # if a GET (or any other method) we'll create a blank form
    else:
        myForm = RequestForm()
        env = environment(loader=FileSystemLoader('/Users/ashok/PycharmProjects/talkLims/templates'))
        template = env.get_template('rnaseqsubmission_init.html')
        return HttpResponse(template.render(form=myForm))


@csrf_exempt
def pull_request_verify(request):
    outForm = request.session.get('outForm')
    env = environment(loader=FileSystemLoader('/Users/ashok/PycharmProjects/talkLims/templates'))
    template1 = env.get_template('rnaseqsubmission_verify.html')
    ##print "template value"
    ##print template1.render(context=outForm)
    if request.method == 'POST':
        ##insert_request_vals(outForm)
        env = environment(loader=FileSystemLoader('/Users/ashok/PycharmProjects/talkLims/templates'))
        template1 = env.get_template('projectinitiationcomplete.html')
        return HttpResponse(template1.render(email="test@com"))
    else:
        return HttpResponse(template1.render(context=outForm))


def verify_sample_id():
    ## when sample Ids submitted in form
    ## Verify if project ID matches
    ## Verify if sample exists
    ## Verify number of samples requested and number of sample ids submitted the same
    return


def insert_request_vals(form_data):
    p = PullRequest(**form_data)
    p.save()
    return
