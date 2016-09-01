__author__ = "Ashok Ragavendran"
__license__ = "GPL"
__version__ = "1.0.1"
__email__ = "ashok.ragavendran@gmail.com"
__maintainer__ = "Ashok Ragavendran"
__status__ = "Production"

from django import forms


class PlateSetupUploadForm(forms.Form):
    request_id = forms.CharField(label=" Request ID")
    manifest_file = forms.FileField(label="file for Upload")
