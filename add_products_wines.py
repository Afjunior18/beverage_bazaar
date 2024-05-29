import os

from products.models import Product, Category

# create wine category
wine_category, created = Category.objects.get_or_create(type_product='Wines')

wine_products = [
    {
        "name": "Château Margaux 2015",
        "description": "A rich and complex Bordeaux wine with notes of blackcurrant and cedar.",
        "price": 499.99,
        "rating": "0",
        "image_url": "wine_01.jpg",
        "image": "wine_01.jpg",
        "sku": "WINE001",
        "region": "France"
    },
    {
        "name": "Penfolds Grange 2016",
        "description": "A full-bodied Australian wine with a deep, dark fruit profile and a long finish.",
        "price": 699.99,
        "rating": "0",
        "image_url": "wine_02.jpg",
        "image": "wine_02.jpg",
        "sku": "WINE002",
        "region": "Australia"
    },
    {
        "name": "Screaming Eagle Cabernet Sauvignon 2017",
        "description": "An exquisite Napa Valley wine with intense black fruit flavors and silky tannins.",
        "price": 2999.99,
        "rating": "0",
        "image_url": "wine_03.jpg",
        "image": "wine_03.jpg",
        "sku": "WINE003",
        "region": "USA"
    },
    {
        "name": "Vega Sicilia Único 2009",
        "description": "A legendary Spanish wine with complex flavors of dark berries, spices, and oak.",
        "price": 449.99,
        "rating": "0",
        "image_url": "wine_04.jpg",
        "image": "wine_04.jpg",
        "sku": "WINE004",
        "region": "Spain"
    },
    {
        "name": "Masseto 2016",
        "description": "An exceptional Italian wine with layers of ripe black fruits, spices, and earthy notes.",
        "price": 799.99,
        "rating": "0",
        "image_url": "wine_05.jpg",
        "image": "wine_05.jpg",
        "sku": "WINE005",
        "region": "Italy"
    },
    {
        "name": "Dom Pérignon 2010",
        "description": "A prestigious Champagne with elegant bubbles and notes of citrus, apple, and brioche.",
        "price": 199.99,
        "rating": "0",
        "image_url": "wine_06.jpg",
        "image": "wine_06.jpg",
        "sku": "WINE006",
        "region": "France"
    },
    {
        "name": "Sassicaia 2015",
        "description": "A renowned Italian wine with a refined blend of red berries, spices, and floral notes.",
        "price": 249.99,
        "rating": "0",
        "image_url": "wine_07.jpg",
        "image": "wine_07.jpg",
        "sku": "WINE007",
        "region": "Italy"
    },
    {
        "name": "Château Lafite Rothschild 2015",
        "description": "An iconic Bordeaux wine with a balanced profile of cassis, tobacco, and graphite.",
        "price": 799.99,
        "rating": "0",
        "image_url": "wine_08.jpg",
        "image": "wine_08.jpg",
        "sku": "WINE008",
        "region": "France"
    },
    {
        "name": "Ornellaia 2016",
        "description": "A superb Italian wine with rich flavors of dark fruits, chocolate, and spice.",
        "price": 249.99,
        "rating": "0",
        "image_url": "wine_09.jpg",
        "image": "wine_09.jpg",
        "sku": "WINE009",
        "region": "Italy"
    },
    {
        "name": "Pétrus 2015",
        "description": "A luxurious Bordeaux wine with complex notes of plum, truffle, and earthy minerals.",
        "price": 2999.99,
        "rating": "0",
        "image_url": "wine_10.png",
        "image": "wine_10.png",
        "sku": "WINE010",
        "region": "France"
    },
    {
        "name": "Château d’Yquem 2014",
        "description": "A legendary Sauternes wine with a luscious profile of apricot, honey, and exotic fruits.",
        "price": 499.99,
        "rating": "0",
        "image_url": "wine_11.png",
        "image": "wine_11.png",
        "sku": "WINE011",
        "region": "France"
    },
    {
        "name": "Harlan Estate 2016",
        "description": "An esteemed Napa Valley wine with powerful flavors of blackberry, licorice, and espresso.",
        "price": 899.99,
        "rating": "0",
        "image_url": "wine_12.png",
        "image": "wine_12.png",
        "sku": "WINE012",
        "region": "USA"
    }
]

# Adding wines products to a DB
for wine_data in wine_products:
    Product.objects.create(
        category=wine_category,
        **wine_data
    )