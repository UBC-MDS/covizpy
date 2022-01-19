from covizpy.get_data import get_data
import pandas as pd
from pytest import raises


def test_get_data():
    """
    Test the get_data() functionality, including:
    - Check the return type of the function
    - Check the input types of each arguments
    - Check the valid values of each arguments
    """
    # check the return type of the function
    location = ["Canada", "United Kingdom", "China"]
    df = get_data(location=location)
    assert type(df) == pd.core.frame.DataFrame

    # check the output df contains locations specified
    assert set(df["location"]) == set(location)

    # check the output df is within default range
    assert df["date"].max() == pd.to_datetime("today").normalize()

    # check the output df is within default range
    assert df["date"].min() == (pd.to_datetime("today").normalize() -
                                pd.to_timedelta(7, unit="d"))

    # check the output df does not filter location if not specified
    assert len(set(get_data(date_from="2021-10-05")["location"])) > 10

    # check input type of data_from
    with raises(TypeError) as e:
        get_data(date_from=123)

    assert 'Invalid argument type: date_from must be in string format of "%Y-%m-%d".' == str(
        e.value)

    # check date format of data_from
    with raises(ValueError) as e:
        get_data(date_from='10-15-2021')

    assert 'Invalid argument value: date_from must be in format of "%Y-%m-%d". Also check if it is a valid date.' == str(
        e.value)

    # check valid date range of data_from
    with raises(ValueError) as e:
        get_data(date_from='2021-02-29')

    assert 'Invalid argument value: date_from must be in format of "%Y-%m-%d". Also check if it is a valid date.' == str(
        e.value)

    # check input type of data_to
    with raises(TypeError) as e:
        get_data(date_to=123)

    assert 'Invalid argument type: date_to must be in string format of "%Y-%m-%d".' == str(
        e.value)

    # check date format of data_to
    with raises(ValueError) as e:
        get_data(date_to='10-15-2021')

    assert 'Invalid argument value: date_to must be in format of "%Y-%m-%d". Also check if it is a valid date.' == str(
        e.value)

    # check valid date range of data_to
    with raises(ValueError) as e:
        get_data(date_to='2021-02-29')

    assert 'Invalid argument value: date_to must be in format of "%Y-%m-%d". Also check if it is a valid date.' == str(
        e.value)

    # check valid date range: date_from <= date_to
    with raises(ValueError) as e:
        get_data(date_from='2021-10-15', date_to='2021-10-01')

    assert "Invalid values: date_from should be smaller or equal to date_to (or today's date if date_to is not specified)." == str(
        e.value)

    # check valid date range: date_to <= today
    with raises(ValueError) as e:
        get_data(date_to=(pd.to_datetime("today").normalize() +
                          pd.to_timedelta(7, unit="d")).strftime('%Y-%m-%d'))

    assert "Invalid values: date_to should be smaller or equal to today." == str(
        e.value)

    # check input type of location: not a list
    with raises(TypeError) as e:
        get_data(location=123)
    assert "Invalid argument type: location must be a list of strings." == str(
        e.value)

    # check type of input list of location
    with raises(TypeError) as e:
        get_data(location=["Canada", "China", 123])
    assert "Invalid argument type: values inside location list must be a strings." == str(
        e.value)
