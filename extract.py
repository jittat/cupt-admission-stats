import sys
from bs4 import BeautifulSoup
import requests

BASE_URL = 'http://admission.cuas.or.th/%s/toppage.html'
MAJOR_URL = 'http://admission.cuas.or.th/%s/search_fac.php?q='

def extract_options(html):
    html.encoding = 'tis-620'
    soup = BeautifulSoup(html.text, 'html.parser')
    return soup.find('select').find_all('option')

def extract_major_name(str):
    items = str.split()
    return ' '.join(items[1:])

def main():
    if len(sys.argv) != 2:
        year_prefix = 'adm60maxmn'
    else:
        year_prefix = sys.argv[1]

    main_url = BASE_URL % (year_prefix,)
        
    html = requests.get(main_url)
    for opt in extract_options(html):
        uname = opt.text.strip()
        unumber = opt.attrs['value']

        if unumber == '000':
            continue
        
        major_query_url = (MAJOR_URL % (year_prefix,)) + unumber

        major_html = requests.get(major_query_url)
        majors = extract_options(major_html)
        for m in majors:
            mname = extract_major_name(m.text.strip())
            mnumber = m.attrs['value']

            if mnumber == '0000':
                continue

            items = [mnumber, mname, unumber, uname]
            print(','.join(['"%s"' % s for s in items]))


if __name__=='__main__':
    main()

    
