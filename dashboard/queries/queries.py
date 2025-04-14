def most_sunked_ships():
    return """
    SELECT 
        EfficiencyPerBoat.UboatName, 
        SummaryUboats.TypeOfUboat, 
        EfficiencyPerBoat.TotalShipsSunked,
        UboatsRaw.Wikipedia
    FROM EfficiencyPerBoat
    JOIN SummaryUboats
    ON EfficiencyPerBoat.UboatName = SummaryUboats.UboatName
    JOIN UboatsRaw
    ON EfficiencyPerBoat.UboatName = UboatsRaw.Name
    ORDER BY EfficiencyPerBoat.TotalShipsSunked DESC
    """

def effective_boats():
    return """
    SELECT 
        SummaryUboats.UboatName, 
        TypeOfUboat, 
        EfficiencyPerBoat.TotalShipsSunked,
        DaysInService,
        AverageDayPerShip,
        UboatsRaw.Wikipedia
    FROM SummaryUboats
    JOIN EfficiencyPerBoat
    ON SummaryUboats.UboatName = EfficiencyPerBoat.UboatName
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