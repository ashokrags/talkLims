__author__ = "Ashok Ragavendran"
__license__ = "GPL"
__version__ = "1.0.1"
__email__ = "ashok.ragavendran@gmail.com"
__maintainer__ = "Ashok Ragavendran"
__status__ = "Production"

import time

from django import forms


class PlatesetupDownloadForm(forms.Form):
    request_id = forms.CharField(widget=forms.Textarea(), label='Request ID')
    plate_name = forms.CharField(label="Plate Name")
    plate_id = forms.CharField(initial="Plt_" + str(int(time.time())), label=" Auto generated Plate ID", disabled=True)

## Boiler plate cod

# textarea = forms.CharField(
#         widget = forms.Textarea(),
#     )
#
#     radio_buttons = forms.ChoiceField(
#         choices = (
#             ('option_one', "Option one is this and that be sure to include why it's great"),
#             ('option_two', "Option two can is something else and selecting it will deselect option one")
#         ),
#         widget = forms.RadioSelect,
#         initial = 'option_two',
#     )
#
#     checkboxes = forms.MultipleChoiceField(
#         choices = (
#             ('option_one', "Option one is this and that be sure to include why it's great"),
#             ('option_two', 'Option two can also be checked and included in form results'),
#             ('option_three', 'Option three can yes, you guessed it also be checked and included in form results')
#         ),
#         initial = 'option_one',
#         widget = forms.CheckboxSelectMultiple,
#         help_text = "<strong>Note:</strong> Labels surround all the options for much larger click areas and a more usable form.",
#     )
#
#     appended_text = forms.CharField(
#         help_text = "Here's more help text"
#     )
#
#     prepended_text = forms.CharField()
#
#     prepended_text_two = forms.CharField()
#
#     multicolon_select = forms.MultipleChoiceField(
#         choices = (('1', '1'), ('2', '2'), ('3', '3'), ('4', '4'), ('5', '5')),
#     )
