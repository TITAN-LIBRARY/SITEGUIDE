import datetime


def get_data(request):
    current_datetime = datetime.datetime.now()
    website_url = 'http://127.0.0.1:8000/'
    context = {
        'current_year': current_datetime.year,
        'business_mail': 'business@siteguide.co.in',
        'website_url': 'http://127.0.0.1:8000/',
        'calendly_link': 'https://calendly.com/diwakarmandal/success-call-with-diwakar',
        'logo': f"{website_url}static/images/logo/SG-logo.png",
    }
    return context


