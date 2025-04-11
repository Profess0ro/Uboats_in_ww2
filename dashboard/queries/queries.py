def top5_effective_uboats():
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
    LIMIT 5
    """