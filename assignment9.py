import tickerScrapper


class main:
    tickers = ""

    def __init__(self):
        self.tickers = input(">> Enter a tickers: \n")
        ticker = tickerScrapper.tickerScrapper()
        ticker.tickersExist(self.tickers)


main = main()
