from api.app import app
from fastapi import APIRouter, Query

from dataframes import DataframeHandler
from targets import Ebay

router = APIRouter()


@app.get('/')
def read_root():
    return {'hello': 'world'}


@app.get('/test')
def read_test():
    auction_listings, buy_it_now_listings = Ebay().scraper('https://www.ebay.co.uk/sch/i.html?_from=R40&_trksid=p2380057.m570.l1313&_nkw=lg+gram+17&_sacat=0')
    return DataframeHandler.buy_now_dataframe(buy_it_now_listings)


@app.get('/request')
def read_request(item: str = Query()):
    print(item)
    auction_listings, buy_it_now_listings = Ebay().scraper(f'https://www.ebay.co.uk/sch/i.html?_from=R40&_trksid=p2334524.m570.l1313&_nkw={item}')
    return DataframeHandler.buy_now_dataframe(buy_it_now_listings)
