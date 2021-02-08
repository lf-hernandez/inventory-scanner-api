from graphene import List, String, Float, Int, Date, ObjectType, Argument, Schema, InputObjectType, Mutation, Field
from db_conf import init_db

db = init_db()

class Product(ObjectType):
    id = String(required=True)
    barcode = Int(required=True)
    name = String(required=True)
    description = String()
    price = Float(required=True)
 
    
class AddProductInput(InputObjectType):
    barcode = Int(required=True)
    name = String(required=True)
    description = String()
    price = Float(required=True)
    
        
class AddProduct(Mutation):
    class Arguments:
        input = Argument(AddProductInput)

    product = Field(Product)
    
    async def mutate(self, info, input):
        db.collection(u'products').document().set(input)
        return AddProduct(product=product)
        
class Query(ObjectType):
    get_products = List(Product)

    async def resolve_get_products(self, info):
        products = db.collection(u'products').stream()
        product_list = []
        
        for product in products:
            product_list.append(product.to_dict())
            
        return product_list


class Mutation(ObjectType):
    add_product = AddProduct.Field()
             

schema = Schema(query=Query,mutation=Mutation)
