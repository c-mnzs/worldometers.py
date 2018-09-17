from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


class Worldometers():
    url = 'https://countrymeters.info/en/World'
    
    chrome_options = Options()
    chrome_options.add_argument("--disable-extensions")
    chrome_options.add_argument('headless')
    browser = webdriver.Chrome(chrome_options=chrome_options)
    browser.get(url)
    html = browser.page_source
    soup = BeautifulSoup(html, 'lxml')

    # World Population
    def current_world_population(self, option = 'total'):
        """
        Parses through the HTML page to gather information about the current world population.

        :param option: Choose between three types of return values. 'total', the default value for this parameter, returns the total world population. 'male' and 'female' returns the current population for each gender.
        :return: Integer with the current population.
        """
        if option.lower() == 'total':
            return int(Worldometers.soup.find(id='cp1').getText().replace(',', ''))
        
        elif option.lower() == 'male':
            return int(Worldometers.soup.find(id='cp2').getText().replace(',', ''))
        
        elif option.lower() == 'female':
            return int(Worldometers.soup.find(id='cp3').getText().replace(',', ''))

    # Births
    def births(self, timescale):
        """
        Parses through the HTML page to gather information about births.

        :param timescale: Choose between two types — 'day' or 'year' — that will return results accordingly.
        :return: Integer with the number of births.
        """
        if timescale.lower() == 'year':
            return int(Worldometers.soup.find(id='cp6').getText().replace(',', ''))

        if timescale.lower() == 'day':
            return int(Worldometers.soup.find(id='cp7').getText().replace(',', ''))

    # Deaths
    def deaths(self, timescale):
        """
        Parses through the HTML page to gather information about deaths.

        :param timescale: Choose between two types — 'day' or 'year' — that will return results accordingly.
        :return: Integer with the number of deaths.
        """
        if timescale.lower() == 'year':
            return int(Worldometers.soup.find(id='cp8').getText().replace(',', ''))

        if timescale.lower() == 'day':
            return int(Worldometers.soup.find(id='cp9').getText().replace(',', ''))

test = Worldometers().deaths(timescale='year')
print(test)
