__author__ = "Ashok Ragavendran"
__license__ = "GPL"
__version__ = "1.0.1"
__email__ = "ashok.ragavendran@gmail.com"
__maintainer__ = "Ashok Ragavendran"
__status__ = "Production"

from django import forms


class SampleManifestForm(forms.Form):
    project_id = forms.CharField(label='Project ID', max_length=100)
    # project_driver = forms.CharField(label='Project Driver')
    # project_ext_contact_name= 	forms.CharField(label='Project Ext. Name')
    # project_ext_contact_email = forms.CharField(label='Project Ext. Contact Email')
    # project_ext_contact_phone = forms.CharField(label='Project Ext. Contact Phone')
    # project_ext_contact_fax = forms.CharField(label='Project Ext. Contact Fax')
    # expected_start_date = forms.CharField(label='Expectd Start Date')
    # expected_end_date = forms.CharField(label='Expected End Date')
    # project_description = forms.CharField(widget = forms.Textarea(), label='Project Description ')
    manifest_file = forms.FileField(label="file for Upload")
