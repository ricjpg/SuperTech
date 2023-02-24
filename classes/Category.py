from classes.Product import Product

class Category:
    def __init__(self, category, id = ""):
        self.category = category
        self.__id = id
        self.__collection = "Category"


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
        collection = db["Category"]
        categories = collection.find()

        list_categories = []
        for c in categories:
            temp_category = Category(c["category"],c["_id"])
            list_categories.append(temp_category)
        return list_categories

    @staticmethod
    def delete_all(db):
        list_c = Category.get_list(db)
        for c in list_c:
            c.delete(db)

    @staticmethod
    def get_dict(db):
        collection = db["Category"]
        types = collection.find()

        dict_types_categories = {}
        for c in types:
            dict_types_categories[c["category"]] = c["_id"]
        return dict_types_categories
        
    
