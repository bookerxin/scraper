
import pandas as pd


class DataframeHandler:
    def __init__(self):
        pass

    @staticmethod
    def buy_now_dataframe(listings):
        data = {
            'title': [listing.title for listing in listings],
            'price': [listing.price for listing in listings],
            'condition': [listing.condition for listing in listings],
            'seller_rating': [listing.seller_rating for listing in listings],
            'watch_count': [listing.watch_count for listing in listings],
            'new_listing': [listing.new_listing for listing in listings],
            'link': [listing.link for listing in listings],
        }
        return pd.DataFrame(data)

    @staticmethod
    def auction_dataframe(listings):
        data = {
            'title': [listing.title for listing in listings],
            'price': [listing.price for listing in listings],
            'condition': [listing.condition for listing in listings],
            'seller_rating': [listing.seller_rating for listing in listings],
            'watch_count': [listing.watch_count for listing in listings],
            'new_listing': [listing.new_listing for listing in listings],
            'bid_count': [listing.bid_count for listing in listings],
            'time_left': [listing.time_left for listing in listings],
            'link': [listing.link for listing in listings],
        }
        return pd.DataFrame(data)
