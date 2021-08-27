from bs4 import BeautifulSoup
from datetime import datetime
import csv
# Update HTML file when logger gets new data


def updater(csv_path, html_path):
    data = []
    try:
        with open(csv_path, 'r', encoding='utf-8') as file:
            reader = csv.reader(file, delimiter=',')
            for i in range(-1, -5, -1):
                data.append(reader[i])
    except FileNotFoundError as err:
        print(f"Error: {err}, path CSV incorrecto.")
        return

    try:
        with open(html_path) as inf:
            soup = BeautifulSoup(inf.read())
            table = soup.find('table')
            first = False
            readings = 0
            while(row := table.find_next('tr')):
                if not first:
                    first = True
                else:
                    cols = row.find_all('td')
                    i = 0
                    for elem in cols:
                        elem.string.replace_with(data[readings][i])
                        i += 1
                    readings += 1
            footer = soup.find('footer')
            timestamp = footer.find('pre')
            timestamp.string.replace_with(datetime.now().strftime("%H:%M:%S"))
        return
    except FileNotFoundError as err:
        print(f"Error: {err}, path HTML incorrecto.")
        return
