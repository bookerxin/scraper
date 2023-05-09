
class Listing:
    def __init__(self, title, price, condition, seller_rating, new_listing, watch_count, link):
        self.title = title
        self.price = price
        self.condition = condition
        self.seller_rating = seller_rating
        self.new_listing = new_listing
        self.watch_count = watch_count
        self.link = link


class BuyNow(Listing):
    def __init__(self, title, price, condition, seller_rating, new_listing, watch_count, link):
        super().__init__(title, price, condition, seller_rating, new_listing, watch_count, link)

    def __repr__(self):
        return f'[ Buy Now ]\n{self.title}\n{self.price}\n{self.condition}\n{self.seller_rating}\n{self.watch_count}\n{self.new_listing}\n'


class Auction(Listing):
    def __init__(self, title, price, condition, seller_rating, new_listing, watch_count, bid_count, time_left, link):
        super().__init__(title, price, condition, seller_rating, new_listing, watch_count, link)
        self.bid_count = bid_count
        self.time_left = time_left

    def __repr__(self):
        return f'[ Auction ]\n{self.title}\n{self.price}\n{self.condition}\n{self.seller_rating}\n{self.watch_count}\n{self.new_listing}\n{self.bid_count}\n{self.time_left}\n'