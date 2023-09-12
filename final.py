#welcome 
name = input('welcome user ! what is your name ? ')
print(f'hello {name}, :) please answer these questions to find you a restaurant!')

#restaurants
restaurants = {
    'pizza': {'pizza hut': '$', 'dominos': '$','papa johns': '$','pizzaria':'$$','italian pizza':'$$$'},
    'burger': {'mcdonald,s':'$','elevation': '$$','gordon ramsey burger':'$$$'},
    'sushi': {'wasabi':'$','sushi mania':'$$','roka':'$$$'},
    'taco' : {'taco bell': '$', 'taco eataco': '$$', 'taco mex': '$$$'},
    'pasta' : {'grans pasta':'$','pastaaa':'$$','mac':'$$$'}
}

def choose_restaurants(food, budget):
    if food not in restaurants :
        return 'we dont have restaurants that serve that food'
    
    if budget not in ['$','$$','$$$']:
        return 'invalid budget range please use $, $$ , $$$'
    
    options = [restaurant for restaurant, price in restaurants[food].items() if price == budget]
    if not options :
        return f'Sorry, we could not find any {food} restaurants in your are within your budget'
    return f"Here are your {food} restaurant options within your budget ({budget}): {', '.join(options)}"


#user input 
food_input = input('what do you want to eat? please enter your answer in singular form!')
budget_input = input('what is your budget?. enter $ for cheap, $$ for moderate , $$$ for expensive: ')

# Get restaurant recommendation
recommendation = choose_restaurants(food_input ,budget_input)
print(recommendation)
print('enjoy your food :)')




