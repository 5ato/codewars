"""
https://www.codewars.com/kata/515bb423de843ea99400000a
"""


class PaginationHelper:
    def __init__(self, collection: list, items_per_page: int):
        self.original_collection: list = collection
        self.length: int = len(collection)
        self.collection: list[list] = self.page_per(collection, items_per_page)
        self.items_per_page: int = items_per_page

    @staticmethod
    def page_per(collection: list, items_per_page: int) -> list[list]:
        test = [[]]
        for item in collection:
            if len(test[-1]) == items_per_page:
                test.append([item])
            else:
                test[-1].append(item)
        return test

    def item_count(self) -> int: return self.length

    def page_count(self) -> int:
        total = self.length // self.items_per_page
        return total if (self.length % self.items_per_page) == 0 else total + 1

    def page_item_count(self, page_index: int) -> int:
        if self.page_count() <= page_index:
            return -1
        return len(self.collection[page_index])

    def page_index(self, item_index: int) -> int:
        if 0 <= item_index < self.length:
            item = self.original_collection[item_index]
            for page in self.collection:
                if item in page:
                    return self.collection.index(page)
        return -1


if __name__ == '__main__':
    p = PaginationHelper(list(range(0, 24)), 10)
    print(p.page_index(1))
