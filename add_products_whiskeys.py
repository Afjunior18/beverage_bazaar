import os
from products.models import Product, Category

# create Whiskies category
whisky_category, created = Category.objects.get_or_create(type_product='Whiskies')

whisky_products = [
    {
        "name": "Macallan 18 Year Old Sherry Oak",
        "description": "A rich and full-bodied single malt Scotch whisky with notes of dried fruits, spices, and orange.",
        "price": 299.99,
        "rating": "0",
        "image_url": "media/whiskey_01.jpg",
        "image": "media/whiskey_01.jpg",
        "sku": "WHISKY001",
        "region": "Scotland"
    },
    {
        "name": "Yamazaki 12 Year Old",
        "description": "A delicate and smooth Japanese single malt whisky with flavors of honey, dried fruits, and a hint of smoke.",
        "price": 149.99,
        "rating": "0",
        "image_url": "media/whiskey_02.jpg",
        "image": "media/whiskey_02.jpg",
        "sku": "WHISKY002",
        "region": "Japan"
    },
    {
        "name": "Glenfiddich 21 Year Old Reserva Rum Cask Finish",
        "description": "A sophisticated single malt Scotch whisky with flavors of toffee, fig, and banana, finished in rum casks.",
        "price": 199.99,
        "rating": "0",
        "image_url": "media/whiskey_03.jpg",
        "image": "media/whiskey_03.jpg",
        "sku": "WHISKY003",
        "region": "Scotland"
    },
    {
        "name": "Lagavulin 16 Year Old",
        "description": "A robust and smoky single malt Scotch whisky with intense peat smoke and rich, complex flavors.",
        "price": 99.99,
        "rating": "0",
        "image_url": "media/whiskey_04.jpg",
        "image": "media/whiskey_04.jpg",
        "sku": "WHISKY004",
        "region": "Scotland"
    },
    {
        "name": "Jameson 18 Year Old Limited Reserve",
        "description": "A refined Irish whiskey with a blend of aged whiskeys, offering rich flavors of oak, caramel, and spice.",
        "price": 129.99,
        "rating": "0",
        "image_url": "media/whiskey_05.jpg",
        "image": "media/whiskey_05.jpg",
        "sku": "WHISKY005",
        "region": "Ireland"
    },
    {
        "name": "Balvenie 21 Year Old PortWood",
        "description": "A luxurious single malt Scotch whisky finished in port casks, with flavors of fruit, honey, and spice.",
        "price": 249.99,
        "rating": "0",
        "image_url": "media/whiskey_06.jpg",
        "image": "media/whiskey_06.jpg",
        "sku": "WHISKY006",
        "region": "Scotland"
    },
    {
        "name": "Ardbeg Uigeadail",
        "description": "A powerful and complex Islay single malt Scotch whisky with intense smoke, rich sweetness, and a full body.",
        "price": 79.99,
        "rating": "0",
        "image_url": "media/whiskey_07.jpg",
        "image": "media/whiskey_07.jpg",
        "sku": "WHISKY007",
        "region": "Scotland"
    },
    {
        "name": "Blanton’s Single Barrel Bourbon",
        "description": "A premium single barrel bourbon with a rich, full-bodied flavor profile featuring vanilla, caramel, and honey.",
        "price": 129.99,
        "rating": "0",
        "image_url": "media/whiskey_08.jpg",
        "image": "media/whiskey_08.jpg",
        "sku": "WHISKY008",
        "region": "USA"
    },
    {
        "name": "Hibiki Japanese Harmony",
        "description": "A harmonious blend of Japanese whiskies with delicate flavors of honey, orange peel, and white chocolate.",
        "price": 99.99,
        "rating": "0",
        "image_url": "media/whiskey_09.jpg",
        "image": "media/whiskey_09.jpg",
        "sku": "WHISKY009",
        "region": "Japan"
    },
    {
        "name": "Talisker 18 Year Old",
        "description": "A full-bodied and rich single malt Scotch whisky with flavors of dried fruits, smoke, and a hint of salt.",
        "price": 129.99,
        "rating": "0",
        "image_url": "media/whiskey_10.jpg",
        "image": "media/whiskey_10.jpg",
        "sku": "WHISKY010",
        "region": "Scotland"
    },
    {
        "name": "Redbreast 21 Year Old",
        "description": "A complex and well-balanced Irish whiskey with rich flavors of dried fruit, nuts, and spices.",
        "price": 199.99,
        "rating": "0",
        "image_url": "media/whiskey_11.jpg",
        "image": "media/whiskey_11.jpg",
        "sku": "WHISKY011",
        "region": "Ireland"
    },
    {
        "name": "Laphroaig 25 Year Old",
        "description": "A legendary Islay single malt Scotch whisky with intense peat smoke, rich oak, and a hint of sweetness.",
        "price": 499.99,
        "rating": "0",
        "image_url": "media/whiskey_12.jpg",
        "image": "media/whiskey_12.jpg",
        "sku": "WHISKY012",
        "region": "Scotland"
    }
]


# Adding whiskeys products to a DB
for whisky_data in whisky_products:
    Product.objects.create(
    category=whisky_category,
    **whisky_data
    )