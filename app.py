from classes import Product, Store, DbMongo
from dotenv import load_dotenv


def main():
    client, db = DbMongo.getDB()

    Product("Lays","110").save(db)


    client.close()


if __name__ == "__main__":
    load_dotenv()
    main()

