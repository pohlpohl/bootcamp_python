cookbook = {
	'sandwich': {
		'ingredients': ['ham', 'bread', 'cheese', 'tomatoes'],
		'meal': 'lunch',
		'prep_time': 10
	},
	'cake': {
		'ingredients': ['flour', 'sugar', 'eggs'],
		'meal': 'dessert',
		'prep_time': 60
	},
	'salad': {
		'ingredients': ['avocado', 'arugula', 'tomatoes', 'spinach'],
		'meal': 'lunch',
		'prep_time': 15
	}
}

def recipe(name):
	print("Recipe for " + name + ":")
	print("The " + name + " is a " + cookbook[name]['meal'] + " that will take you "  + str(cookbook[name]['prep_time']) + " minutes to make.")
	print("Just mix " + (", ".join(cookbook[name]['ingredients'][i] for i in range(len(cookbook[name]['ingredients']) - 1))) + " and " + cookbook[name]['ingredients'][-1] + " and pray for the best...")

def del_recipe(name):
	cookbook.pop(name)

def add_recipe(name, ingredients, meal, prep_time):
	cookbook[name] = {
		'meal': meal,
		'prep_time': prep_time,
	}
	cookbook[name]['ingredients'] = ingredients

def print_names():
	print("There are " + str(len(cookbook)) + " recipes : " + (", ".join(i for i in cookbook.keys())))

usr_input = 0
while int(usr_input) != 5:
	usr_input = input('Please select an option by typing the corresponding number:\n1: Add a recipe\n2: Delete a recipe\n3: Print a recipe\n4: Print the cookbook\n5: Quit\n>> ')
	while not usr_input.isdigit() or not 1 <= int(usr_input) <= 5:
		usr_input = input("This option does not exist, please type the corresponding number.\nTo exit, enter 5.\n>> ")
	if int(usr_input) == 1:
		recipe_name = str(input("Great ! name your recipe :\n>> "))
		recipe_meal = str(input("What meal is it ?\n>> "))
		recipe_time = str(input("How long does it take to make your recipe?\n>> "))
		while not recipe_time.isdigit():
			recipe_time = str(input("Please enter a number,\nHow long does it take to make your recipe?\n>> "))
		recipe_ingredients = str(input("Specify the ingredients, separate each one by a comma\n>> "))
		add_recipe(recipe_name, recipe_ingredients.split(","), recipe_meal, recipe_time)
		print("Your recipe was created ! Go check it out")
		print(cookbook[recipe_name])
	if int(usr_input) == 2:
		recipe_del = str(input("Which recipe do you want to delete ? Type 'none' to exit\n>> "))
		while recipe_del not in cookbook and recipe_del != 'none':
			recipe_del = str(input("This recipe does not exist,\nWhich recipe do you want to delete ? Type 'none' to exit\n>> "))
		if recipe_del in cookbook:
			del_recipe(recipe_del)
			print("Your recipe was deleted !")
	if int(usr_input) == 3:
		recipe_print = str(input("Which recipe do you want to print ? Type 'none' to exit\n>> "))
		while recipe_print not in cookbook and recipe_print != 'none':
			recipe_print = str(input("This recipe does not exist,\nWhich recipe do you want to print ? Type 'none' to exit\n>> "))
		if recipe_print in cookbook:
			recipe(recipe_print)
			str(input("Press any key to continue"))
	if int(usr_input) == 4:
		print_names()
		str(input("Press any key to continue"))
print("Cookbook closed.")
