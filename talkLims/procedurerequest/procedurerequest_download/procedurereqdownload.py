__author__ = "Ashok Ragavendran"
__license__ = "GPL"
__version__ = "1.0.1"
__email__ = "ashok.ragavendran@gmail.com"
__maintainer__ = "Ashok Ragavendran"
__status__ = "Production"

import time

from django import forms


##from talkLims.settings import EXCELFILES_FOLDER

class ProcedureRequestDownloadForm(forms.Form):
    project_name = forms.CharField(label='Project Name', max_length=100)
    project_id = forms.CharField(label=" Project ID")
    project_driver = forms.CharField(label='Project Driver')
    driver_email = forms.EmailField(label='Contact Email')
    protocol_type = forms.CharField(label="Protocol Type")  # drop down box eventually
    request_id = forms.CharField(initial="Req_" + str(int(time.time())), label=" Auto generated GTC Request ID",
                                 disabled=True)
    project_archivist = forms.CharField(label='Archivist')
    requested_by = forms.CharField(label='Requested by')
    request_date = forms.CharField(label='Request Date')
    expected_end_date = forms.CharField(label='Expected Completion Date')
    quote_number = forms.CharField(label='Quote #')
    number_of_samples = forms.IntegerField(label='Number of Samples')
    number_of_reads = forms.CharField(label="Number of Reads Requested (in Millions)")
    sample_amount = forms.CharField(label="Amount Required")
    sample_volume = forms.CharField(label="Volume Required")

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
