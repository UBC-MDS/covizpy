import pandas as pd
import altair as alt
from dateutil.parser import parse


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
    # Load data
    df = pd.read_csv("https://covid.ourworldindata.org/data/owid-covid-data.csv")

    # Exception Handling
    if not isinstance(var, str):
        raise TypeError("var needs to be of str type!")

    if not isinstance(val, str):
        raise TypeError("val needs to be of str type!")

    if not isinstance(fun, str):
        raise TypeError("fun needs to be of str type!")

    if not isinstance(df, pd.DataFrame):
        raise FileNotFoundError("Data not found! There may be a problem with data URL.")

    if df[var].dtypes.kind != "O":
        raise TypeError("var needs to be a categorical variable!")

    if df[val].dtypes.kind == "O":
        raise TypeError("val needs to be a numeric variable!")

    if not isinstance(top_n, int) or top_n <= 0:
        raise ValueError("top_n must be an integer bigger than zero")

    if pd.to_datetime(date_to) < pd.to_datetime(date_from):
        raise ValueError(
            "Invalid values: date_from should be smaller or equal to date_to (or today's date if date_to is not specified)."
        )
    if pd.to_datetime(date_to) > pd.to_datetime("today").normalize():
        raise ValueError("Invalid values: date_to should be smaller or equal to today.")

    # Parse date, else raise ValueError
    date_from = parse(date_from)
    date_to = parse(date_to)

    # Convert 'date' to date format
    df["date"] = pd.to_datetime(df["date"])

    # Filter by date
    df = df.query("date >= @date_from & date <= @date_to")

    # Remove aggregated locations
    df = df[~df["iso_code"].str.startswith("OWID")]

    # Aggregation
    df_plot = df.groupby(var).agg({val: fun})[val].nlargest(top_n)
    df_plot = df_plot.to_frame().reset_index()

    return alt.Chart(df_plot).mark_bar().encode(y=alt.Y(var, sort="x"), x=val)
