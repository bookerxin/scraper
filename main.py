from types import NoneType

import os
import sys
import pyfiglet
from api.routes import router
from api.app import app

from dataframes import DataframeHandler
from targets import Ebay


# from selenium import webdriver
# from selenium.webdriver.common.keys import Keys

class OptionsMenu:
    def __init__(self):
        pass

    @staticmethod
    def start_menu():
        running = True
        options = ['1. Ebay']

        while running:
            map(options)


if __name__ == "__main__":
    # Use Selenium for page changing at least
    # Selenium for searching items

    banner = pyfiglet.figlet_format('S C R A P E R ', 'isometric1', width=180)
    print(banner)

    # auction_listings, buy_it_now_listings = Ebay().scraper('https://www.ebay.co.uk/sch/i.html?_from=R40&_trksid=p2380057.m570.l1313&_nkw=lg+gram+17&_sacat=0')
    # print(DataframeHandler.buy_now_dataframe(buy_it_now_listings))
    # print(DataframeHandler.auction_dataframe(auction_listings))

    app.include_router(router)

    # Make Subprocess
    os.system('uvicorn main:app')

    # Idea is to give the program a terminal interface as well
