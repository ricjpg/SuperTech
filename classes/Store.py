from classes.DbMongo import DbMongo
from classes.Product import Product
from classes.Category import Category
import pprint

class Store:
    printer = pprint.PrettyPrinter()
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

    @staticmethod
    def get_list(db):
        collection = db["Store"]
        store = collection.find()

        list_store = []
        for s in store:
            temp_store = Store(
                s["name"],
                s["category"],
                s["_id"])
            list_store.append(temp_store)
        return list_store

    @staticmethod
    def delete_all(db):
        list_s = Store.get_list(db)
        for s in list_s:
            s.delete(db)

    @staticmethod
    def get_dict(db):
        collection = db["Store"]
        types = collection.find()

        dict_types_store = {}
        for s in types:
            dict_types_store[s["name"]] = s["_id"]
        return dict_types_store
        
    @staticmethod
    def get_report(db):
        collection = db["Store"]
        printer = pprint.PrettyPrinter()
        result = collection.aggregate([
            {
                '$lookup':{
                "from":"Product",
                "localField":"category",
                "foreignField":"category",
                "as":"cat"
                }
            },
            {
                '$project':{
                    "name":1,
                    "cat":1,
                    # "cat":1,
                    "Product.name":1,
                    "Product.quantity":1,
                    "Product.category":1,
                    # "quantity":1,
                    "_id":0,
                    }
            }
        ])
        for s in result:
            # print(s)
            printer.pprint(s)
        