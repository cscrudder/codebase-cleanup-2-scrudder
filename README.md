# codebase-cleanup-template

## Setup
Create virtual environment:

```sh
conda create -n cleanup-env python=3.8
```

```sh
conda activate cleanup-env
```

Install packages:

```sh
pip install -r requirements.txt
```

## Configuration

### AlphaVantage API
Obtain a premium AlphaVantage API Key [here](https://www.alphavantage.co/).

Set environment variables using a ".env" file approach:
1) Create a .env file in the root directory.
2) Add the following code into the .env file.
```sh
ALPHAVANTAGE_API_KEY="..."
```
3) Add your AlphaVantage API Key after the '=' in the above code.
A default, demo code will be used if you do not complete this step, but it will not have full functionality.

### Groceries Data
To create a custom groceries list, create a .csv file called 'products.csv' and save it in the data folder.
Enter items following the template: id,name,aisle,department,price
A default product list will be used if you do not complete this step.

## Usage

Run the game:
```sh
python app/game.py
```

Run the crypto data fetcher:
```sh
python -m app.crypto
```

Run the stock data fetcher:
```sh
python -m app.stock
```

Run the unemployment data fetcher:
```sh
python -m app.unemployment
```

Run the groceries app:
```sh
python -m app.groceries
```


## Tests

To run all tests, type the following into the terminal:
```sh
pytest --disable-pytest-warnings
```

This code disables all pytest warnings that clog up the output. 
Alternatively, you can simply run:
```sh
pytest
```
which would run tests with the warnings.