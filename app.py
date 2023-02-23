from classes import Product, Store, DbMongo
from dotenv import load_dotenv


def main():
    client, db = DbMongo.getDB()

    Product("Nachos","3").save(db)
    churro = Product("Doraditas","3")
    churro.save(db)

    client.close()


if __name__ == "__main__":
    load_dotenv()
    main()

