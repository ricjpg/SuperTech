from classes import Product, Store, DbMongo, Category
from dotenv import load_dotenv
import pprint


def main():
    printer = pprint.PrettyPrinter()
    client, db = DbMongo.getDB()


    #-------------------CLEAN UP----------------------#
    Category.delete_all(db)
    Store.delete_all(db)
    Product.delete_all(db)
    
    #-------------------SETTING SOME DATA----------------------#
    Category("Gamming").save(db)
    Category("Office").save(db)
    Category("Educational").save(db)

    dictType = Category.get_dict(db)

    Product("RTX 4090 TI","7",dictType["Gamming"]).save(db)
    Product("Chair","12",dictType["Office"]).save(db)
    Product("MongoDB for dummies","12",dictType["Educational"]).save(db)
    Product("Python for dummies","5",dictType["Educational"]).save(db)

    Store("NewEgg",dictType["Gamming"]).save(db)
    Store("HonduCompras",dictType["Office"]).save(db)
    Store("Pearson",dictType["Educational"]).save(db)
    

    #-------------------GETTING ALL DATA----------------------#
    Store.get_report(db)
    # Category.get_report(db)



    client.close()


if __name__ == "__main__":
    load_dotenv()
    main()

