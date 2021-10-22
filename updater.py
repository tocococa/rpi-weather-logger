from bs4 import BeautifulSoup
from datetime import datetime
from collections import deque


def updater(csv_path, html_path):
    try:
        with open(csv_path, 'r', buffering=1, encoding='utf-8') as file:
            qdata = deque(file, 5)
        data = []
        for row in qdata:
            data.append(row.split(','))
    except FileNotFoundError as err:
        print(f"Error: {err}, path CSV incorrecto.")
        return

    try:
        with open(html_path) as inf:
            soup = BeautifulSoup(inf.read(), features="html.parser")
            tables = soup.find_all('table')
            entries = len(data)
            for table in tables:
                rows = table.find_all('tr')
                for i, row in enumerate(rows):
                    cols = row.find_all('td')
                    for ii, elem in enumerate(cols):
                        elem.string.replace_with(data[i][ii])
                    if i == entries - 1:
                        break
            footer = soup.find('footer')
            timestamp = footer.find('pre')
            timestamp.string.replace_with(datetime.now().strftime("%H:%M:%S"))
        with open(html_path, 'w') as outf:
            outf.write(str(soup))
        return
    except FileNotFoundError as err:
        print(f"Error: {err}, path HTML incorrecto.")
        return
