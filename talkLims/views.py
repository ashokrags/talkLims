__author__ = "Ashok Ragavendran"
__license__ = "GPL"
__version__ = "1.0.1"
__email__ = "ashok.ragavendran@gmail.com"
__maintainer__ = "Ashok Ragavendran"
__status__ = "Production"

from django.http import HttpResponse
from jinja2 import FileSystemLoader

from talkLims.settings import TEMPLATE_DIRS
from talkLims.utils.jinja2config import environment


def navpage(request):
    env = environment(loader=FileSystemLoader(TEMPLATE_DIRS))
    template = env.get_template('base.html')
    return HttpResponse(template.render())
