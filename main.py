from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()


class Category(BaseModel):
    id: str
    name: str
    image: str


class Product(BaseModel):
    id: str
    name: str
    images: list
    price: str
    description: str


dbCategories = [
    Category(id='1', name='Shoes',
             image='http://product.hstatic.net/1000288768/product/nx_1868_14_grande_cccf1a2d8ec246ee933eb94b94412dde_grande.jpg'),
    Category(id='2', name='Hat',
             image='https://cdn.shopify.com/s/files/1/2091/0839/products/mockup-a067e42b_1200x1200.jpg'),
    Category(id='3', name='Clothes',
             image='https://previews.123rf.com/images/zephyr18/zephyr182004/zephyr18200400013/143659130-trendy-cotton-men-shirt-display-on-mannequin-in-clothes-shop-summer-collection-fashion-product-sampl.jpg'),
]

product = Product(id='1', name='Shoes',
            images= [
                'http://product.hstatic.net/1000288768/product/nx_1868_14_grande_cccf1a2d8ec246ee933eb94b94412dde_grande.jpg',
                'http://product.hstatic.net/1000288768/product/nx_1868_14_grande_cccf1a2d8ec246ee933eb94b94412dde_grande.jpg',
                'http://product.hstatic.net/1000288768/product/nx_1868_14_grande_cccf1a2d8ec246ee933eb94b94412dde_grande.jpg',
            ],
            price='$10.05',
            description='Lorem ipsum dolor sit amet, consectetur adipiscing elit. Suspendisse sed neque nec lectus lobortis accumsan in id metus. Aliquam erat volutpat.'),

dbProduct = [product,product,product,product]

dbCart = []


@app.get('/')
def index():
    return {'key': 'value'}


@app.get('/categories')
def get_categories():
    return dbCategories


@app.get('/categories/{category_id}')
def get_city(category_id: int):
    return dbProduct


#
@app.post('cities')
def create_city(city: Category):
    dbCategories.append(city.dict())
    return dbCategories[-1]


#

@app.delete('/cities')
def delete_city(citi_id: int):
    dbCart.pop(citi_id - 1)
    return {}
