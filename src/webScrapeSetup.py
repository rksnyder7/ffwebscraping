from requests import get
from requests.exceptions import RequestException
from contextlib import closing
from bs4 import BeautifulSoup

def simple_get(url):
    """
    Attempts to get the content at `url` by making an HTTP GET request.
    If the content-type of response is some kind of HTML/XML, return the
    text content, otherwise return None
    """
    try:
        with closing(get(url, stream=True)) as resp:
            if is_good_response(resp):
                return resp.content
            else:
                return None

    except RequestException as e:
        log_error('Error during requests to {0} : {1}'.format(url, str(e)))
        return None


def is_good_response(resp):
    """
    Returns true if the response seems to be HTML, false otherwise
    """
    content_type = resp.headers['Content-Type'].lower()
    return (resp.status_code == 200 
            and content_type is not None 
            and content_type.find('html') > -1)


def log_error(e):
    """
    It is always a good idea to log errors. 
    This function just prints them, but you can
    make it do anything.
    """
    print(e)



# raw_html = simple_get('https://fantasyfootballcalculator.com/rankings/ppr/quarterback')

# Html_file=open("fantasyfootballcalculator.html", "wb")
# Html_file.write(raw_html)
# Html_file.close()

# raw_html =open('fantasyfootballcalculator.html').read()
# html = BeautifulSoup(raw_html, 'html.parser')
# print(html)
# Html_file=open("quarterbacksFromFFC.html", "w")
# for tr in html.select('tr.QB'):
# 	hold = 0
# 	for td in tr:
# 		if hold == 3:
# 			Html_file.write('<td>' + td.text + '</td>' + '\n')
# 			print(td.text)
# 			break
# 		hold += 1

# Html_file.close()
