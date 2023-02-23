from classes.DbMongo import DbMongo
from classes.Product import Product

class Store:

    def __init__(self, name, category, id = ""):
        self.name = name
        self.category = category
        self.__id = id
        self.__collection = "Product"

    def save(self,db):
        collection = db[self.__collection]
        result = collection.insert_one(self.__dict__)
        self.__id = result.inserted_id



    