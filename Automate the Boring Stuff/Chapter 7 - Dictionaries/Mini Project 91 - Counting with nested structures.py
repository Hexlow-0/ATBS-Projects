
from collections import defaultdict
from collections import Counter

raw_data = [
    {
        "continent": "Asia",
        "countries": [
            {
                "name": "Japan",
                "cities": [
                    {
                        "name": "Tokyo",
                        "population": 14000000,
                        "orders": [
                            {
                                "order_id": 1001,
                                "product": "laptop",
                                "category": "electronics",
                                "qty": 2,
                                "unit_price": 1200,
                                "status": "shipped",
                                "date": "2025-01-05",
                                "customer": {
                                    "id": 501,
                                    "name": "Alice",
                                    "segment": "business"
                                }
                            },
                            {
                                "order_id": 1002,
                                "product": "phone",
                                "category": "electronics",
                                "qty": 3,
                                "unit_price": 900,
                                "status": "delivered",
                                "date": "2025-01-06",
                                "customer": {
                                    "id": 502,
                                    "name": "Bob",
                                    "segment": "consumer"
                                }
                            },
                            {
                                "order_id": 1003,
                                "product": "monitor",
                                "category": "electronics",
                                "qty": 2,
                                "unit_price": 350,
                                "status": "pending",
                                "date": "2025-01-07",
                                "customer": {
                                    "id": 503,
                                    "name": "Carol",
                                    "segment": "consumer"
                                }
                            }
                        ]
                    },
                    {
                        "name": "Osaka",
                        "population": 2700000,
                        "orders": [
                            {
                                "order_id": 1004,
                                "product": "tablet",
                                "category": "electronics",
                                "qty": 2,
                                "unit_price": 700,
                                "status": "delivered",
                                "date": "2025-01-08",
                                "customer": {
                                    "id": 504,
                                    "name": "David",
                                    "segment": "business"
                                }
                            },
                            {
                                "order_id": 1005,
                                "product": "phone",
                                "category": "electronics",
                                "qty": 1,
                                "unit_price": 950,
                                "status": "cancelled",
                                "date": "2025-01-09",
                                "customer": {
                                    "id": 505,
                                    "name": "Emma",
                                    "segment": "consumer"
                                }
                            }
                        ]
                    },
                    {
                        "name": "Kyoto",
                        "population": 1500000,
                        "orders": [
                            {
                                "order_id": 1006,
                                "product": "keyboard",
                                "category": "accessories",
                                "qty": 5,
                                "unit_price": 80,
                                "status": "shipped",
                                "date": "2025-01-10",
                                "customer": {
                                    "id": 506,
                                    "name": "Frank",
                                    "segment": "business"
                                }
                            }
                        ]
                    }
                ]
            },
            {
                "name": "China",
                "cities": [
                    {
                        "name": "Beijing",
                        "population": 21500000,
                        "orders": [
                            {
                                "order_id": 1007,
                                "product": "laptop",
                                "category": "electronics",
                                "qty": 4,
                                "unit_price": 1100,
                                "status": "delivered",
                                "date": "2025-01-11",
                                "customer": {
                                    "id": 507,
                                    "name": "Grace",
                                    "segment": "business"
                                }
                            },
                            {
                                "order_id": 1008,
                                "product": "tablet",
                                "category": "electronics",
                                "qty": 2,
                                "unit_price": 650,
                                "status": "pending",
                                "date": "2025-01-12",
                                "customer": {
                                    "id": 508,
                                    "name": "Henry",
                                    "segment": "consumer"
                                }
                            }
                        ]
                    },
                    {
                        "name": "Shanghai",
                        "population": 24800000,
                        "orders": [
                            {
                                "order_id": 1009,
                                "product": "phone",
                                "category": "electronics",
                                "qty": 6,
                                "unit_price": 850,
                                "status": "shipped",
                                "date": "2025-01-13",
                                "customer": {
                                    "id": 509,
                                    "name": "Ivy",
                                    "segment": "consumer"
                                }
                            }
                        ]
                    }
                ]
            },
            {
                "name": "India",
                "cities": [
                    {
                        "name": "Mumbai",
                        "population": 20400000,
                        "orders": [
                            {
                                "order_id": 1010,
                                "product": "headphones",
                                "category": "audio",
                                "qty": 10,
                                "unit_price": 120,
                                "status": "delivered",
                                "date": "2025-01-14",
                                "customer": {
                                    "id": 510,
                                    "name": "Jack",
                                    "segment": "consumer"
                                }
                            }
                        ]
                    }
                ]
            }
        ]
    },
    {
        "continent": "Europe",
        "countries": [
            {
                "name": "Germany",
                "cities": [
                    {
                        "name": "Berlin",
                        "population": 3700000,
                        "orders": [
                            {
                                "order_id": 1011,
                                "product": "phone",
                                "category": "electronics",
                                "qty": 2,
                                "unit_price": 950,
                                "status": "delivered",
                                "date": "2025-01-15",
                                "customer": {
                                    "id": 511,
                                    "name": "Kate",
                                    "segment": "business"
                                }
                            },
                            {
                                "order_id": 1012,
                                "product": "laptop",
                                "category": "electronics",
                                "qty": 3,
                                "unit_price": 1400,
                                "status": "shipped",
                                "date": "2025-01-16",
                                "customer": {
                                    "id": 512,
                                    "name": "Leo",
                                    "segment": "consumer"
                                }
                            }
                        ]
                    },
                    {
                        "name": "Munich",
                        "population": 1500000,
                        "orders": [
                            {
                                "order_id": 1013,
                                "product": "mouse",
                                "category": "accessories",
                                "qty": 12,
                                "unit_price": 40,
                                "status": "pending",
                                "date": "2025-01-17",
                                "customer": {
                                    "id": 513,
                                    "name": "Mia",
                                    "segment": "consumer"
                                }
                            }
                        ]
                    }
                ]
            },
            {
                "name": "France",
                "cities": [
                    {
                        "name": "Paris",
                        "population": 2100000,
                        "orders": [
                            {
                                "order_id": 1014,
                                "product": "smartwatch",
                                "category": "wearables",
                                "qty": 4,
                                "unit_price": 300,
                                "status": "delivered",
                                "date": "2025-01-18",
                                "customer": {
                                    "id": 514,
                                    "name": "Noah",
                                    "segment": "business"
                                }
                            }
                        ]
                    }
                ]
            }
        ]
    },
    {
        "continent": "North America",
        "countries": [
            {
                "name": "United States",
                "cities": [
                    {
                        "name": "New York",
                        "population": 8400000,
                        "orders": [
                            {
                                "order_id": 1015,
                                "product": "server",
                                "category": "infrastructure",
                                "qty": 2,
                                "unit_price": 5000,
                                "status": "shipped",
                                "date": "2025-01-19",
                                "customer": {
                                    "id": 515,
                                    "name": "Olivia",
                                    "segment": "enterprise"
                                }
                            }
                        ]
                    },
                    {
                        "name": "San Francisco",
                        "population": 810000,
                        "orders": [
                            {
                                "order_id": 1016,
                                "product": "laptop",
                                "category": "electronics",
                                "qty": 7,
                                "unit_price": 1800,
                                "status": "delivered",
                                "date": "2025-01-20",
                                "customer": {
                                    "id": 516,
                                    "name": "Paul",
                                    "segment": "enterprise"
                                }
                            }
                        ]
                    }
                ]
            }
        ]
    }
]

total_product_quantities = {}
orders_per_continent = {}
most_rev_per_continent = {}
country_populations = {}

for data in raw_data:
    print(f"Continent: {data['continent']}")

    for country in data['countries']:
        print(f"  Country: {country['name']}")

        for city in country['cities']:

            print(f"    City: {city['name']}")
            print(f"    Population: {city['population']}\n")

            country_populations[country['name']] = country_populations.get(country['name'], 0) + city['population']

            for order in city['orders']:

                print(f"      Order ID: {order['order_id']}")
                print(f"      Product: {order['product']}")
                print(f"      Category: {order['category']}")
                print(f"      Quantity: {order['qty']}")
                print(f"      Price: {order['unit_price']}")
                print(f"      Status: {order['status']}\n")

                total_product_quantities[order['product']] = total_product_quantities.get(order['product'], 0) + order['qty']

                if order['order_id']:
                    orders_per_continent[data['continent']] = orders_per_continent.get(data['continent'], 0) + 1

                most_rev_per_continent[data['continent']] = most_rev_per_continent.get(data['continent'], 0) + order['unit_price']

                print("       Customer data:\n")

                for customer_data, data_values in order['customer'].items():

                    print(f"       {customer_data}: {data_values}")

                print()

print()

print("=" * 40)
print("SUMMARY".center(40))
print("=" * 40)
print()

print()
print("=" * 40)
print("TOTAL PRODUCT QUANTITIES".center(40))
print("=" * 40)
print()

for product, quantities in total_product_quantities.items():

    print(f"{product}: {quantities}")

print()
print("=" * 40)
print("ORDERS PER CONTINENT".center(40))
print("=" * 40)
print()

for continent, order_num in orders_per_continent.items():

    print(f"{continent}: {order_num}")

print()
print("=" * 40)
print("REVENUE PER CONTINENT".center(40))
print("=" * 40)
print()

for continent, revenue in most_rev_per_continent.items():

    print(f"{continent}: ${revenue:,}")

print()
print("=" * 40)
print("COUNTRY POPULATION COUNT".center(40))
print("=" * 40)
print()

for country, population in country_populations.items():

    print(f"{country}: {population:,}")

print()
print("=" * 40)
print("STATS".center(40))
print("=" * 40)
print()

# Best selling product
product, sold = max(total_product_quantities.items(), key=lambda x: x[1])
print(f"Best selling product: {product} with {sold} units!\n")

# Continent with most orders
continent_orders, orders = max(orders_per_continent.items(), key=lambda x: x[1])
print(f"Highest orders by continent: {continent} with {orders} orders!\n")

# Continent with product, sold = max(total_product_quantities.items(), key=lambda x: x[1])
continent_rev, revenue = max(most_rev_per_continent.items(), key=lambda x: x[1])
print(f"Continent with most revenue: {continent_rev} with ${revenue:,} total!\n")

country, population = max(country_populations.items(), key=lambda x: x[1])
print(f"Highest country population: {country} with {population:,} total!\n")



# Country with highest population
