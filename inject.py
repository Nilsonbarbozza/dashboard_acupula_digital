from bs4 import BeautifulSoup

html_path = r'c:\Users\Ti\Desktop\dashboard_acupula_digital\clientes.html'
try:
    with open(html_path, 'r', encoding='utf-8') as f:
        html = f.read()

    soup = BeautifulSoup(html, 'html.parser')
    rows = soup.find_all('tr', class_='sail-table-row')
    i = 1
    for row in rows[:12]:
        tds = row.find_all('td')
        if len(tds) > 1:
            name_span = tds[1].find('span')
            if name_span:
                name_span['id'] = f'clientName{i}'
        
        if len(tds) > 3:
            email_span = tds[3].find('span')
            if email_span:
                 email_span = email_span.find('span') or email_span # it's nested
                 email_span['id'] = f'clientEmail{i}'
        i += 1

    with open(html_path, 'w', encoding='utf-8') as f:
        f.write(str(soup))
        
    print("Injected correctly")
except ImportError:
    print("Please install beautifulsoup4")
