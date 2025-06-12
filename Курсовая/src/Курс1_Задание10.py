products = [
    {"name": "Apple", "category": "fruit", "price": 120, "quantity": 10},
    {"name": "Banana", "category": "fruit", "price": 90, "quantity": 15},
    {"name": "Avocado", "category": "fruit", "price": 200, "quantity": 5},
    {"name": "Tomato", "category": "veggie", "price": 100, "quantity": 20},
    {"name": "Broccoli", "category": "veggie", "price": 300, "quantity": 8},
    {"name": "Carrot", "category": "veggie", "price": 100, "quantity": 25},
    {"name": "Cookie", "category": "sweets", "price": 200, "quantity": 12, "brand": "ABC"},
    {"name": "Donut", "category": "sweets", "price": 300, "quantity": 7, "brand": "XYZ"},
    {"name": "Cake", "category": "sweets", "price": 400, "quantity": 3, "brand": "DEF", "discount": 10},
    {"name": "Orange", "category": "fruit", "price": 150, "quantity": 18},
    {"name": "Lettuce", "category": "veggie", "price": 80, "quantity": 30, "organic": True},
    {"name": "Chocolate", "category": "sweets", "price": 250, "quantity": 10, "brand": "GHI", "flavor": "Dark"}
]
def group_products_by_category(products):
  dict_product = {}
  dict_product["fruit"] = []
  dict_product["veggie"] = []
  dict_product["sweets"] = []
  for product in products:
      if product.get("category") == "fruit":
        dict_product["fruit"].append(product)
      if product.get("category") == "veggie":
        dict_product["veggie"].append(product)
      if product.get("category") == "sweets":
        dict_product["sweets"].append(product)
  if dict_product["fruit"] == []:
        del dict_product["fruit"]

  if dict_product["veggie"] == []:
        del dict_product["veggie"]
  if dict_product["sweets"] == []:
        del dict_product["sweets"]
  return dict_product
print(group_products_by_category(products))