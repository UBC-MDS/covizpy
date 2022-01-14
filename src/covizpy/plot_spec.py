def plot_spec(
    country=["Canada"],
    val="new_cases",
    date_from=None,
    date_to=None,
    title=None
):
    """
    Create a line chart presenting specific country/countries COVID information
    within a time period
    
    Parameters
    ----------
    country : list, optional
        A list of the country names of interests, by default ["Canada"]
    val : str, optional
        A string indicating the quantitative values of interests. 
        Can be one of the following: "new_cases", "new_deaths", "hosp_patients",
        "new_vaccinations", by default "new_cases"
    date_from : str, optional
        Start date of the plot, by default "None" will use 2 weeks prior today's date
    date_to : str, optional
        End date of the plot, by default "None" will use today's date
    title : str, optional
        The title of the graph, by default "None" will be generated based on subject.

    Returns
    -------
    chart
        The line chart created
    """