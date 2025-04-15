def most_sunked_ships():
    return """
    SELECT 
        EfficiencyPerUboat.UboatName, 
        SummaryUboats.TypeOfUboat, 
        EfficiencyPerUboat.TotalShipsSunked,
        UboatsRaw.Wikipedia
    FROM EfficiencyPerUboat
    JOIN SummaryUboats
    ON EfficiencyPerUboat.UboatName = SummaryUboats.UboatName
    JOIN UboatsRaw
    ON EfficiencyPerUboat.UboatName = UboatsRaw.Name
    ORDER BY EfficiencyPerUboat.TotalShipsSunked DESC
    """

def effective_boats():
    return """
    SELECT 
        SummaryUboats.UboatName, 
        TypeOfUboat, 
        EfficiencyPerUboat.TotalShipsSunked,
        DaysInService,
        AverageDayPerShip,
        UboatsRaw.Wikipedia
    FROM SummaryUboats
    JOIN EfficiencyPerUboat
    ON SummaryUboats.UboatName = EfficiencyPerUboat.UboatName
    JOIN UboatsRaw
    ON SummaryUboats.UboatName = UboatsRaw.Name
    ORDER BY AverageDayPerShip
    """

def longest_serving_time():
    return """
    SELECT
        SummaryUboats.UboatName,
        SummaryUboats.TypeOfUboat,
        SummaryUboats.Commissioned,
        SummaryUboats.FateDate,
        SummaryUboats.Fate,
        SummaryUboats.DaysInService,
        UboatsRaw.Wikipedia
    FROM SummaryUboats
    JOIN UboatsRaw
    ON SummaryUboats.UboatName = UboatsRaw.Name
    ORDER BY DaysInService DESC
    """