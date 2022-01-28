# File Name: test_get_data.py
# Author: Thomas Siu

from covizpy.get_data import get_data
import pandas as pd
from pytest import raises, fixture


@fixture
def location():
    """
    Fixture of location list
    """
    return ["Canada", "United Kingdom", "China"]


def test_get_data_output(location):
    """
    Test the output of get_data()
    """

    df = get_data(location=location)

    # check the return type of the function
    assert (
        type(df) == pd.core.frame.DataFrame
    ), "Return type should be a pandas dataframe."

    # check the output df contains locations specified
    assert set(df["location"]) == set(
        location
    ), "Location returned in dataframe does not match with the input"

    # check the output df is within default range
    assert (
        df["date"].max() == pd.to_datetime("today").normalize()
        or df["date"].max()
        == (pd.to_datetime("today").normalize() - pd.to_timedelta(1, unit="d"))
        or df["date"].max()
        == (pd.to_datetime("today").normalize() - pd.to_timedelta(2, unit="d"))
    ), "date_to does not match the default range of today or today - 1"
    # check the output df is within default range
    assert df["date"].min() == (
        pd.to_datetime("today").normalize() - pd.to_timedelta(7, unit="d")
        or df["date"].min()
        == (pd.to_datetime("today").normalize() - pd.to_timedelta(8, unit="d"))
    ), "date_from does not match the default range of D-7"

    # check the output df does not filter location if not specified
    assert (
        len(set(get_data(date_from="2021-10-05")["location"])) > 10
    ), "Data returned has been filtered somehow."


def test_get_data_input_types():
    """
    Test the input type exceptions of get_data()
    """
    # check input type of data_from
    with raises(TypeError) as e:
        get_data(date_from=123)
    assert (
        "Invalid argument type: date_from must be in string format of YYYY-MM-DD."
        == str(e.value)
    )

    # check date format of data_from
    with raises(ValueError) as e:
        get_data(date_from="10-15-2021")
    assert (
        "Invalid argument value: date_from must be in format of YYYY-MM-DD. Also check if it is a valid date."
        == str(e.value)
    )

    # check input type of data_to
    with raises(TypeError) as e:
        get_data(date_to=123)
    assert (
        "Invalid argument type: date_to must be in string format of YYYY-MM-DD."
        == str(e.value)
    )

    # check date format of data_to
    with raises(ValueError) as e:
        get_data(date_to="10-15-2021")
    assert (
        "Invalid argument value: date_to must be in format of YYYY-MM-DD. Also check if it is a valid date."
        == str(e.value)
    )

    # check input type of location: not a list
    with raises(TypeError) as e:
        get_data(location=123)
    assert "Invalid argument type: location must be a list of strings." == str(e.value)

    # check type of input list of location
    with raises(TypeError) as e:
        get_data(location=["Canada", "China", 123])
    assert (
        "Invalid argument type: values inside location list must be a strings."
        == str(e.value)
    )


def test_get_data_input_values():
    """
    Test the input values exceptions of get_data()
    """
    # check valid date range of data_from
    with raises(ValueError) as e:
        get_data(date_from="2021-02-29")
    assert (
        "Invalid argument value: date_from must be in format of YYYY-MM-DD. Also check if it is a valid date."
        == str(e.value)
    )

    # check valid date range of data_to
    with raises(ValueError) as e:
        get_data(date_to="2021-02-29")
    assert (
        "Invalid argument value: date_to must be in format of YYYY-MM-DD. Also check if it is a valid date."
        == str(e.value)
    )

    # check valid date range: date_from <= date_to
    with raises(ValueError) as e:
        get_data(date_from="2021-10-15", date_to="2021-10-01")
    assert (
        "Invalid values: date_from should be smaller or equal to date_to (or today's date if date_to is not specified)."
        == str(e.value)
    )

    # check valid date range: date_to <= today
    with raises(ValueError) as e:
        get_data(
            date_to=(
                pd.to_datetime("today").normalize() + pd.to_timedelta(7, unit="d")
            ).strftime("%Y-%m-%d")
        )

    assert "Invalid values: date_to should be smaller or equal to today." == str(
        e.value
    )
