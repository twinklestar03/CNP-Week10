from collections import Counter


class Potter:
    PER_BOOK = 8
    DISCOUNT_MAP = {
        1: 0,
        2: 0.05,
        3: 0.10,
        4: 0.20,
        5: 0.25
    }

    def __init__(self, books=[]):
        self.books = books

    def price(self) -> int:
        price = 0
        while len(self.books) > 0:
            counter = Counter(self.books)

            if len(self.books) % 5 == 0 and len(counter.keys()) == 5:
                # Maximum discount
                price += self.PER_BOOK * len(counter.keys()) * (1 - self.DISCOUNT_MAP[len(counter.keys())])
                for data, _ in counter.most_common():
                    self.books.remove(data)
            else:
                # Break books into groups that less than maximum discount
                picked = 0
                for data, _ in counter.most_common():
                    if picked >= 4:
                        break
                    picked += 1
                    self.books.remove(data)
                
                price += self.PER_BOOK * picked * (1 - self.DISCOUNT_MAP[picked])

        print(price)
        return 0

if __name__ == '__main__':
    potter = Potter([])
    # potter.books = [1, 1, 2, 2, 3, 3, 4, 5]
    potter.price()
