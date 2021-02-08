from graphene.test import Client
from schema import schema

client = Client(schema)


def test_get_products_query(snapshot):
    query = """
        query getProducts {
            id
            name
            description
            barcode
            price
        }
    """
    
    snapshot.assert_match(client.execute(query))
