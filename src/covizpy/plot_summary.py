def plot_summary(
    var="location",
    val="new_cases",
    fun="sum",
    date_from="2022-01-01",
    date_to="2022-01-13",
    top_n=5,
):
    """Generate summary plot

    Create a horizontal bar chart summarising a specified variable and value
    within a time period

    Parameters
    ----------
    var : str, optional
        Qualitative values to segment data. Must be a categorical variable.
        Also known as a 'dimension'. By default 'location'
    val : str, optional
        Quantitative values to be aggregated. Must be numeric variable.
        Also known as a 'measure'. By default 'new_cases'
    fun : str, optional
        Aggregation function for val, by default 'sum'
    date_from : str, optional
        Start date for plot summary, by default '2022-01-01'
    date_to : str, optional
        End date for plot summary, by default '2022-01-13'
    top_n : int, optional
        Specify number of qualitative values to show, by default 5
    """
