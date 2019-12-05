class Calculate:
    def yearToYearGrowth(self, revenue):
        i = 1
        growth = []
        while i < len(revenue):
            growth.append(
                ((revenue[i] - revenue[i - 1]) / revenue[i - 1]) * 100)
            i += 1
        return growth

    def profitMargin(self, revenue, income):
        i = 0
        profit = []
        while i < len(revenue):
            profit.append((income[i] / revenue[i]) * 100)
            i += 1
        return profit
