from classes.Methods import Methods
class Product:

    def __init__(self, name, quantity, id = ""):
        self.name = name
        self.quantity = quantity
        self.__id = id
        self.__collection = "Product"

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