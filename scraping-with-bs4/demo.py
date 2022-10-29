import requests
from bs4 import BeautifulSoup



class Wikipedia:
    def __init__(self, filter) -> None:
        self.filter_str = filter

    def get_data(self):
        url = f"https://en.wikipedia.org/wiki/{self.filter_str}"
        
        res = requests.get(url)
        # create the soup
        soup = BeautifulSoup(res.content, 'html.parser')

        main_table =  soup.find("table", attrs={"class": 'infobox'})
        if main_table is None:
            return{"error": "Main table is not found which have data."}
        
        result = {}
        for row in main_table.findAll('tr'):
            th = row.find('th')
            td = row.find("td")
            if th is not None and td is not None:
                result[str(th.text)] = td.text

        print(result)
        # print(res)
        return result
