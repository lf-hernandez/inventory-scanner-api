from graphene import String, Float, Int, Date, ObjectType

class Product(ObjectType):
    id = String(required=True)
    barcode = Int(required=True)
    name = String(required=True)
    description = String()
    price = Float(required=True)
    created_date = Date(required=True)
