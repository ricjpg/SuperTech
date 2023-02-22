class Product:

    def __init__(self, name, quantity, id = ""):
        self.name = name
        self.quantity = quantity
        self.__id = id
        self.__collection = "Product"


    def save(self,db):
        collection = db[self.__collection]
        result = collection.insert_one(self.__dict__)
        self.__id = result.inserted_id
