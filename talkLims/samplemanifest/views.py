__author__ = "Ashok Ragavendran"
__license__ = "GPL"
__version__ = "1.0.1"
__email__ = "ashok.ragavendran@gmail.com"
__maintainer__ = "Ashok Ragavendran"
__status__ = "Production"

import csv

from django.core.urlresolvers import reverse
from django.http import HttpResponse, HttpResponseRedirect
from django.views.decorators.csrf import csrf_exempt
from jinja2 import Environment, FileSystemLoader

from samplemanifest import SampleManifestForm
from talkLims.models import SampleManifest


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
def initiate_manifest(request):
    # if this is a POST request we need to process the form data
    env = environment(loader=FileSystemLoader('/Users/ashok/PycharmProjects/talkLims/templates'))
    if request.method == 'POST':
        print request.FILES.keys()
        # create a form instance and populate it with data from the request:
        outForm = SampleManifestForm(request.POST)
        print outForm
        # check whether it's valid:
        # if outForm.is_valid():
        print "form validates"
        csv_data = upload(request)
        print "print csv data"
        for row in csv_data:
            print row

        outForm_dict = {}
        for item in outForm.cleaned_data.keys():
            outForm_dict[item] = outForm.cleaned_data[item]
        print "print outform_dict"
        print outForm_dict
        ##request.session['outForm'] = outForm.cleaned_data
        request.session['outForm'] = outForm_dict
        request.session['data'] = csv_data
        return HttpResponseRedirect('manifest-verify-form')
        # if a GET (or any other method) we'll create a blank form
    else:
        myForm = SampleManifestForm()
        env = environment(loader=FileSystemLoader('/Users/ashok/PycharmProjects/talkLims/templates'))
        template = env.get_template('startsamplemanifest.html')
        return HttpResponse(template.render(form=myForm))


@csrf_exempt
def manifest_verify(request):
    outForm = request.session.get('outForm')
    data = request.session.get('data')

    env = environment(loader=FileSystemLoader('/Users/ashok/PycharmProjects/talkLims/templates'))
    template1 = env.get_template('samplemanifestverify.html')

    ##print "template value"
    ##print template1.render(formDat=outForm,valDat=data)
    ##print data

    if request.method == 'POST':
        print "completed"
        verify_samples()
        modelmanifest(data, outForm)
        return HttpResponseRedirect('complete-form')
        ##return HttpResponse(render(request,'projectinitiationcomplete.html'))
    else:

        return HttpResponse(template1.render(formDat=outForm, valDat=data))


@csrf_exempt
def manifest_submit_complete(request):
    env = environment(loader=FileSystemLoader('/Users/ashok/PycharmProjects/talkLims/templates'))
    template1 = env.get_template('projectinitiationcomplete.html')
    return HttpResponse(template1.render({'email': 'test.com'}))
    # return HttpResponse('projectinitiationcomplete.html')


def verify_samples(data):
    return


def upload(request):
    key = request.FILES.keys()[0]
    data = csv.DictReader(request.FILES[key])
    list1 = []
    for row in data:
        list1.append(row)
    ##print list1
    return list1


def modelmanifest(indat, project_info):
    for item in indat:
        s = SampleManifest()
        project_id = project_info['project_id']
        sample_id = ''
        sample_name = ''
        sample_replicate = 1
        sample_species = ''
        sample_type = ''
        sample_conc = 0.0
        sample_amount = 0.0
        other = ''
        desc = ''
        for val in item.keys():
            if val != "SampleID" or val != "SampleName":
                other = other + ";" + item[val]
                desc = desc + ";" + val
            elif val == "SampleID":
                sample_id = item[val]
            elif val == "SampleName":
                sample_name = item[val]
            elif val == "Conc":
                sample_conc = float(item[val])
            elif val == "Amount":
                sample_amount = item[val]
            elif val == "Replicate":
                sample_replicate = int(item[val])
            elif val == "SampleType":
                sample_type = item[val]
            elif val == "Species":
                sample_species = item[val]

        s.sample_name = sample_name
        s.sample_id = sample_id
        s.sample_conc = sample_conc
        s.sample_amount = sample_amount
        s.sample_replicate = sample_replicate
        s.sample_type = sample_type
        s.sample_species = sample_species

        s.other = other
        s.desc = desc
        s.save()
    return

    # def readcsv():
    #     pass
    #     return
    #
    # class MyCsvModel(CsvModel):
    #     sample_id = CharField()
    #     sample_name = CharField()
    #     subject_name = CharField()
    #     species = CharField()
    #     ethnicity = CharField()
    #     gender = CharField()
    #     status = CharField()
    #     family_relation = CharField()
    #     phenotype = CharField()
    #     genotype = CharField()
    #     tissue = CharField()
    #     tissue_subType = CharField()
    #     sample_subType = CharField()
    #     number_of_Cells = IntegerField()
    #     conc = FloatField()
    #     amount = FloatField()
    #     soln = FloatField()
    #     date_collected = CharField()
    #     plate_id = CharField()
    #     location = CharField()
    #     shelf = CharField()
    #     rack = CharField()
    #     box = CharField()
    #     grid = CharField()
    #     comments = CharField()
    #
    #
    #     class Meta:
    #         delimiter = ";"
