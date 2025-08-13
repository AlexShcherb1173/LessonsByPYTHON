products = [{"name": "Apple", "category": "fruit", "price": 120, "quantity": 10},
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
    {"name": "Chocolate", "category": "sweets", "price": 250, "quantity": 10, "brand": "GHI", "flavor": "Dark"}]
def average_price_per_category(products):
      price_fr = 0
      price_vg = 0
      price_sw = 0
      count_fr = 0
      count_vg = 0
      count_sw = 0
      dict_avg = {}
      for product in products:
          if product.get("category") == "fruit":
                price_fr += product.get("price")
                count_fr += 1
          elif product.get("category") == "veggie":
                price_vg += product.get("price")
                count_vg += 1
          elif product.get("category") == "sweets":
                price_sw += product.get("price")
                count_sw += 1
          if count_fr > 0:
            dict_avg["fruit"] = round(price_fr/count_fr, 1)
          if count_vg > 0:
            dict_avg["veggie"] = round(price_vg/count_vg, 1)
          if count_sw > 0:
             dict_avg["sweets"] = round(price_sw/count_sw, 1)
      return dict_avg
print(average_price_per_category(products))
