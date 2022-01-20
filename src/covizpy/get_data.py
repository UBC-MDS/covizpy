def get_data(
    date_from=None,
    date_to=None,
    location=None
):
    """Get covid data
    Retrieve covid data in pandas dataframe format with the time periods and countries provided.

    Parameters
    ----------
    date_from : str, optional
        Start date of the data range. By default 'None' is used to represent 7 days prior to today's date.
    date_to : str, optional
        End date of data range. By default 'None' is used to represent today's date.
    location : list, optional
        List of target country names. By default 'None' is used for all countries.

    Returns
    -------
    pandas.DataFrame
        Pandas dataframe of the selected covid data.

    Examples
    --------
    >>> get_data(date_from="2022-01-01", date_to="2022-01-07", location=["Canada", "China"])
    """
