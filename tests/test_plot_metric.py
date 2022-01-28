# File Name: test_plot_metric.py
# Author: Rohit Rawat

from covizpy.plot_metric import plot_metric
from pytest import raises, fixture


def test_plot_metric_input():
    """
    Test the inputs of plot_metric()
    """
    # check the data type of the date_from
    with raises(TypeError) as e:
        plot_metric(date_from=123)
    assert (
        "Incorrect argument type: The starting date should be in string format"
        == str(e.value)
    )

    # check the data type of the date_to
    with raises(TypeError) as e:
        plot_metric(date_to=123)
    assert "Incorrect argument type: The end date should be in string format" == str(
        e.value
    )

    # check the data type of the metric
    with raises(TypeError) as e:
        plot_metric(metric=123)
    assert "Incorrect argument type: Metric 1 input should be a string" == str(e.value)

    # check if the metric provided is one of the columns in the dataframe
    with raises(ValueError) as e:
        plot_metric(metric="invalid_column")
    assert (
        "Incorrect argument value: The metric chosen is not one of the columns in dataframe"
        == str(e.value)
    )


def test_plot_metric_output():
    """
    Test the output type exceptions of plot_metric()
    """

    # check the layer 1 type is line or not
    assert (
        plot_metric().layer[0].mark.type == "line"
    ), "Incorrect Mark Type: Layer 1 mark is not line"

    # check the layer 2 type is line or not
    assert (
        plot_metric().layer[1].mark.type == "line"
    ), "Incorrect Mark Type: Layer 2 mark is not line"

    # check the layer 1 x-axis is named Date or not
    assert (
        plot_metric().layer[0].encoding.x.title == "Date"
    ), "Incorrect Axis Label: Layer 1 x-axis label is not Date"
