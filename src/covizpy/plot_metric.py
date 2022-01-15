def plot_metric(
    metric="positive_rate",
    date_from=None,
    date_to=None
):
    """
    Create a line chart visualizing COVID total new
    cases and another metric for a specific time period
    
    Parameters
    ----------
    metric : str, optional
        The name of the metric to be plotted with the new COVID cases. 
        It can be one of the these: "reproduction_rate", "positive_rate", "cardiovasc_death_rate ",
        or any other numeric column
    date_from : str, optional
        Start date of the plot, by default "None" will use 2 weeks prior today's date
    date_to : str, optional
        End date of the plot, by default "None" will use today's date
    Returns
    -------
    chart
        The line chart created
    """
