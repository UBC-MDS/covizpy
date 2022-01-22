from covizpy.plot_summary import plot_summary
from covizpy.get_data import get_data
import pandas as pd
from pytest import raises, fixture
import pickle


@fixture
def df():
    """
    Retrieve the dataframe
    """
    with open("tests/test_df_plot_summary.pkl", "rb") as pickle_file:
        return pickle.load(pickle_file)


def test_plot_summary_inputs(df):
    """
    Test the input type exceptions of plot_summary()
    """
    # check input type of var
    with raises(TypeError) as e:
        plot_summary(df, var=123)
    assert "var needs to be of str type!" == str(e.value)

    # check input type of val
    with raises(TypeError) as e:
        plot_summary(df, val=123)
    assert "val needs to be of str type!" == str(e.value)

    # check input type of fun
    with raises(TypeError) as e:
        plot_summary(df, fun=123)
    assert "fun needs to be of str type!" == str(e.value)

    # check input of top_n is bigger than zero
    with raises(ValueError) as e:
        plot_summary(df, top_n=-5)
    assert "top_n must be an integer bigger than zero" == str(e.value)

    # check date_from and date_to logic
    with raises(ValueError) as e:
        plot_summary(df, date_from="2022-01-10", date_to="2020-01-01")
    assert (
        "Invalid values: date_from should be smaller or equal to date_to (or today's date if date_to is not specified)."
        == str(e.value)
    )


def test_plot_summary_agg(df):
    """
    Test aggregation logic of plot_summary()
    """
    # check groupby sum produce correct result for location
    assert (
        plot_summary(df, date_from="2022-01-01", date_to="2022-01-10").data["location"][
            0
        ]
        == "United States"
    ), "Aggregation logic is incorrect!"

    # check groupby sum produce correct result for new_cases
    assert (
        plot_summary(df, date_from="2022-01-01", date_to="2022-01-10").data[
            "new_cases"
        ][0]
        == 6898160.0
    ), "Aggregation logic is incorrect!"


def test_plot_summary_altair(df):
    """
    Test Altair output of plot_summary()
    """
    # check x-axis is using the correct variable
    assert (
        plot_summary(df, date_from="2022-01-01", date_to="2022-01-10").encoding["x"][
            "shorthand"
        ]
        == "new_cases"
    ), "Altair chart x-axis should be using variable 'new_cases'"
