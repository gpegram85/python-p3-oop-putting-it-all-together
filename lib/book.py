#!/usr/bin/env python3

class Book:
    def __init__(self, title="Default Title", page_count=1000):
        self.title = title
        self.page_count = page_count

    @property
    def page_count(self):
        return self._page_count
    
    @page_count.setter
    def page_count(self, page_count):
        if isinstance(page_count, int):
            self._page_count = page_count
        else:
            print("page_count must be an integer")
    
    def turn_page(self):
        print("Flipping the page...wow, you read fast!")

    @property
    def title(self):
        return self._title
    
    @title.setter
    def title(self, title):
        if isinstance(title, str):
            self._title = title
        else:
            print("Title must be a string.")

    
        