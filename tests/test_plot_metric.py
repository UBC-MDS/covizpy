# File Name: test_plot_metric.py
# Author: Rohit Rawat

from covizpy.plot_metric import plot_metric

def test_plot_metric_input():
    """
    Test the inputs of plot_metric()
    """
    # check the data type of the date_from
    assert plot_metric(date_from=123), 'Incorrect argument type: The starting date should be in string format'

    # check the data type of the date_to
    assert plot_metric(date_to=123), 'Incorrect argument type: The end date should be in string format'
    
    # check the data type of the metric
    assert plot_metric(metric=123), 'Incorrect argument type: Metric 1 input should be a float'
   
    # check if the metric provided is one of the columns in the dataframe
    assert plot_metric(metric="invalid_column"), 'Incorrect argument value: The metric chosen is not one of the columns in dataframe'
   
   #
    assert plot_metric(date_from="01-04-2000"), 'Error in date format: Could not fetch data using get_data. Incorrect date format'

def test_plot_metric_output():
    """
    Test the output type exceptions of plot_metric()
    """
    # check the output type of the plot 
    assert type(plot_metric()), 'altair.vegalite.v4.api.LayerChart'
    
