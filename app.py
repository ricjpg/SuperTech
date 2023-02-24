from classes import Product, Store, DbMongo, Category
from dotenv import load_dotenv


def main():
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
    Product("OOP Book","1",dictType["Educational"]).save(db)

    st = Store("NewEgg",dictType["Gamming"])
    st.save(db)
    # printer.pprint(Store)
    printer.pprint(st)

    client.close()


if __name__ == "__main__":
    load_dotenv()
    main()

