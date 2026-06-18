def score_stock(market, fund):

    score = 50  # base

    try:
        if fund["pl"] != "N/D" and float(fund["pl"]) < 10:
            score += 15

        if fund["roe"] != "N/D" and float(fund["roe"].replace("%","")) > 15:
            score += 15

        if fund["dy"] != "N/D" and float(fund["dy"].replace("%","")) > 6:
            score += 10

        if fund["pvp"] != "N/D" and float(fund["pvp"]) < 1.5:
            score += 10

    except:
        pass

    return min(score, 100)
