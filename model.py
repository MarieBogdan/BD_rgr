import psycopg2
import random
import time

starter = ["Tomato Soup", "Minestrone", "Clam Chowder", "Butternut Squash Soup", "French Onion Soup",
           "Chicken Noodle Soup",
           "Gazpacho", "Lentil Soup", "Split Pea Soup", "Potato Leek Soup", "Cream of Mushroom Soup", "Miso Soup",
           "Chicken and Rice Soup", "Beef Stew", "Goulash", "Chili", "Tortilla Soup", "Corn Chowder",
           "Cabbage Soup",
           "Borscht", "Wonton Soup", "Hot and Sour Soup", "Egg Drop Soup", "Pho", "Ramen", "Chow Mein", "Udon Soup",
           "Vichyssoise", "Gazpacho Andaluz", "Avgolemono Soup", "Chicken and Dumplings", "Matzo Ball Soup",
           "Beef Barley Soup", "New England Clam Chowder", "Lobster Bisque", "Oyster Stew", "Tom Yum Soup",
           "Tom Kha Gai", "Beef Noodle Soup", "Beef and Vegetable Soup", "Minced Beef Soup", "Meatball Soup",
           "Chicken Gumbo", "Jambalaya", "Crawfish Etouffee", "Shrimp and Corn Chowder",
           "Chicken and Sausage Gumbo",
           "Seafood Bisque", "Chicken Tortilla Soup", "Chicken Posole", "Cheddar Broccoli Soup", "Pumpkin Soup",
           "Carrot Ginger Soup", "Broccoli Cheddar Soup", "Mushroom Bisque", "Spinach Soup", "Leek and Potato Soup",
           "Chicken and Wild Rice Soup", "Cream of Asparagus Soup", "Cream of Artichoke Soup",
           "Roasted Red Pepper Soup",
           "Avocado Soup", "Asparagus and Pea Soup", "Beet Soup", "Sweet Potato Soup", "Cream of Celery Soup",
           "Spinach and Lentil Soup", "Potato Corn Chowder", "Cream of Spinach Soup", "Onion and Garlic Soup",
           "Cream of Tomato Soup", "Italian Wedding Soup", "Bok Choy Soup", "Roasted Butternut Squash Soup",
           "Navy Bean Soup", "Wild Mushroom Soup", "Tuscan Bean Soup", "Chickpea Soup", "Moroccan Lentil Soup",
           "Pea and Ham Soup", "Cream of Chicken Soup", "Cream of Turkey Soup", "Chicken and Leek Soup",
           "Chicken Mulligatawny",
           "Chicken and Rice Soup with Saffron", "Cream of Chicken and Mushroom Soup",
           "Cream of Chicken and Rice Soup",
           "Chicken and Lentil Soup", "Chicken and Barley Soup", "Chicken and Black Bean Soup",
           "Chicken and Couscous Soup",
           "Chicken and Chickpea Soup", "Chicken and Sweet Potato Soup", "Chicken and Corn Soup",
           "Chicken and Potato Soup",
           "Chicken and Mushroom Soup with Thyme", "Chicken and Rice Soup with Curry", "Chicken and Vegetable Soup",
           "Chicken and Rice Soup with Lemon", "Chicken and Rice Soup with Cilantro"]

main_course = ["Spaghetti Carbonara", "Beef Stroganoff", "Chicken Alfredo", "Chicken Parmesan", "Shrimp Scampi",
               "Pad Thai", "Beef and Broccoli",
               "Lobster Bisque", "Lamb Kebabs", "Chicken Fajitas", "Garlic Butter Shrimp",
               "Beef and Mushroom Stir-Fry",
               "Honey Glazed Salmon", "Lemon Garlic Butter Shrimp", "Sesame Chicken", "Cajun Jambalaya",
               "Mushroom Risotto",
               "Chicken Tikka Masala", "Baked Ziti", "Crispy Pork Belly", "Lemon Butter Garlic Shrimp",
               "Chicken Marsala",
               "Sweet and Sour Chicken", "Tandoori Chicken", "Coconut Curry Chicken", "Chicken and Rice Casserole",
               "Honey Garlic Shrimp", "Pork Chops with Apples", "Chicken Stroganoff", "Beef and Noodles",
               "Honey Mustard Salmon",
               "Lemon Pepper Chicken", "Mongolian Beef", "Teriyaki Chicken", "Creamy Garlic Shrimp",
               "Garlic Parmesan Shrimp",
               "Beef with Broccoli", "Lemon Herb Roast Chicken", "Shrimp and Grits", "Pineapple Teriyaki Chicken",
               "Garlic Parmesan Chicken", "Orange Chicken", "Chicken Cacciatore", "Peppered Steak",
               "Shrimp Fettuccine Alfredo",
               "Chicken Coconut Curry", "Beef Stir-Fry", "Lemon Pepper Salmon", "Beef and Vegetable Stir-Fry",
               "Pork Tenderloin with Apples", "Chicken Fried Rice", "Garlic Butter Shrimp Pasta", "Shrimp Stir-Fry",
               "Beef and Green Bean Stir-Fry", "Chicken and Mushroom Risotto", "Lemon Herb Roast Salmon",
               "Chicken Florentine",
               "Honey Mustard Chicken", "Chicken Gumbo", "Teriyaki Beef", "Pork and Apple Stir-Fry",
               "Creamy Garlic Shrimp Pasta",
               "Garlic Parmesan Shrimp Pasta", "Beef and Asparagus Stir-Fry", "Shrimp Alfredo",
               "Chicken and Leek Risotto",
               "Lemon Herb Roast Pork", "Beef and Snow Pea Stir-Fry", "Chicken Enchiladas", "Miso Salmon",
               "Chicken and Artichoke Risotto",
               "Garlic Butter Shrimp and Broccoli", "Chicken and Spinach Risotto", "Beef and Carrot Stir-Fry",
               "Orange Shrimp",
               "Chicken and Sun-Dried Tomato Risotto", "Teriyaki Chicken and Pineapple",
               "Beef and Bok Choy Stir-Fry",
               "Pork and Pear Stir-Fry", "Chicken and Mango Risotto", "Shrimp Scampi Linguine",
               "Garlic Butter Shrimp and Asparagus",
               "Chicken and Red Pepper Risotto", "Lemon Herb Roast Lamb", "Beef and Red Pepper Stir-Fry",
               "Garlic Parmesan Shrimp and Broccoli", "Teriyaki Beef and Broccoli", "Chicken and Zucchini Risotto",
               "Honey Mustard Chicken and Potatoes", "Creamy Garlic Shrimp and Spinach",
               "Beef and Eggplant Stir-Fry",
               "Garlic Butter Shrimp and Spinach", "Chicken and Asparagus Risotto",
               "Lemon Herb Roast Chicken and Potatoes",
               "Mongolian Beef and Broccoli", "Chicken and Mushroom Risotto", "Lemon Pepper Salmon and Asparagus",
               "Beef and Snow Pea Stir-Fry", "Pork and Brussels Sprouts Stir-Fry",
               "Garlic Parmesan Shrimp and Spinach",
               "Chicken and Butternut Squash Risotto"]
dessert = ["Chocolate Cake", "Apple Pie", "Cheesecake", "Strawberry Shortcake",
           "Tiramisu", "Brownies", "Red Velvet Cake", "Ice Cream Sundae", "Lemon Bars", "Pumpkin Pie",
           "Chocolate Chip Cookies",
           "Key Lime Pie", "Banana Split", "Carrot Cake", "Cupcakes", "Rice Pudding", "Blueberry Muffins",
           "Peach Cobbler",
           "Fruit Salad", "Panna Cotta", "Chocolate Mousse", "Lava Cake", "Coconut Macaroons", "Bread Pudding",
           "Cherry Pie",
           "Peanut Butter Cookies", "Caramel Flan", "Strawberry Cheesecake", "Chocolate Brownies", "Apple Crisp",
           "Pecan Pie",
           "Lemon Meringue Pie", "Oatmeal Cookies", "Chocolate Fondue", "Vanilla Ice Cream", "Lemon Sorbet",
           "Fudge Brownies",
           "Chocolate Eclairs", "Creme Brulee", "Raspberry Sorbet", "Chocolate Souffle", "Butter Pecan Ice Cream",
           "Tropical Fruit Salad", "Fruit Tart", "Cheese Danish", "Molten Chocolate Cake",
           "Chocolate Covered Strawberries",
           "Cannoli", "Peach Melba", "Chocolate Pudding", "Gelato", "Cherry Cheesecake", "Cinnamon Rolls",
           "Pineapple Upside-Down Cake", "Mango Sorbet", "Caramel Apple", "Strawberry Shortcake",
           "Chocolate Lava Cake",
           "White Chocolate Mousse", "Pumpkin Cheesecake", "Pistachio Ice Cream", "Cherry Pie", "Oreo Cookies",
           "Key Lime Pie",
           "Fruit Sorbet", "Chocolate Tiramisu", "Caramel Flan", "Lemon Bars", "Chocolate Muffins", "Rhubarb Pie",
           "Snickerdoodle Cookies", "Banana Cream Pie", "Toasted Marshmallows", "Berry Parfait",
           "Ricotta Cheesecake",
           "Pineapple Cake", "Lemon Tarts", "Coconut Cream Pie", "Peanut Butter Brownies", "Chocolate Crepes",
           "Mint Chocolate Chip Ice Cream", "Peach Cobbler", "Lemon Cake", "Blueberry Pie",
           "Chocolate Creme Brulee",
           "Red Velvet Cupcakes", "Butterscotch Pudding", "Apple Turnovers", "Pumpkin Muffins", "Cinnamon Bread",
           "Berry Trifle", "Vanilla Panna Cotta", "Mango Sorbet", "Cheese Blintzes", "Chocolate Lava Cake",
           "Chocolate Cherry Trifle", "Caramel Popcorn", "Raspberry Mousse", "Butter Pecan Cake", "Kiwi Sorbet",
           "Pineapple Upside-Down Cake", "Ricotta Cannoli", "Peach Melba", "Lemon Meringue Pie"]
category_type = ["Starter", "Main course", "Dessert"]
category_difficulty = ["Difficult", "Medium", "Easy"]
country = ["Albania", "Algeria", "Andorra", "Angola", "Antigua and Barbuda", "Argentina", "Armenia",
           "Australia", "Austria", "Azerbaijan", "Bahamas", "Bahrain", "Bangladesh", "Barbados", "Belgium",
           "Belize", "Benin", "Bhutan", "Bolivia", "Bosnia and Herzegovina", "Botswana", "Brazil", "Brunei", "Bulgaria",
           "Burkina Faso", "Burundi", "Cabo Verde", "Cambodia", "Cameroon", "Canada", "Central African Republic",
           "Chad", "Chile", "Colombia", "Comoros", "Congo (Congo-Brazzaville)", "Costa Rica", "Croatia",
           "Cuba", "Cyprus", "Czechia (Czech Republic)", "Democratic Republic of the Congo (Congo-Kinshasa)",
           "Denmark", "Djibouti", "Dominica", "Dominican Republic", "East Timor", "Ecuador", "Egypt", "El Salvador",
           "Equatorial Guinea", "Eritrea", "Estonia", "Eswatini", "Ethiopia", "Fiji", "Finland", "France", "Gabon",
           "Gambia", "Georgia", "Germany", "Ghana", "Greece", "Grenada", "Guatemala", "Guinea", "Guinea-Bissau",
           "Guyana", "Haiti", "Honduras", "Hungary", "Iceland", "India", "Indonesia", "Iran", "Iraq", "Ireland",
           "Israel", "Italy", "Ivory Coast", "Jamaica", "Japan", "Jordan", "Kazakhstan", "Kenya", "Kiribati",
           "Kuwait", "Kyrgyzstan", "Laos", "Latvia", "Lebanon", "Lesotho", "Liberia", "Libya", "Liechtenstein",
           "Lithuania"]
ingredients = ["Salt", "Pepper", "Garlic", "Onion", "Olive oil", "Lemon", "Basil", "Parsley", "Thyme", "Rosemary",
               "Sage", "Oregano", "Cumin", "Coriander", "Cilantro", "Paprika", "Cayenne pepper", "Ginger", "Turmeric",
               "Cinnamon", "Nutmeg", "Cloves", "Bay leaves", "Mustard seeds", "Soy sauce", "Worcestershire sauce",
               "Vinegar", "Ketchup", "Mayonnaise", "Mustard", "Honey", "Brown sugar", "White sugar", "Maple syrup",
               "Molasses", "Peanut butter", "Almond butter", "Sesame seeds", "Coconut milk", "Sour cream", "Yogurt",
               "Milk", "Cream", "Butter", "Cheese", "Eggs", "Flour", "Cornstarch", "Baking powder", "Baking soda",
               "Cocoa powder", "Vanilla extract", "Almond extract", "Lime zest", "Orange zest", "Pecans", "Walnuts",
               "Cashews", "Hazelnuts", "Macadamia nuts", "Pistachios", "Sunflower seeds", "Pumpkin seeds", "Quinoa",
               "Rice", "Pasta", "Bread", "Couscous", "Barley", "Bulgur", "Lentils", "Chickpeas", "Black beans",
               "Kidney beans", "Cannellini beans", "Lima beans", "Green peas", "Carrots", "Celery", "Bell peppers",
               "Cucumbers", "Tomatoes", "Zucchini", "Mushrooms", "Spinach", "Kale", "Lettuce", "Cabbage", "Broccoli",
               "Cauliflower", "Eggplant", "Asparagus", "Green beans", "Radishes", "Beets", "Sweet potatoes", "Potatoes",
               "Pumpkin", "Butternut squash", "Acorn squash", "Red onion", "Yellow onion", "Red cabbage",
               "White cabbage"]


class Model:
    def __init__(self):
        self.conn = psycopg2.connect(
            dbname='postgres',
            user='postgres',
            password='marichka1104',
            host='localhost',
            port=5432
        )
        self.create_tables()

    def create_tables(self):
        c = self.conn.cursor()
        c.execute('CREATE EXTENSION IF NOT EXISTS "uuid-ossp";')

        c.execute("SELECT EXISTS (SELECT 1 FROM information_schema.tables WHERE table_name = 'Author')")
        c.execute("SELECT EXISTS (SELECT 1 FROM information_schema.tables WHERE table_name = 'Recipe')")
        c.execute("SELECT EXISTS (SELECT 1 FROM information_schema.tables WHERE table_name = 'Ingredients')")
        c.execute("SELECT EXISTS (SELECT 1 FROM information_schema.tables WHERE table_name = 'Category')")
        c.execute("SELECT EXISTS (SELECT 1 FROM information_schema.tables WHERE table_name = 'Includes')")
        c.execute("SELECT EXISTS (SELECT 1 FROM information_schema.tables WHERE table_name = 'Consists')")
        table_exists = c.fetchone()

        if not table_exists:
            c.execute('''
                CREATE TABLE Author (
                    Login TEXT PRIMARY KEY,
                    Name TEXT NOT NULL,
                    Password TEXT NOT NULL
                )
            ''')
            c.execute('''
                CREATE TABLE Recipe (
                    Recipe_ID TEXT PRIMARY KEY,
                    Author_login TEXT,
                    Name TEXT NOT NULL,
                    Calories INT,
                    Time TIME,
                    Photos TEXT,
                    Steps TEXT NOT NULL,
                    FOREIGN KEY(Author_login) 
                        REFERENCES Author(Login)
                        
                )
            ''')
            c.execute('''
                CREATE TABLE Ingredients (
                    Ingredient_ID TEXT PRIMARY KEY,
                    Name TEXT NOT NULL,
                )
            ''')
            c.execute('''
                CREATE TABLE Category (
                    Category_ID TEXT PRIMARY KEY,
                    Difficulty TEXT,
                    Type TEXT NOT NULL,
                    Country TEXT,
                )
            ''')
            c.execute('''
                CREATE TABLE Includes (
                Category_FK TEXT,
                Recipe_FK TEXT, 
                PRIMARY KEY(Category_FK,Recipe_FK),
                FOREIGN KEY(Category_FK) 
                    REFERENCES Category(Category_ID)
                FOREIGN KEY(Recipe_FK) 
                    REFERENCES Recipe(Recipe_ID)
                )
            ''')
            c.execute('''
                CREATE TABLE Consists (
                    Recipe_FK TEXT, 
                    Ingredients_FK TEXT,
                    Amount INT NOT NULL,
                    Measurement unit TEXT NOT NULL,
                    Temperature INT,
                    PRIMARY KEY (Recipe_FK, Ingredients_FK),
                    FOREIGN KEY(Ingredients_FK) 
                        REFERENCES Ingredients(Ingredients_ID)                      
                    FOREIGN KEY(Recipe_FK) 
                        REFERENCES Recipe(Recipe_ID)
            ''')

        self.conn.commit()

    def add_author(self, name, password):
        c = self.conn.cursor()
        c.execute('''
            INSERT INTO "Author" ("Login", "Name", "Password")
            VALUES (
                chr(trunc(65 + random() * 50)::int) || chr(trunc(65 + random() * 25)::int) ||
                chr(trunc(65 + random() * 25)::int) || chr(trunc(65 + random() * 25)::int),
                %s, %s
            )
            RETURNING "Login"
        ''', (name, password))
        self.conn.commit()
        return c.fetchone()

    def add_recipe(self, login, name, calories, cooking_time, photos, steps, difficulty, type_, recipe_country):
        c = self.conn.cursor()

        c.execute('''
        INSERT INTO "Recipe" ("Recipe_ID", "Author_login", "Name", "Calories", "Time", "Photos", "Steps") 
        VALUES (md5(random()::text), %s, %s, %s, %s, %s, %s)  
        RETURNING "Recipe_ID" 
        ''', (login, name, calories, cooking_time, photos, steps))
        recipe_id = c.fetchone()

        c.execute('SELECT "Category_ID" FROM "Category" WHERE "Difficulty" = %s AND "Type" = %s AND "Country" = %s',
                  (difficulty, type_, recipe_country))
        category_id = c.fetchone()

        if not category_id:
            category_id = self.add_category(difficulty, type_, recipe_country)

        c.execute('INSERT INTO "Includes" ("Recipe_FK", "Category_FK") VALUES (%s, %s)', (recipe_id, category_id))

        self.conn.commit()

        return recipe_id

    def add_ingredient(self, name, recipe_id, amount, measurement_unit, temperature):
        c = self.conn.cursor()
        c.execute('''
            INSERT INTO "Ingredients" ("Ingredients_ID", "Name") 
            VALUES (md5(random()::text), %s) 
            RETURNING "Ingredients_ID" 
        ''', (name,))
        ingredient_id = c.fetchone()
        c.execute('''
            INSERT INTO "Consists" ("Recipe_FK", "Ingredients_FK", "Amount", "Measurement unit", "Temperature")
            VALUES (%s, %s, %s, %s, %s)
        ''', (recipe_id, ingredient_id, amount, measurement_unit, temperature))

        self.conn.commit()

    def add_category(self, difficulty, type_, recipe_country):
        c = self.conn.cursor()

        c.execute('''
            INSERT INTO "Category" ("Category_ID", "Difficulty", "Type", "Country") 
            VALUES (md5(random()::text), %s, %s, %s)
            RETURNING "Category_ID"     
        ''', (difficulty, type_, recipe_country))
        category_id = c.fetchone()

        return category_id

    def update_author(self, login, name, password):
        c = self.conn.cursor()
        c.execute('UPDATE "Author" SET "Name" = %s, "Password" = %s WHERE "Login" = %s', (name, password, login))

        self.conn.commit()

    def update_recipe(self, recipe_id, author_login, name, calories, cooking_time, photos, steps, difficulty, type_, recipe_country):
        c = self.conn.cursor()
        c.execute('''
            UPDATE "Recipe"
            SET "Author_login" = %s, "Name" = %s, "Calories" = %s, "Time" = %s, "Photos" = %s, "Steps" = %s  
            WHERE "Recipe_ID" = %s
        ''', (author_login, name, calories, cooking_time, photos, steps, recipe_id))
        c.execute('''
            SELECT "Category_ID"
            FROM "Category"
            WHERE "Difficulty" = %s AND "Type" = %s AND "Country" = %s
            ''', (difficulty, type_, recipe_country))
        category_id = c.fetchone()

        if not category_id:
            category_id = self.add_category(difficulty, type_, recipe_country)

        c.execute('''
            UPDATE "Includes"
            SET "Category_FK" = %s
            WHERE "Recipe_FK" = %s
            ''', (category_id, recipe_id))

        self.conn.commit()

    def update_ingredient(self, ingredient_id, name, recipe_id, amount, measurement_unit, temperature):
        c = self.conn.cursor()
        c.execute('UPDATE "Ingredients" SET "Name" = %s WHERE "Ingredients_ID" = %s', (name, ingredient_id))
        c.execute('''
                    UPDATE "Consists" 
                    SET "Amount" = %s, "Measurement unit" = %s, "Temperature"= %s 
                    WHERE "Recipe_FK" = %s AND "Ingredients_FK"= %s
                ''', (amount, measurement_unit, temperature, recipe_id, ingredient_id))
        self.conn.commit()

    def update_category(self, category_id, difficulty, type_, recipe_country):
        c = self.conn.cursor()
        c.execute('''
            UPDATE "Category" SET "Difficulty" = %s, "Type" = %s, "Country" = %s WHERE "Category_ID" = %s
        ''', (difficulty, type_, recipe_country, category_id))
        self.conn.commit()

    def delete_author(self, login):
        c = self.conn.cursor()

        c.execute('SELECT * FROM "Recipe" WHERE "Author_login" = %s', (login,))
        recipes = c.fetchall()

        if len(recipes) > 0:
            raise ValueError("Cannot delete author with existing recipes.")

        c.execute('DELETE FROM "Author" WHERE "Login" = %s', (login,))
        self.conn.commit()

    def delete_recipe(self, recipe_id):
        c = self.conn.cursor()

        c.execute('DELETE FROM "Consists" WHERE "Recipe_FK" = %s', (recipe_id,))
        c.execute('DELETE FROM "Includes" WHERE "Recipe_FK" = %s', (recipe_id,))
        c.execute('DELETE FROM "Recipe" WHERE "Recipe_ID" = %s', (recipe_id,))

        self.conn.commit()

    def delete_ingredient(self, ingredient_id):
        c = self.conn.cursor()

        c.execute('SELECT * FROM "Consists" WHERE "Ingredients_FK" = %s', (ingredient_id,))
        consists_entries = c.fetchall()

        if len(consists_entries) > 0:
            raise ValueError("Cannot delete ingredient which consists in recipe.")

        c.execute('DELETE FROM "Ingredients" WHERE "Ingredients_ID" = %s', (ingredient_id,))
        self.conn.commit()

    def delete_category(self, category_id):
        c = self.conn.cursor()

        c.execute('SELECT * FROM "Includes" WHERE "Category_FK" = %s', (category_id,))
        includes_entries = c.fetchall()

        if len(includes_entries) > 0:
            raise ValueError("Cannot delete category which includes recipe.")

        c.execute('DELETE FROM "Category" WHERE "Category_ID" = %s', (category_id,))
        self.conn.commit()

    def generate_author(self, number_of_data):
        c = self.conn.cursor()
        c.execute("""
            INSERT INTO "Author" ("Login", "Name", "Password")
            VALUES(
                md5(random()::text),
                chr(trunc(65 + random() * 26)::int) || 
                chr(trunc(97 + random() * 26)::int) || 
                chr(trunc(97 + random() * 26)::int) || 
                chr(trunc(97 + random() * 26)::int) AS "Name",
                chr(trunc(65 + random() * 50)::int) || chr(trunc(65 + random() * 25)::int) ||
                chr(trunc(65 + random() * 25)::int) || chr(trunc(65 + random() * 25)::int) AS "Password")
            FROM generate_series(1, %s);
        """, (number_of_data,))
        self.conn.commit()

    def generate_dish(self, dish_type):
        if dish_type == "starter":
            dish = random.choice(starter)
        elif dish_type == "main course":
            dish = random.choice(main_course)
        else:
            dish = random.choice(dessert)

        return dish

    def generate_difficulty(self):
        return random.choice(category_difficulty)

    def generate_dish_type(self):
        return random.choice(category_type)

    def generate_country(self):
        return random.choice(country)

    def generate_ingredient(self):
        return random.choice(ingredients)

    def generate_time(self):
        hour = random.randint(0, 23)
        minute = random.randint(0, 59)
        second = random.randint(0, 59)

        random_time = f"{hour:02d}:{minute:02d}:{second:02d}"

        return random_time

    def generate_recipe(self, number_of_data):
        c = self.conn.cursor()

        for _ in range(number_of_data):

            dish_type = self.generate_dish_type()
            dish = self.generate_dish(dish_type)
            prep_time = self.generate_time()
            dish_country = self.generate_country()
            difficulty = self.generate_difficulty()

            c.execute('SELECT "Login" FROM "Author" ORDER BY random() LIMIT 1')
            login = c.fetchone()

            c.execute('''
               INSERT INTO "Recipe" ("Recipe_ID", "Author_login", "Name", "Calories", "Time", "Photos", "Steps")
                    VALUES(
                        md5(random()::text),
                        %s,
                        %s,
                        floor(random() * 1000)::int,
                        %s,
                        'recipe.jpg',
                        'steps')
                    FROM generate_series(1, 1)
                    RETURNING "Recipe_ID";
            ''', (login, dish, prep_time))
            recipe_id = c.fetchone()

            for _ in range(1):
                ingredient_name = self.generate_ingredient()
                c.execute('SELECT "Ingredients_ID" FROM "Ingredients" WHERE "Name" = %s', (ingredient_name,))
                ingredient_id = c.fetchone()

                if not ingredient_id:
                    c.execute('''
                        INSERT INTO "Ingredients" ("Ingredients_ID", "Name")
                        VALUES (chr(trunc(65 + random() * 50)::int) || chr(trunc(65 + random() * 25)::int) ||
                             chr(trunc(65 + random() * 25)::int) || chr(trunc(65 + random() * 25)::int),
                             %s)
                        RETURNING "Ingredients_ID";
                    ''', (ingredient_name,))
                    ingredient_id = c.fetchone()

                c.execute('SELECT 1 FROM "Consists" WHERE "Recipe_FK" = %s AND "Ingredients_FK" = %s',
                          (recipe_id, ingredient_id))

                if not c.fetchone():
                    c.execute('''
                        INSERT INTO "Consists" ("Recipe_FK", "Ingredients_FK", "Amount", "Measurement unit", "Temperature")
                        VALUES (%s, %s, floor(random() * 1000)::int, 'grams', floor(random() * 100)::int)
                        FROM "Ingredients" ORDER BY random() LIMIT 1;
                    ''', (recipe_id, ingredient_id))

            c.execute('SELECT "Category_ID" FROM "Category" WHERE "Difficulty" = %s AND "Type" = %s AND "Country" = %s',
                      (difficulty, dish_type, dish_country))
            category_id = c.fetchone()

            if not category_id:

                c.execute('''
                    INSERT INTO "Category" ("Category_ID", "Difficulty", "Type", "Country")
                    VALUES(
                        md5(random()::text), 
                        %s,
                        %s, 
                        %s)
                        RETURNING "Category_ID";
                ''', (difficulty, dish_type, dish_country))
                category_id = c.fetchone()
            c.execute('''
                SELECT 1
                FROM "Includes"
                WHERE "Recipe_FK" = %s AND "Category_FK" = %s
            ''', (recipe_id, category_id))

            if not c.fetchone():
                c.execute('''
                    INSERT INTO "Includes" ("Recipe_FK", "Category_FK")
                    VALUES (%s, %s)
                ''', (recipe_id, category_id))

            self.conn.commit()

    def generate_ingredients(self, number_of_data):
        c = self.conn.cursor()
        for _ in range(number_of_data):

            ingredient = self.generate_ingredient()

            c.execute('SELECT "Recipe_ID" FROM "Recipe" ORDER BY random() LIMIT 1')
            recipe_id = c.fetchone()

            c.execute('''
                INSERT INTO "Ingredients" ("Ingredients_ID", "Name")
                    VALUES (md5(random()::text), %s)
                    FROM generate_series(1, 1)
                    RETURNING "Ingredients_ID"
            ''', (ingredient,))
            ingredient_id = c.fetchone()
            c.execute('SELECT 1 FROM "Consists" WHERE "Recipe_FK" = %s AND "Ingredients_FK" = %s',
                      (recipe_id, ingredient_id))

            if not c.fetchone():
                c.execute('''
                    INSERT INTO "Consists" ("Recipe_FK", "Ingredients_FK", "Amount", "Measurement unit", "Temperature")
                    VALUES (%s, %s, floor(random() * 1000)::int, 'grams', floor(random() * 100)::int)
                    FROM "Ingredients" ORDER BY random() LIMIT 1;
                ''', (recipe_id, ingredient_id))

            self.conn.commit()

    def generate_category(self, number_of_data):

        c = self.conn.cursor()

        for _ in range(number_of_data):

            difficulty = self.generate_difficulty()
            type_ = self.generate_dish_type()
            recipe_country = self.generate_country()

            c.execute('''
                INSERT INTO "Category" ("Category_ID", "Difficulty", "Type", "Country")
                VALUES (md5(random()::text), %s, %s, %s)
                FROM generate_series(1, 1);
            ''', (difficulty, type_, recipe_country))

        self.conn.commit()

    def search_recipes_by_attributes(self, type_, recipe_country, difficulty):
        c = self.conn.cursor()
        start_time = time.time()

        c.execute('''
            SELECT "Recipe"."Name", "Author"."Name"
            FROM "Recipe"
            JOIN "Author" ON "Recipe"."Author_login" = "Author"."Login"
            JOIN "Includes" ON "Recipe"."Recipe_ID" = "Includes"."Recipe_FK"
            JOIN "Category" ON "Includes"."Category_FK" = "Category"."Category_ID"
            WHERE "Category"."Type" = %s
                AND "Category"."Country" = %s
                AND "Category"."Difficulty" = %s
            ORDER BY "Recipe"."Name";
        ''', (type_, recipe_country, difficulty))

        results = c.fetchall()
        end_time = time.time()
        execution_time = (end_time - start_time) * 1000

        return results, execution_time

    def search_recipes_by_ingredient_and_name(self, ingredient_name, recipe_name):

        c = self.conn.cursor()
        start_time = time.time()

        if not recipe_name:

            c.execute('''
                SELECT DISTINCT "Recipe"."Name", "Author"."Name", "Recipe"."Time"
                FROM "Recipe"
                JOIN "Author" ON "Recipe"."Author_login" = "Author"."Login"
                JOIN "Consists" ON "Recipe"."Recipe_ID" = "Consists"."Recipe_FK"
                JOIN "Ingredients" ON "Consists"."Ingredients_FK" = "Ingredients"."Ingredients_ID"
                WHERE "Ingredients"."Name" = %s
                ORDER BY "Recipe"."Time" DESC;
            ''', (ingredient_name,))
        else:
            c.execute('''
                SELECT DISTINCT "Recipe"."Name", "Author"."Name", "Recipe"."Time"
                FROM "Recipe"
                JOIN "Author" ON "Recipe"."Author_login" = "Author"."Login"
                JOIN "Consists" ON "Recipe"."Recipe_ID" = "Consists"."Recipe_FK"
                JOIN "Ingredients" ON "Consists"."Ingredients_FK" = "Ingredients"."Ingredients_ID"
                WHERE "Ingredients"."Name" = %s AND "Recipe"."Name" = %s
                ORDER BY "Recipe"."Time" DESC;
            ''', (ingredient_name, recipe_name))

        end_time = time.time()
        execution_time = (end_time - start_time) * 1000

        results = c.fetchall()
        return results, execution_time

    def get_author_recipe_counts(self, login):
        c = self.conn.cursor()
        start_time = time.time()

        c.execute('''
            SELECT "Author"."Name", COUNT("Recipe"."Recipe_ID") AS "RecipeCount"
            FROM "Author"
            LEFT JOIN "Recipe" ON "Author"."Login" = "Recipe"."Author_login"
            WHERE "Author"."Login" = %s
            GROUP BY "Author"."Name"
            ORDER BY "RecipeCount" DESC;
        ''', (login,))

        end_time = time.time()
        execution_time = (end_time - start_time) * 1000

        results = c.fetchall()
        return results, execution_time

    def get_authors(self):
        c = self.conn.cursor()
        c.execute('SELECT "Login", "Name", "Password" FROM "Author"')
        authors = c.fetchall()
        return authors

    def get_recipes(self):
        c = self.conn.cursor()
        c.execute('SELECT "Recipe_ID", "Author_login", "Name", "Calories", "Time", "Photos", "Steps" FROM "Recipe"')
        recipes = c.fetchall()
        return recipes

    def get_ingredients(self):
        c = self.conn.cursor()
        c.execute('SELECT "Ingredients_ID", "Name" FROM "Ingredients"')
        ingredient = c.fetchall()
        return ingredient

    def get_categories(self):
        c = self.conn.cursor()
        c.execute('SELECT "Category_ID", "Difficulty", "Type", "Country" FROM "Category"')
        categories = c.fetchall()
        return categories

    def get_includes(self):
        c = self.conn.cursor()
        c.execute('SELECT "Recipe_FK", "Category_FK" FROM "Includes"')
        includes = c.fetchall()
        return includes

    def get_consists(self):
        c = self.conn.cursor()
        c.execute('SELECT "Recipe_FK", "Ingredients_FK", "Amount", "Measurement unit", "Temperature" FROM "Consists"')
        consists = c.fetchall()
        return consists

    def author_exists(self, login):
        c = self.conn.cursor()
        c.execute('SELECT 1 FROM "Author" WHERE "Login" = %s', (login,))
        return bool(c.fetchone())

    def recipe_exists(self, recipe_id):
        c = self.conn.cursor()
        c.execute('SELECT 1 FROM "Recipe" WHERE "Recipe_ID" = %s', (recipe_id,))
        return bool(c.fetchone())

    def ingredient_exists(self, ingredient_id):
        c = self.conn.cursor()
        c.execute('SELECT 1 FROM "Ingredients" WHERE "Ingredients_ID" = %s', (ingredient_id,))
        return bool(c.fetchone())

    def category_id_exists(self, category_id):
        c = self.conn.cursor()
        c.execute('''
            SELECT 1 FROM "Category" WHERE "Category_ID" = %s
            ''', (category_id,))
        return bool(c.fetchone())

    def category_param_exists(self, difficulty, type_, recipe_country):
        c = self.conn.cursor()
        c.execute('''
            SELECT 1 FROM "Category" 
            WHERE "Difficulty" = %s AND "Type" = %s AND "Country" = %s
            ''', (difficulty, type_, recipe_country,))
        return bool(c.fetchone())

    def check_ingredient_exists(self, ingredient_name):
        c = self.conn.cursor()
        c.execute('SELECT COUNT(*) FROM "Ingredients" WHERE "Name" = %s', (ingredient_name,))
        count = c.fetchone()[0]

        if count > 0:
            return True
        else:
            return False
