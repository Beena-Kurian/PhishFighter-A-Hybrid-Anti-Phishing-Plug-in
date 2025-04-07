key_words = {
    "PayPal username": 2,
    "PayPal password": 2,
    "1999 - 2013 PayPal": 2,
    "1999-2013 PayPal": 2,
    "1999 - 2013 PayPal.": 2,
    "1999-2013 PayPal.": 2,
    "1999-2014 PayPal": 2,
    "1999 - 2014 PayPal": 2,
    "1999-2014 PayPal.": 2,
    "1999 - 2014 PayPal.": 2,
    "ATM pin": 2,
    "Credit Card Number": 2,
    "3D Secure Password": 2,
    "Card Type": 2,
    "Card Number": 2,
    "Expiration Date": 2,
    "Card Verification Number": 2,
    "Cardholder Name": 2,
    "Cardholder's Name": 2,
    "Name on Card": 2,
    "2014 Apple Inc" : 2,
    "2014 Apple Inc." : 2,
    "My Apple ID": 2,
    "view and edit your Apple ID": 2,
    "Sign in  - Apple Store": 2,
}

def has_match(text, url):
    try:
        has_https = url.startswith("https")
        count = 0
        text = text.lower()
	for word in key_words:
            if text.find(word.lower()) > -1:
                count += key_words[word]
		
		if (count >= 2) and has_https is False:
          	    print "textual weight = ",count   
		    print "URL Scheme used is not https"   	    
                    return True
  	print "Textual Weight = ",count
        return False 

    except Exception, dt:
        print dt
