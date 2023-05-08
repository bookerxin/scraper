from types import NoneType

import requests
from bs4 import BeautifulSoup

from listings import BuyNow, Auction


class Ebay:
    def __init__(self):
        pass

    @staticmethod
    def scraper(url):
        response = requests.get(url)
        html = response.content

        auction_listings = []
        buy_it_now_listings = []

        soup = BeautifulSoup(html, 'html.parser')
        listings = soup.find_all('div', {'class': 's-item__wrapper'})

        for i, listing in enumerate(listings):
            title = listing.find_next('div', {'class': 's-item__title'}).find_next('span', {'role': 'heading'}).text

            condition = listing.find_next('div', {'class', 's-item__subtitle'}).find_next('span', {'class', 'SECONDARY_INFO'}).text

            price = listing.find_next('span', {'class': 's-item__price'}).text

            seller_rating = listing.find_next('span', {'class', 's-item__seller-info-text'})
            seller_rating = seller_rating.text if seller_rating is not None else ''

            is_new = listing.find_next('span', {'class': 'LIGHT_HIGHLIGHT'})
            is_new = is_new.text if is_new is not None else ''

            bid_count = listing.find_next('span', {'class', 's-item__bidCount'})
            time_left = listing.find_next('span', {'class', 's-item__time-left'}).text if bid_count is not None else ''
            bid_count = bid_count.text if bid_count is not None else ''

            watch_count = listing.find_next('span', {'class', 's-item__watchCountTotal'})
            watch_count = watch_count.text if watch_count is not None else ''

            link = listing.find_next('a', {'class', 's-item__link'}).get('href')

            # Handle for Auctions
            if len(time_left) == 0:
                new_listing = BuyNow(title, price, condition, seller_rating, is_new, watch_count, link)
                buy_it_now_listings.append(new_listing)
            else:
                new_listing = Auction(title, price, condition, seller_rating, is_new, watch_count, bid_count, time_left, link)
                auction_listings.append(new_listing)

        return auction_listings, buy_it_now_listings
