__author__ = "Ashok Ragavendran"
__license__ = "GPL"
__version__ = "1.0.1"
__email__ = "ashok.ragavendran@gmail.com"
__maintainer__ = "Ashok Ragavendran"
__status__ = "Production"

from django import forms


class PoolingDownloadForm(forms.Form):
    request_id = forms.CharField(max_length=100, label='Request ID')
    plate_id = forms.CharField(max_length=100, label="Plate ID")
