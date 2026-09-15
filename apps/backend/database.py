import sqlite3

# define connection (used to connect to the database) and cursor (used to interact with the database, create and modify tables, insert and retrieve data)
connection = sqlite3.connect('recipebook.db')
cursor = connection.cursor()

# create ingredients table
command1 = """
CREATE TABLE IF NOT EXISTS ingredients (ID_ingredient INTEGER PRIMARY KEY, name_ingredient TEXT)"""

cursor.execute(command1)

# create recipes table
command2 = """
CREATE TABLE IF NOT EXISTS recipes (ID_recipe INTEGER PRIMARY KEY, name_recipe TEXT, category TEXT, estimated_time INT, servings INT)"""

cursor.execute(command2)

# create recipes_ingredients table
command3 = """
CREATE TABLE IF NOT EXISTS recipes_ingredients (ID_recipe INTEGER, ID_ingredient INTEGER, quantity FLOAT, unit TEXT, FOREIGN KEY(ID_recipe) REFERENCES recipes(ID_recipe), FOREIGN KEY(ID_ingredient) REFERENCES ingredients(ID_ingredient))"""

cursor.execute(command3)

# create instructions table
command4 = """
CREATE TABLE IF NOT EXISTS instructions (ID_instruction INTEGER PRIMARY KEY, ID_recipe INTEGER, step_number INT, instruction TEXT, FOREIGN KEY(ID_recipe) REFERENCES recipes(ID_recipe))"""

cursor.execute(command4)

# function to get the ID of an ingredient by name, or insert it if it doesn't exist
def get_ingredient_id(name):

    cursor.execute("""
        SELECT ID_ingredient
        FROM ingredients
        WHERE name_ingredient = ?
    """, (name,))

    result = cursor.fetchone()

    if result:
        return result[0]

    cursor.execute("""
        INSERT INTO ingredients (name_ingredient)
        VALUES (?)
    """, (name,))

    return cursor.lastrowid

# insert a recipe with ingredients and instructions
cursor.execute("""
    INSERT INTO recipes
    (name_recipe, category, estimated_time, servings)
    VALUES (?, ?, ?, ?)
""", ("Bolo de chocolate", "Sobremesa", 60, 8))

ID_recipe = cursor.lastrowid

# insert ingredients for the recipe
ingredients = [
    ("ovo", 2, "unidades"),
    ("farinha de trigo", 200, "g"),
    ("açúcar", 100, "g")
]

for name, quantity, unit in ingredients:

    ID_ingredient = get_ingredient_id(name)

    cursor.execute("""
        INSERT INTO recipes_ingredients
        (ID_recipe, ID_ingredient, quantity, unit)
        VALUES (?, ?, ?, ?)
    """, (ID_recipe, ID_ingredient, quantity, unit))

# insert instructions for the recipe
instructions = [
    "Misture os ovos com o açúcar.",
    "Adicione a farinha de trigo.",
    "Asse por aproximadamente 40 minutos."
]

for step_number, instruction in enumerate(instructions, start=1):

    cursor.execute("""
        INSERT INTO instructions
        (ID_recipe, step_number, instruction)
        VALUES (?, ?, ?)
    """, (ID_recipe, step_number, instruction))

# retrieve the recipe with its ingredients
cursor.execute("""
    SELECT
        recipes.name_recipe,
        ingredients.name_ingredient,
        recipes_ingredients.quantity,
        recipes_ingredients.unit
    FROM recipes
    JOIN recipes_ingredients
        ON recipes.ID_recipe = recipes_ingredients.ID_recipe
    JOIN ingredients
        ON recipes_ingredients.ID_ingredient = ingredients.ID_ingredient
    WHERE recipes.ID_recipe = ?
""", (ID_recipe,))

result = cursor.fetchall()

for row in result:
    print(row)


# retrieve the instructions of the recipe
cursor.execute("""
    SELECT
        recipes.name_recipe,
        instructions.step_number,
        instructions.instruction
    FROM recipes
    JOIN instructions
        ON recipes.ID_recipe = instructions.ID_recipe
    WHERE recipes.ID_recipe = ?
    ORDER BY instructions.step_number
""", (ID_recipe,))

result = cursor.fetchall()

for row in result:
    print(row)

connection.commit()
