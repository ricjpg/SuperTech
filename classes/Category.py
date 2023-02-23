from classes.Product import Product

class Category:
    def __init__(self, name, product, id = ""):
        self.name = name
        self.product = product
        self.__id = id
        self.__collection = "Category"


def save(self,db):
    collection = db[self.__collection]
    result = collection.insert_one(self.__dict__)
    self.__id = result.inserted_id
    