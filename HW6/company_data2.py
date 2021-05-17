product_list = [
    {
        "type": "1",
        "name": "shirt",
        "price": 30,
        "unit": "Dollar",
        "commission_groups": ["A", "B"]
    },
    {
        "type": "2",
        "name": "pants",
        "price": 50,
        "unit": "Dollar",
        "commission_groups": ["A", "C"]
    },
    {
        "type": "3",
        "name": "shoes",
        "price": 80,
        "unit": "Dollar",
        "commission_groups": ["B"]
    },
    {
        "type": "4",
        "name": "hat",
        "price": 20,
        "unit": "Dollar",
        "commission_groups": []
    }
]

markup_list = [
    {
        "product_type": "1",
        "lower_cost": 10,
        "upper_cost": 20,
        "unit": "percent",
        "lower_count": 10
    },
    {
        "product_type": "2",
        "lower_cost": 15,
        "upper_cost": 20,
        "unit": "percent",
        "lower_count": 10
    },
    {
        "product_type": "3",
        "lower_cost": 10,
        "upper_cost": 15,
        "unit": "percent",
        "lower_count": 5
    },
    {
        "product_type": "4",
        "lower_cost": 10,
        "upper_cost": 30,
        "unit": "percent",
        "lower_count": 20
    },
]

discount_list = [
    {
        "group_name": "A",
        "cost": 5,
        "unit": "percent",
        "users": [1001, 1002, 1003, 1005]
    },
    {
        "group_name": "B",
        "cost": 3,
        "unit": "Dollar",
        "users": [1001, 1003, 1006]
    },
    {
        "group_name": "C",
        "cost": 7,
        "unit": "percent",
        "users": [1001, 1002, 1004]
    }
]

user_list = [
    {
        "userid": 1001,
        "first_name": "Mohsen",
        "last_name": "Bayat",
    },
    {
        "userid": 1002,
        "first_name": "Sobhan",
        "last_name": "Taghadosi",
    },
    {
        "userid": 1003,
        "first_name": "Javad",
        "last_name": "Jafari",
    },
    {
        "userid": 1004,
        "first_name": "Masoud",
        "last_name": "Hosseini",
    },
    {
        "userid": 1005,
        "first_name": "Hassan",
        "last_name": "Zand",
    },
    {
        "userid": 1006,
        "first_name": "Ali",
        "last_name": "Ebadi",
    }
]

# #### # q1


def calculate_markup_percent(product_type, number_of_product):
    if number_of_product >= markup_list[product_type - 1]["lower_count"]:
        print('The markup will be', + markup_list[product_type - 1]["lower_cost"], 'percent')
    elif 1 <= number_of_product < markup_list[product_type - 1]["lower_count"]:
        m = (markup_list[product_type - 1]["upper_cost"] - markup_list[product_type - 1]["lower_cost"]) / \
            (1 - markup_list[product_type - 1]["lower_count"])
        markup = m * number_of_product - m + markup_list[product_type - 1]["upper_cost"]
        print('The markup will be', + markup.__round__(3), 'percent')
    else:
        print('You have not purchased any products')


print(calculate_markup_percent(1, 10))

print('----------------------------------------------------\n')

# #### # q2
# 'username': (dict(user_list[l]) for l in user_list if userid == user_list[l]["userid"])

# def Calculate_product_price(product_type, count, userid):
product_type = 1
count = 10
userid = 1002
if count >= markup_list[product_type - 1]["lower_count"]:
    price1 = count * product_list[product_type - 1]["price"]
    total_markup = markup_list[product_type - 1]["lower_cost"] * 0.01 * price1
    total_price = price1 + total_markup
    for item in product_list[product_type - 1]["commission_groups"]:
        if item in discount_list[product_type - 1]["group_name"] and userid in discount_list[product_type - 1]["users"]:
            if discount_list[product_type - 1]["unit"] == "percent":
                discount = discount_list[product_type - 1]["cost"] * 0.01 * total_price
                total_with_commission = total_price - discount
                print({'product_name': product_list[product_type - 1]["name"], 'total_price': total_price,
                       'total_with_commission': total_with_commission, 'discount': discount})
                break
            elif discount_list[product_type - 1]["unit"] == "Dollar":
                discount = discount_list[product_type - 1]["cost"]
                total_with_commission = total_price - discount
                print({'product_name': product_list[product_type - 1]["name"], 'total_price': total_price,
                       'total_with_commission': total_with_commission, 'discount': discount})
                break
        elif userid not in discount_list[product_type - 1]["users"]:
            print({'product_name': product_list[product_type - 1]["name"], 'total_price': total_price,
                   'total_with_commission': total_price, 'discount': 0})
            break
    else:
        print({'product_name': product_list[product_type - 1]["name"], 'total_price': total_price,
               'total_with_commission': total_price, 'discount': 0})
elif 1 <= count < markup_list[product_type - 1]["lower_count"]:
    m = (markup_list[product_type - 1]["upper_cost"] - markup_list[product_type - 1]["lower_cost"]) / (
            1 - markup_list[product_type - 1]["lower_count"])
    markup = m * count - m + markup_list[product_type - 1]["upper_cost"]
    price1 = count * product_list[product_type - 1]["price"]
    total_markup = markup * 0.01 * price1
    total_price = price1 + total_markup
    for item in product_list[product_type - 1]["commission_groups"]:
        if item in discount_list[product_type - 1]["group_name"] and userid in discount_list[product_type - 1]["users"]:
            if discount_list[product_type - 1]["unit"] == "percent":
                discount = discount_list[product_type - 1]["cost"] * 0.01 * total_price
                total_with_commission = total_price - discount
                print({'product_name': product_list[product_type - 1]["name"], 'total_price': total_price,
                       'total_with_commission': total_with_commission, 'discount': discount})
                break
            elif discount_list[product_type - 1]["unit"] == "Dollar":
                discount = discount_list[product_type - 1]["cost"]
                total_with_commission = total_price - discount
                print({'product_name': product_list[product_type - 1]["name"], 'total_price': total_price,
                       'total_with_commission': total_with_commission, 'discount': discount})
                break
        elif userid not in discount_list[product_type - 1]["users"]:
            print({'product_name': product_list[product_type - 1]["name"], 'total_price': total_price,
                   'total_with_commission': total_price, 'discount': 0})
            break
    else:
        print({'product_name': product_list[product_type - 1]["name"], 'total_price': total_price,
               'total_with_commission': total_price, 'discount': 0})
else:
    print('You have not purchased any products')