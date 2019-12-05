import selenium
from selenium import webdriver
import calculate
import graphic

# Will scap yahoo finance


class tickerScrapper:
    driver = webdriver.Chrome(executable_path=".//chromedriver")

    def __convertArrayToFloat(self, srcArray):
        i = 0
        while i < len(srcArray):
            srcArray[i] = float(srcArray[i].replace(',', '')) / 10000
            i += 1

    def __scrapDates(self):
        dates = self.driver.find_element_by_css_selector(
            "#Col1-1-Financials-Proxy > section > div:nth-of-type(4) > div > div:nth-of-type(1) > div:nth-of-type(1)").text
        dates = dates[13:]
        dates = [(dates[i:i + 10]) for i in range(0, len(dates), 10)]
        dates.insert(0, 'TTM')
        dates = dates[::-1]
        return dates

    def __scrapRow(self, rows, index):
        res = rows.find_element_by_css_selector(
            f"div:nth-of-type({index})").text.split('\n')
        res = res[1].split(' ')
        self.convertArrayToFloat(res)
        res = res[::-1]
        return res

    # Parse the html to get date, income, revenue and call Calculate class
    # to get growth and profit margin
    def __parser(self):
        try:
            rows = self.driver.find_element_by_css_selector(
                "#Col1-1-Financials-Proxy > section > div:nth-of-type(4) > div > div:nth-of-type(1) > div:nth-of-type(2)")
            dates = self.scrapDates()
            revenue = self.scrapRow(rows, 1)
            income = self.scrapRow(rows, 11)
            calc = calculate.Calculate()
            growth = calc.yearToYearGrowth(revenue)
            profitMargin = calc.profitMargin(revenue, income)
        except Exception as identifier:
            print(f"Error: {str(identifier)}")
            exit()
        plot = graphic.Graphic()
        plot.drawPlot(dates, growth, profitMargin)

    # Check if the ticker exist, if yes, call parser method
    def tickersExist(self, ticker):
        try:
            self.driver.get(
                "https://finance.yahoo.com/quote/" + ticker + "/financials")
            if "quote" not in self.driver.current_url:
                print(f"Tickers {ticker} does not exist")
                exit()
        except Exception as e:
            print("Request have failed: " + str(e))
            exit()
        self.parser()
