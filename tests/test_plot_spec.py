# File Name: test_plot_spec.py
# Author: Rong Li

from covizpy.plot_spec import plot_spec
from covizpy.get_data import get_data
import pandas as pd
from pytest import raises, fixture
import pickle


@fixture
def df():
    """
    Retrieve the dataframe
    """
    with open("tests/test_df_plot_spec.pkl", "rb") as pickle_file:
        return pickle.load(pickle_file)


def test_plot_spec_inputs(df):
    """
    Test the input type exceptions of plot_spec()
    """
    # check input type of dataframe
    with raises(FileNotFoundError) as e:
        plot_spec(None, location="Canada")
    assert "Data not found. There may be a problem with data URL." == str(e.value)
    
    # check input type of location
    with raises(TypeError) as e:
        plot_spec(df, location="Canada")
    assert "Invalid argument type: location must be a list of strings." == str(e.value)

    # check input type of the item inside location
    with raises(TypeError) as e:
        plot_spec(df, location=["Canada", 231])
    assert "Invalid argument type: values inside location list must be strings." == str(e.value)

    # check input type of val
    with raises(TypeError) as e:
        plot_spec(df, val=123)
    assert "Invalid argument type: val must be a string." == str(e.value)
    
    # check the column type of val
    with raises(TypeError) as e:
        plot_spec(df, val="iso_code")
    assert "Invalid argument type: val must be a numeric variable." == str(e.value)
    
    # check the Value of date_from
    with raises(ValueError) as e:
        plot_spec(df, date_from="iso_code")
    assert "Invalid argument value: date_from must be in format of YYYY-MM-DD. Also check if it is a valid date." == str(e.value)
    
    # check the Value of date_to
    with raises(ValueError) as e:
        plot_spec(df, date_to="342432")
    assert "Invalid argument value: date_to must be in format of YYYY-MM-DD. Also check if it is a valid date." == str(e.value)
    
    # check date_from and date_to logic
    with raises(ValueError) as e:
        plot_spec(df, date_from="2021-06-15", date_to="2021-06-11")
    assert "Invalid values: date_from should be smaller or equal to date_to (or today's date if date_to is not specified)." == str(e.value)
    
    # check date_to value
    with raises(ValueError) as e:
        plot_spec(df, date_to="2022-06-11")
    assert "Invalid values: date_to should be smaller or equal to today." == str(e.value)
    
    # check title value
    with raises(TypeError) as e:
        plot_spec(df, title=True)
    assert "Invalid argument type: title must be a string." == str(e.value)


def test_plot_spec_mapping(df):
    """
    Test plot output of plot_spec()
    """
    # check y-axis is using the correct variable
    assert plot_spec(df, val="new_deaths").layer[0].encoding.y.shorthand == "new_deaths", "Altair chart y-axis should be using variable 'new_deaths'"
    
    # check y-axis is using the correct lable
    assert plot_spec(df, val="new_deaths").layer[1].encoding.y.title == "New Deaths", "Altair chart y-axis should have lable 'New Deaths'"
    
    # check the first layer of the graph is line
    assert plot_spec(df).layer[0].mark == 'line', "Altair chart first layer should be line"
    
    # check the title of the graph
    assert plot_spec(df, title="Daily cases").layer[0].title=="Daily cases", "Altair chart title should be changeable"
    
    # check the data of the graph
    assert (plot_spec(df, date_from="2022-01-19", date_to="2022-01-20").layer[0].data["new_cases"] == [16849, 15775]).all(), "Altair chart data is wrong"