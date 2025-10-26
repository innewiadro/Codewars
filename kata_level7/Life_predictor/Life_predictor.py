from datetime import datetime, timedelta


def life_predictor(date):
    x = datetime.strptime(date, "%Y-%m-%d")
    result = x - timedelta(days=280)
    return result.strftime("%Y-%m-%d")
