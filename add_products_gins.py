import os

from products.models import Product, Category

# create gin category
gin_category, created = Category.objects.get_or_create(type_product='Gins')

products = [
    {
        "name": "Hendrick's Gin",
        "description": "A premium gin with infusions of cucumber and rose petals, creating a refreshing and unique flavor.",
        "price": 39.99,
        "rating": "0",
        "image_url":"gin_01.jpg",
        "image": "gin_01.jpg",
        "sku": "GIN001",
        "region": "Girvan, Scotland"
    },
    {
        "name": "Bombay Sapphire",
        "description": "A London Dry gin with a complex and balanced flavor, featuring botanicals such as juniper, coriander, and citrus.",
        "price": 29.99,
        "rating": "0",
        "image_url": "gin_02.jpg",
        "image": "gin_02.jpg",
        "sku": "GIN002",
        "region": "London, England"
    },
    {
        "name": "Tanqueray No. Ten",
        "description": "A small-batch gin crafted with fresh citrus fruits and botanicals for a smooth and crisp taste.",
        "price": 34.99,
        "rating": "0",
        "image_url": "gin_03.jpg",
        "image": "gin_03.jpg",
        "sku": "GIN003",
        "region": "Cameronbridge, Scotland"
    },
    {
        "name": "Monkey 47 Schwarzwald Dry Gin",
        "description": "A highly aromatic gin from the Black Forest, made with 47 botanicals including local herbs and spices.",
        "price": 59.99,
        "rating": "0",
        "image_url": "gin_04.jpg",
        "image": "gin_04.jpg",
        "sku": "GIN004",
        "region": "Black Forest, Germany"
    },
    {
        "name": "The Botanist Islay Dry Gin",
        "description": "A hand-crafted gin from Islay, featuring 22 foraged botanicals for a unique and complex flavor.",
        "price": 44.99,
        "rating": "0",
        "image_url": "gin_05.jpg",
        "image": "gin_05.jpg",
        "sku": "GIN005",
        "region": "Islay, Scotland"
    },
    {
        "name": "Plymouth Gin",
        "description": "A smooth and balanced gin with earthy notes and a slightly sweet finish, crafted in England.",
        "price": 32.99,
        "rating": "0",
        "image_url": "gin_06.jpg",
        "image": "gin_06.jpg",
        "sku": "GIN006",
        "region": "Plymouth, England"
    },
    {
        "name": "Roku Japanese Gin",
        "description": "A Japanese craft gin with six unique botanicals including sakura flower, yuzu peel, and green tea.",
        "price": 29.99,
        "rating": "0",
        "image_url": "gin_07.jpg",
        "image": "gin_07.jpg",
        "sku": "GIN007",
        "region": "Osaka, Japan"
    },
    {
        "name": "Beefeater 24",
        "description": "A sophisticated gin with 12 botanicals including Japanese sencha and Chinese green teas, creating a rich flavor.",
        "price": 34.99,
        "rating": "0",
        "image_url": "gin_08.jpg",
        "image": "gin_08.jp",
        "sku": "GIN008",
        "region": "London, England"
    },
    {
        "name": "Aviation American Gin",
        "description": "A smooth and balanced American gin with botanicals such as lavender, cardamom, and sarsaparilla.",
        "price": 27.99,
        "rating": "0",
        "image_url": "gin_09.jpg",
        "image": "gin_09.jpg",
        "sku": "GIN009",
        "region": "Oregon, USA"
    },
    {
        "name": "Nolet's Silver Dry Gin",
        "description": "A floral and fruit-forward gin with botanicals such as Turkish rose, peach, and raspberry.",
        "price": 49.99,
        "rating": "0",
        "image_url": "gin_10.jpg",
        "image": "gin_10.jpg",
        "sku": "GIN010",
        "region": "Schiedam, Netherlands"
    },
    {
        "name": "Sipsmith London Dry Gin",
        "description": "A quintessential London Dry gin with a classic blend of botanicals for a crisp and refreshing taste.",
        "price": 34.99,
        "rating": "0",
        "image_url": "gin_11.jpg",
        "image": "gin_11.jpg",
        "sku": "GIN011",
        "region": "London, England"
    },
    {
        "name": "Caorunn Small Batch Scottish Gin",
        "description": "A small-batch Scottish gin with locally foraged botanicals including rowan berry, heather, and dandelion.",
        "price": 39.99,
        "rating": "0",
        "image_url": "gin_12.jpg",
        "image": "gin_12.jpg",
        "sku": "GIN012",
        "region": "Speyside, Scotland"
    }
]

# Adding gin produt to DB
for product_data in products:
    Product.objects.create(
        category=gin_category,
        **product_data
    )

