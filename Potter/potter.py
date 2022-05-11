from collections import Counter


__all__ = ['Potter']


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

    def price(self, books=None) -> float:
        if not books:
            books = self.books
            
        price = 0
        while len(books) > 0:
            counter = Counter(books)
            if len(counter.keys()) == 5 and len(books) % 5 == 0:
                # Maximum discount
                price += self.PER_BOOK * len(counter.keys()) * (1 - self.DISCOUNT_MAP[len(counter.keys())])
                for data, _ in counter.most_common():
                    books.remove(data)

            elif (len(books) - 1) % 5 == 0 and len(counter.keys()) == 5:
                # Dealing with 1 : 5 pair
                price += 8
                books.remove(counter.most_common()[0][0])
            else:
                # Break books into groups that less than maximum discount
                picked = 0
                for data, _ in counter.most_common():
                    if picked >= 4:
                        break
                    picked += 1
                    books.remove(data)
                price += self.PER_BOOK * picked * (1 - self.DISCOUNT_MAP[picked])

        return price

if __name__ == '__main__':
    potter = Potter([])
    potter.books = [0, 1, 1, 2, 3, 4]
    potter.price()
