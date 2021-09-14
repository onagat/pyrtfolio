# Copyright 2019 Alvaro Bartolome @ alvarobartt in GitHub
# See LICENSE for details.

import pyrtfolio
from pyrtfolio.StockPortfolio import StockPortfolio


def test_package():
    """
    This function tests both the authorship and version of pyrtfolio.
    """
    
    print(pyrtfolio.__author__)
    print(pyrtfolio.__version__)


def test_stock_portfolio():
    """
    This functions tests the basic creation of a StockPortfolio with some sample Stocks.
    """
    
    portfolio = StockPortfolio()
    
    portfolio.add_stock(stock_symbol='AAPL',
                        stock_country='United States',
                        purchase_date='09/04/2020',
                        num_of_shares=6,
                        cost_per_share=66.5)
    
    portfolio.add_stock(stock_symbol='8001',
                        stock_country='japan',
                        purchase_date='27/08/2020',
                        num_of_shares=1,
                        cost_per_share=2655.5)
    
    print(portfolio.data.head())
    portfolio.refresh()
    print(portfolio.data.head())


if __name__ == '__main__':
    test_package()
    test_stock_portfolio()
