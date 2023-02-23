from classes.DbMongo import DbMongo
from classes.Product import Product

class Store:

    def __init__(self, name, category, id = ""):
        self.name = name
        self.category = category
        self.__id = id
        self.__collection = "Store"

    def save(self,db):
        collection = db[self.__collection]
        result = collection.insert_one(self.__dict__)
        self.__id =  result.inserted_id

    def update(self,db):
        collection = db[self.__collection]
        filterToUse = {'_id':self.__id}
        objStorage = {'$set': self.__dict__}
        collection.update_one(filterToUse,objStorage)

    def delete(self, db):
        collection = db[self.__collection]
        filterToUse = {'_id':self.__id}
        collection.delete_one(filterToUse)