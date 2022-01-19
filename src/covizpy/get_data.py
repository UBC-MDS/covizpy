def get_data(
    date_from=None,
    date_to=None,
    location=None,
):
    """Get covid data
    Retrieve covid data in pandas dataframe format witg tge time periods provided
    Parameters
    ----------
    date_from : str, optional
        Start date of the data range with format '%Y-%m-%d'. By default 'None' is used to represent 7 days prior to today's date
    date_to : str, optional
        End date of data range with format '%Y-%m-%d'. By default 'None' is used to represent today's date
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
    query = "@date_from <= date <= @date_to"
    url = "https://raw.githubusercontent.com/owid/covid-19-data/master/public/data/owid-covid-data.csv"

    if date_from is None:
        date_from = (pd.to_datetime("today").normalize() -
                     pd.to_timedelta(7, unit="d")).strftime('%Y-%m-%d')

    if date_to is None:
        date_to = pd.to_datetime("today").normalize().strftime('%Y-%m-%d')

    try:
        if date_from != datetime.strptime(date_from, "%Y-%m-%d").strftime("%Y-%m-%d"):
            raise ValueError
    except ValueError:
        raise ValueError(
            'Invalid argument value: date_from must be in format of "%Y-%m-%d". Also check if it is a valid date.'
        )
    except TypeError:
        raise TypeError(
            'Invalid argument type: date_from must be in string format of "%Y-%m-%d".'
        )

    try:
        if date_to != datetime.strptime(date_to, "%Y-%m-%d").strftime("%Y-%m-%d"):
            raise ValueError
    except ValueError:
        raise ValueError(
            'Invalid argument value: date_to must be in format of "%Y-%m-%d". Also check if it is a valid date.'
        )
    except TypeError:
        raise TypeError(
            'Invalid argument type: date_from must be in string format of "%Y-%m-%d".'
        )

    if location is not None:

        if not (isinstance(location, list)):
            raise TypeError(
                "Invalid argument type: location must be a list of strings."
            )

        for item in location:
            if not (isinstance(item, str)):
                raise TypeError(
                    "Invalid argument type: values inside location list must be a strings."
                )

        query += " and location in @location"

    covid_df = pd.read_csv(url, parse_dates=["date"],)
    covid_df = covid_df.query(query)

    return covid_df
