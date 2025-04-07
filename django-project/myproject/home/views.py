import os
import re

from django.http import HttpResponse
from django.conf import settings
from django.utils.timezone import now

from emd import compare_images
from textual import has_match



def save_image(request):
    path = os.path.join(settings.BASE_DIR, str(now())) + ".jpg"
    original = os.path.join(settings.BASE_DIR, 'apple-login.jpg')
    originalp = os.path.join(settings.BASE_DIR, 'paypal-login.jpg')
    data_uri = request.REQUEST['file']
    text = request.REQUEST['text']
    url = request.REQUEST['url']
    print "------------------------------PHASE III-Checking Results----------------------------------"
    print "URL of loaded page=  ",url
    if has_match(text, url):
	print "Textually Similar webpage-------------------->PHISHING ATTACK"
    	return HttpResponse('true')
    img_str = re.search(r'base64,(.*)', data_uri).group(1)
    output = open(path, 'wb')
    output.write(img_str.decode('base64'))
    output.close()
   

   
    diff = 999

    try:
        diff = compare_images(original, path)
        diffp = compare_images(originalp, path)
        print "------------------------Calculating Image Difference----------------------"
        print "Difference towards Apple =",diff
        print "Difference towards PayPal=",diffp
    except Exception, dt:
        print dt
    print "----------------Base 64 Encoded String of Screenshot---------------------"
    #os.unlink(path)
    if diff <= 0.2 or diffp <= 0.2:
	print "Visually Similar webpage-------------------->PHISHING ATTACK"
        return HttpResponse('true')

    #if diff > 0.1 or diffp > 0.1:
    	
    return HttpResponse('false')
