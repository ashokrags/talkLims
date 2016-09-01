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

from talkLims.models import ProjectInfo
##from talkLims.projectinitiation import InitiationForm
from talkLims.initiateproject.projectinitiation import InitiationForm


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
def initiate_project(request):
    # if this is a POST request we need to process the form data
    env = environment(loader=FileSystemLoader('/Users/ashok/PycharmProjects/talkLims/templates'))
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        outForm = InitiationForm(request.POST)
        # check whether it's valid:
        if outForm.is_valid():

            ##print outForm.cleaned_data
            # process the data in form.cleaned_data as required
            # ...
            # redirect to a new URL:
            outForm_dict = {}
            for item in outForm.cleaned_data.keys():
                ##print item
                outForm_dict[item] = outForm.cleaned_data[item]

            print outForm_dict
            request.session['outForm'] = outForm.cleaned_data
            ##url = project_initiation_verify(request, outForm_dict)
            ##return HttpResponse(url)
            return HttpResponseRedirect('verify-form')
            # if a GET (or any other method) we'll create a blank form
    else:
        myForm = InitiationForm()
        env = environment(loader=FileSystemLoader('/Users/ashok/PycharmProjects/talkLims/templates'))
        template = env.get_template('projectinitiation.html')
        return HttpResponse(template.render(form=myForm))


@csrf_exempt
def project_initiation_verify(request):
    outForm = request.session.get('outForm')
    env = environment(loader=FileSystemLoader('/Users/ashok/PycharmProjects/talkLims/templates'))
    template1 = env.get_template('projectinitiationverify.html')
    ##print "template value"
    ##print template1.render(context=outForm)
    if request.method == 'POST':
        ##print "completed"
        insert_project_vals(outForm)
        env = environment(loader=FileSystemLoader('/Users/ashok/PycharmProjects/talkLims/templates'))
        template1 = env.get_template('projectinitiationcomplete.html')
        return HttpResponse(template1.render(email="test@com"))
    else:
        return HttpResponse(template1.render(context=outForm))


@csrf_exempt
def project_initiation_complete(request):
    if request.method == "POST":
        env = environment(loader=FileSystemLoader('/Users/ashok/PycharmProjects/talkLims/templates'))
        template1 = env.get_template('projectinitiationcomplete.html')
        print "complete form view"
        print template1.render(email="test@com")
        return HttpResponse(template1.render(email="test@com"))
    else:
        return HttpResponseRedirect('startup')


def insert_project_vals(form_data):
    p = ProjectInfo(**form_data)
    # p.project_name = form_data['project_name']
    # p.project_initiation_complet = forms.CharField(initial="talklab_prj_" + str(int(time.time())), label=" Auto generated Project ID", disabled=True)
    # p.project_driver = forms.CharField(label='Project Driver')
    # p.project_ext_contact_name= 	forms.CharField(label='Project Ext. Name')
    # p.project_ext_contact_email = forms.CharField(label='Project Ext. Contact Email')
    # p.project_ext_contact_phone = forms.CharField(label='Project Ext. Contact Phone')
    # pproject_ext_contact_fax = forms.CharField(label='Project Ext. Contact Fax')
    # expected_start_date = forms.CharField(label='Expectd Start Date')
    # expected_end_date = forms.CharField(label='Expected End Date')
    # project_description = forms.CharField(widget = forms.Textarea(), label='Project Description ')
    p.save()
    return
