def plot_metric(metric='positive_rate', date_from="2022-01-01", date_to="2022-01-13"):
    """
    Create a line chart visualizing COVID total new
    cases and another metric for a specific time period
    
    Parameters
    ----------
    metric    : str, optional
                The name of the metric to be plotted with the new COVID cases. 
                It can be one of the these: "reproduction_rate", "positive_rate",
                or any other numeric column
    date_from : str, optional
                Start date of the plot in "YYYY-MM-DD" format, by default "2022-01-01"
    date_to   : str, optional
                End date of the plot in "YYYY-MM-DD" format, by default "2022-01-13"
    Returns
    -------
    chart
        The line chart created
    """
    
    try:
        covid_df = pd.read_csv('https://covid.ourworldindata.org/data/owid-covid-data.csv')
    except:
        return "The link to the data is broken"
    
    # Check the input format of arguments
    if not isinstance(metric, str):
        return 'Incorrect argument type: Metric 1 input should be a float'

    if not isinstance(date_from, str):
        return 'Incorrect argument type: The starting date should be in string format'

    if not isinstance(date_to, str):
        return 'Incorrect argument type: The end date should be in string format'

    # Check the date format of the dates

    try:
        datetime.datetime.strptime(date_from, '%Y-%m-%d')
    except:
        return 'date_from: Date Formart incorrect, should be YYYY-MM-DD'
    try:
        datetime.datetime.strptime(date_to, '%Y-%m-%d')
    except:
        return 'date_to: Date format incorrect, should be YYYY-MM-DD'

    # Check if the date value and column name is correct

    if not date_from < date_to:
        return 'The date_from has to be earlier than date_to argument'
    if date_from < covid_df.date.min():
        return "The date_from is less than the minimum date possible ('2020-01-01')"
    if date_to > covid_df.date.max():
        return 'The date_to is greater than the maximum date possible'
    if metric not in covid_df.columns:
        return 'The metric column is not present in df. Check column name'
    if not(isinstance(covid_df[metric][0], float)):
        return 'The data type of the metric column should be numeric'

    # Filtering the data for lighter visualizations

    df = covid_df[covid_df['date'] > date_from]
    df = df[df['date'] < date_to]
    
    metric_label = "Mean " + metric.replace("_", " ")
    
    base = alt.Chart(df).encode(x=alt.X('monthdate(date):T',
                                axis=alt.Axis(format='%b-%d'),
                                title='Date'))

    line1 = base.mark_line(color='skyblue', interpolate='monotone'
                           ).encode(alt.Y('sum(new_cases)',
                                    scale=alt.Scale(zero=False),
                                    axis=alt.Axis(title='Daily new cases'
                                    , titleColor='skyblue')))

    line2 = base.mark_line(color='orange', interpolate='monotone'
                           ).encode(alt.Y(f"mean({metric})",
                                    scale=alt.Scale(zero=False),
                                    axis=alt.Axis(title=metric_label
                                    , titleColor='orange')))

    plot = alt.layer(line1, line2,
                     title= 'Daily COVID cases versus ' + metric_label
                     ).resolve_scale(y='independent')

    return plot
