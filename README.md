# covizpy

`covizpy` is a Python package that provides easy access to Covid-19 data from [Our World in Data](https://ourworldindata.org/coronavirus), as well as functions to generate relevant Covid-19 charts and summaries easily. We aim to make `covizpy` simple and easy to use. Our goal is to enable anyone with basic Python programming knowledge to access and visualize Covid-19 data, and make their own informed decisions and conclusions.

There are existing Python packages that allow users to download and generate Covid-19 charts. For example, [covid19pandas](https://github.com/PayneLab/covid19pandas) is a package that presents COVID-19 data from Johns Hopkins University and The New York Times in pandas dataframes, to make analysis and visualization easier in a Python environment.

While other packages have more advanced plotting capabilities, we provide simpler functions that allow users to answer questions regarding the Covid-19 pandemic as quickly as possible.

## Features

This package contains four functions: `plot_metric`, `plot_spec`, `get_data` and `plot_summary`.

* `plot_metric`: Create a line chart presenting COVID total new cases verses another metric within a time period

* `plot_spec`: Create a line chart presenting specific country/countries COVID information within a time period

* `get_data`: User can retrieve the COVID data from the source as a pandas dataframe. Specific data can be retrieved by passing the date range and the list of countries

* `plot_summary`: Create a horizontal bar chart summarising a specified variable and value within a time period

## Installation

```bash
$ pip install --index-url https://test.pypi.org/simple/ covizpy
```

## Usage and Examples

To use the package, import the package with following commands:

```python
from covizpy.get_data import get_data
from covizpy.plot_summary import plot_summary
from covizpy.plot_metric import plot_metric
from covizpy.plot_spec import plot_spec
```

To use the functions, see below examples:

### Retrieve COVID-19 data with default date range and location

```python
df = get_data()
```

### Plot summary graph (bar chart)

```python
plot_summary(df)
```

![Summary graph](https://github.com/UBC-MDS/covizpy/raw/main/img/plot_summary.png)


### Plot metrics of new COVID-19 cases (line chart)

```python
plot_metric()
```

![New COVID-19 case graph](https://github.com/UBC-MDS/covizpy/raw/main/img/plot_metric.png)

### Plot specific country COVID-19 cases (line chart)

```python
plot_spec(df, country=["Canada"])
```

![New COVID-19 case graph](https://github.com/UBC-MDS/covizpy/raw/main/img/plot_spec.png)


## Contributors

* Rohit Rawat
* Rong Li
* Thomas Siu
* Ting Zhe Yan

## Contributing

Interested in contributing? Check out the contributing guidelines. Please note that this project is released with a Code of Conduct. By contributing to this project, you agree to abide by its terms.

## License

`covizpy` was created by Rohit Rawat, Rong Li, Thomas Siu, Ting Zhe Yan. It is licensed under the terms of the MIT license.

## Credits

`covizpy` was created with [`cookiecutter`](https://cookiecutter.readthedocs.io/en/latest/) and the `py-pkgs-cookiecutter` [template](https://github.com/py-pkgs/py-pkgs-cookiecutter).
