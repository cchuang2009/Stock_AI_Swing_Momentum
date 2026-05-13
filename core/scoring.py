
def calculate_score(row):
    return round(
        0.3 * row["RVOL"] +
        0.25 * row["Momentum"] +
        0.2 * row["NewsScore"] +
        0.15 * row["ShortInterest"] +
        0.1 * row["OptionsFlow"],
        2
    )
