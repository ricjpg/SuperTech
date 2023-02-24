class Product:

    def __init__(self, name, quantity, category, id = ""):
        self.name = name
        self.quantity = quantity
        self.category = category
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

    @staticmethod
    def get_list(db):
        collection = db["Product"]
        products = collection.find()

        list_products = []
        for p in products:
            temp_products = Product(
                p["name"],
                p["quantity"],
                p["category"],
                p["_id"])
            list_products.append(temp_products)
        return list_products

    @staticmethod
    def delete_all(db):
        list_p = Product.get_list(db)
        for p in list_p:
            p.delete(db)