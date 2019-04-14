
def make_pizza(size, *toppings):
    """描述要制作的比萨"""
    print("\nMaking a " + str(size) + 
          "-inch pizza with the following toppings:")
    for topping in toppings:
        print('- ' + topping)

def build_profile1(first, last, **user_info):
    """Create a dictionary that contains users' everything we know"""
    profile = {}
    profile['first_name'] = first
    profile['last_name'] = last
    for key, value in user_info.items():
        profile[key] = value
    return profile






























