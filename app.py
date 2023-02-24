from classes import Product, Store, DbMongo, Category
from dotenv import load_dotenv


def main():
    client, db = DbMongo.getDB()

    Category.delete_all(db)

    # Category("Gaming").save(db)
    # Category("Office").save(db)
    # Category("Educational").save(db)


    client.close()


if __name__ == "__main__":
    load_dotenv()
    main()

