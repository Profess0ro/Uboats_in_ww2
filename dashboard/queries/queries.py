# Query to find the U-boats with the most ships sunk
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


# Query to find the most effective U-boats based on average days per ship sunk
def effective_boats():
    return """
    SELECT 
        SummaryUboats.UboatName, 
        SummaryUboats.TypeOfUboat, 
        EfficiencyPerUboat.TotalShipsSunked,
        SummaryUboats.Days_in_service,
        AverageDayPerShip,
        UboatsRaw.Wikipedia
    FROM SummaryUboats
    JOIN EfficiencyPerUboat
    ON SummaryUboats.UboatName = EfficiencyPerUboat.UboatName
    JOIN UboatsRaw
    ON SummaryUboats.UboatName = UboatsRaw.Name
    ORDER BY AverageDayPerShip
    """


# Query to find the U-boats with the longest service time
def longest_serving_time():
    return """
    SELECT
        SummaryUboats.UboatName,
        SummaryUboats.TypeOfUboat,
        SummaryUboats.Commissioned,
        SummaryUboats.FateDate,
        SummaryUboats.Fate,
        SummaryUboats.Days_in_service,
        UboatsRaw.Wikipedia
    FROM SummaryUboats
    JOIN UboatsRaw
    ON SummaryUboats.UboatName = UboatsRaw.Name
    ORDER BY Days_in_service DESC
    """


# Query to calculate average service time by U-boat type
def type_longest_serving_days():
    return """
    SELECT 
        TypeOfUboat, 
        ROUND(AVG(Days_in_service), 2) AS AvgDaysInService, 
        ROUND(AVG(Years_in_service), 2) AS AvgYearsInService, 
        WarOutCome
    FROM SummaryUboats
    GROUP BY TypeOfUboat
    ORDER BY AvgDaysInService DESC
    """