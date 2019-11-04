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

def print_recipe(name):
	if name in cookbook:
		recipe = cookbook[name]
		print(f"Recipe for {name}:")
		print("Ingredients list:", recipe['ingredients'])
		print(f"To be eaten for {recipe['meal']}.")
		print(f"Takes {recipe['prep_time']} minutes of cooking.")
	else:
		print(f"No recipe for {name} in the cookbook!")

def add_recipe(name, ingredients, meal, prep_time):
	if name not in cookbook:
		cookbook[name] = {
			'ingredients': ingredients,
			'meal': meal,
			'prep_time': prep_time
			}
		print(f"Added recipe for {name} to the cookbook!")

def del_recipe(name):
	if name in cookbook:
		del cookbook[name]
		print(f"Deleted recipe for {name} from the cookbook!")

def print_cookbook():
	recipes = list(cookbook)
	for name in recipes[:-1]:
		print_recipe(name)
		print()
	print_recipe(recipes[-1])

def prog():
	arg = "0"
	while arg != "5":
		print(f"{'':->59s}")
		print("Please select an option by typing the corresponding number:")
		print("1: Add a recipe")
		print("2: Delete a recipe")
		print("3: Print a recipe")
		print("4: Print the cookbook")
		print("5: Quit")
		arg = input(">> ")
		if arg == "1":
			print("Gimme a name!")
			name = input(">> ")
			print("Gimme ingredients!")
			ingredients = input(">> ").split()
			print("Gimme a meal!")
			meal = input(">> ")
			print("Gimme a prep time!")
			prep_time = input(">> ")
			try:
				add_recipe(name, ingredients, meal, prep_time)
			except:
				print("Format is wrong, bud... Try again!")
		elif arg == "2":
			recipes = list(cookbook)
			if len(recipes) == 0:
				print("No recipes in the cookbook!")
			else:
				print("Available recipes:")
				if len(recipes) > 1:
					print(", ".join(recipes[:-1]) + " and ", end='')
				print(recipes[-1] + ".")
				print("Please enter the name of the recipe you wish to delete:")
				name = input(">> ")
				del_recipe(name)
		elif arg == "3":
			recipes = list(cookbook)
			if len(recipes) == 0:
				print("No recipes in the cookbook!")
			else:
				print("Available recipes:")
				if len(recipes) > 1:
					print(", ".join(recipes[:-1]) + " and ", end='')
				print(recipes[-1] + ".")
				print("Please enter the name of the recipe you wish to print:")
				name = input(">> ")
				print_recipe(name)
		elif arg == "4":
			print_cookbook()
		elif arg == "5":
			print("Cookbook closed.")
		else:
			print("This option does not exist,", end=' ')
			print("please type the corresponding number.")
			print("To exit, enter 5.")
		print(f"{'':->59s}")
		print()

prog()
