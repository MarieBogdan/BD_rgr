from model import Model
from view import View
import re


class Controller:
    def __init__(self):
        self.model = Model()
        self.view = View()

    def run(self):

        author_methods = {'1': self.add_author,
                          '2': self.update_author,
                          '3': self.delete_author,
                          '4': self.generate_author,
                          '6': self.delete_all_authors,
                          '5': 'break'}

        recipe_methods = {'1': self.add_recipe,
                          '2': self.update_recipe,
                          '3': self.delete_recipe,
                          '4': self.generate_recipe,
                          '5': 'break'}

        ingredients_methods = {'1': self.add_ingredient,
                               '2': self.update_ingredient,
                               '3': self.delete_ingredient,
                               '4': self.generate_ingredients,
                               '5': 'break'}

        category_methods = {'1': self.add_category,
                            '2': self.update_category,
                            '3': self.delete_category,
                            '4': self.generate_category,
                            '5': 'break'}
        requests_methods = {'1': self.search_recipes_by_type_country_difficulty,
                            '2': self.search_recipes_by_ingredient_and_name,
                            '3': self.get_author_recipe_counts,
                            '4': 'break'}

        while True:
            choice1 = self.view.show_menu()

            if choice1 == "1":
                choice2 = self.view.show_author_menu()

                if choice2 in author_methods:
                    if choice2 == "5":
                        break
                    author_methods[choice2]()
                else:
                    self.view.show_message("Invalid choice, please try again.")
            elif choice1 == "2":
                choice2 = self.view.show_recipe_menu()

                if choice2 in recipe_methods:
                    if choice2 == "5":
                        break
                    recipe_methods[choice2]()
                else:
                    self.view.show_message("Invalid choice, please try again.")
            elif choice1 == "3":
                choice2 = self.view.show_ingredients_menu()

                if choice2 in ingredients_methods:
                    if choice2 == "5":
                        break
                    ingredients_methods[choice2]()
                else:
                    self.view.show_message("Invalid choice, please try again.")
            elif choice1 == "4":
                choice2 = self.view.show_category_menu()

                if choice2 in category_methods:
                    if choice2 == "5":
                        break
                    category_methods[choice2]()
                else:
                    self.view.show_message("Invalid choice, please try again.")
            elif choice1 == "5":
                choice2 = self.view.show_requests_menu()

                if choice2 in requests_methods:
                    if choice2 == "4":
                        break
                    requests_methods[choice2]()
                else:
                    self.view.show_message("Invalid choice, please try again.")

    def add_author(self):
        try:
            name, password = self.view.get_authors_input()

            if not name or not password:
                raise ValueError("Invalid data. Name and password must be filled.")

            if not isinstance(name, str):
                raise ValueError("Invalid name format. Name must be a string.")
            if not isinstance(password, str):
                raise ValueError("Invalid password format. Password must be a string.")

            login = self.model.add_author(name, password)

            self.view.show_message("\nAUTHOR ADDED  SUCCESSFULLY!")
            self.view.show_authors_login(login)
            self.show_author_table()

        except ValueError as e:
            self.view.show_message(f"Input error: {e}")
        except Exception as e:
            self.view.show_message(f"An unexpected error occurred: {e}")

    def add_recipe(self):
        try:
            author_login, name, calories, time, photos, steps = self.view.get_recipe_input()
            author_exists = self.model.author_exists(author_login)
            self.view.show_message("Please enter category for this dish: ")
            difficulty = self.view.get_difficulty_input()
            type_ = self.view.get_type_input()
            country = self.view.get_country_input()

            if not name or not steps or not author_login:
                raise ValueError("Invalid data. Name, steps and author's login must be filled.")

            if not isinstance(author_login, str):
                raise ValueError("Invalid login format. Login must be a string.")
            if not isinstance(name, str):
                raise ValueError("Invalid name format. Name must be a string.")

            if calories is not None:
                calories = int(calories)

            if not re.match(r'\d{2}:\d{2}:\d{2}', time):
                raise ValueError("Invalid time format. Time must be in the 'hh:mi:ss' format.")

            if not isinstance(photos, str):
                raise ValueError("Invalid photos format. Path to photos must be a string.")
            if not isinstance(steps, str):
                raise ValueError("Invalid steps format. Steps must be a string.")
            if not isinstance(difficulty, str):
                raise ValueError("Invalid name format. Difficulty must be a string.")
            if not isinstance(type_, str):
                raise ValueError("Invalid login format. Type must be a string.")
            if not isinstance(country, str):
                raise ValueError("Invalid name format. Country must be a string.")

            if not author_exists:
                self.show_author_table()
                raise ValueError("Author with this login does not exist.")

            recipe_id = self.model.add_recipe(
                author_login, name, calories, time, photos, steps, difficulty, type_, country)

            self.view.show_message("\nRECIPE ADDED  SUCCESSFULLY!")
            self.view.show_recipe_id(recipe_id)
            self.show_recipe_table()
            self.show_includes_table()

        except ValueError as e:
            self.view.show_message(f"Input error: {e}")
        except Exception as e:
            self.view.show_message(f"An unexpected error occurred: {e}")

    def add_ingredient(self):
        try:
            name, recipe_id, amount, measurement_unit, temperature = self.view.get_ingredient_input()

            if not name or not recipe_id or not amount or not measurement_unit:
                raise ValueError("Invalid data. Name, recipe_id, amount and measurement_unit must be filled.")

            if not isinstance(name, str):
                raise ValueError("Invalid name format. Name must be a string")

            is_recipe_exists = self.model.recipe_exists(recipe_id)
            if is_recipe_exists:
                self.model.add_ingredient(name, recipe_id, amount, measurement_unit, temperature)
                self.view.show_message("\nINGREDIENT ADDED  SUCCESSFULLY!")
                self.show_ingredients_table()
                self.show_consists_table()
            else:
                self.view.show_message("Recipe with this ID does not exist")

        except ValueError as e:
            self.view.show_message(f"Input error: {e}")
        except Exception as e:
            self.view.show_message(f"An unexpected error occurred: {e}")

    def add_category(self):
        try:
            difficulty = self.view.get_difficulty_input()
            type_ = self.view.get_type_input()
            country = self.view.get_country_input()

            if not type_:
                raise ValueError("Invalid data.Type must be filled.")

            if not isinstance(difficulty, str):
                raise ValueError("Invalid name format. Difficulty must be a string.")
            if not isinstance(type_, str):
                raise ValueError("Invalid login format. Type must be a string.")
            if not isinstance(country, str):
                raise ValueError("Invalid name format. Country must be a string.")

            is_category_exists = self.model.category_param_exists(difficulty, type_, country)

            if not is_category_exists:
                self.model.add_category(difficulty, type_, country)
                self.view.show_message("\nCATEGORY ADDED  SUCCESSFULLY!")
                self.show_category_table()
            else:
                self.view.show_message("Category with this parameters already exists!")

        except ValueError as e:
            self.view.show_message(f"Input error: {e}")
        except Exception as e:
            self.view.show_message(f"An unexpected error occurred: {e}")

    def update_author(self):
        try:
            login = self.view.get_login()
            name, password = self.view.get_authors_input()

            if not login:
                raise ValueError("Invalid data. Login must be filled.")

            if not self.model.author_exists(login):
                raise ValueError("Author with this login does not exist.")

            if not isinstance(login, str):
                raise ValueError("Invalid login format. Login must be a string.")

            if not isinstance(name, str):
                raise ValueError("Invalid name format. Name must be a string.")
            if not isinstance(password, str):
                raise ValueError("Invalid password format. Password must be a string.")

            self.model.update_author(login, name, password)
            self.view.show_message("Author updated successfully!")
            self.show_author_table()

        except ValueError as e:
            self.view.show_message(f"Input error: {e}")
        except Exception as e:
            self.view.show_message(f"An unexpected error occurred: {e}")

    def update_recipe(self):
        try:
            recipe_id = self.view.get_recipe_id()
            author_login, name, calories, time, photos, steps = self.view.get_recipe_input()
            difficulty = self.view.get_difficulty_input()
            type_ = self.view.get_type_input()
            country = self.view.get_country_input()

            if not recipe_id:
                raise ValueError("Invalid data. Recipe id must be filled.")

            if not self.model.recipe_exists(recipe_id):
                raise ValueError("Recipe with this ID does not exist.")

            if not isinstance(author_login, str):
                raise ValueError("Invalid login format. Login must be a string.")
            if not isinstance(name, str):
                raise ValueError("Invalid name format. Name must be a string.")

            if calories is not None:
                calories = int(calories)

            if not re.match(r'\d{2}:\d{2}:\d{2}', time):
                raise ValueError("Invalid time format. Time must be in the 'hh:mi:ss' format.")

            if not isinstance(photos, str):
                raise ValueError("Invalid photos format. Photos must be a string.")
            if not isinstance(steps, str):
                raise ValueError("Invalid steps format. Steps must be a string.")

            self.model.update_recipe(recipe_id, author_login, name, calories, time, photos, steps, difficulty, type_, country)
            self.view.show_message("Recipe updated successfully!")
            self.show_recipe_table()
            self.show_includes_table()

        except ValueError as e:
            self.view.show_message(f"Input error: {e}")
        except Exception as e:
            self.view.show_message(f"An unexpected error occurred: {e}")

    def update_ingredient(self):
        try:
            ingredient_id = self.view.get_ingredient_id()
            name, recipe_id, amount, measurement_unit, temperature = self.view.get_ingredient_input()

            if not ingredient_id:
                raise ValueError("Invalid data. Ingredient id must be filled.")

            if not self.model.ingredient_exists(ingredient_id):
                raise ValueError("Ingredient with this ID does not exist.")

            if not isinstance(name, str):
                raise ValueError("Invalid name format. Name must be a string.")

            self.model.update_ingredient(ingredient_id, name, recipe_id, amount, measurement_unit, temperature)
            self.view.show_message("Ingredient updated successfully!")
            self.show_ingredients_table()
            self.show_consists_table()

        except ValueError as e:
            self.view.show_message(f"Input error: {e}")
        except Exception as e:
            self.view.show_message(f"An unexpected error occurred: {e}")

    def update_category(self):
        try:
            category_id = self.view.get_category_id()
            difficulty = self.view.get_difficulty_input()
            type_ = self.view.get_type_input()
            country = self.view.get_country_input()

            if not category_id:
                raise ValueError("Invalid data. Category id must be filled.")

            if not self.model.category_id_exists(category_id):
                raise ValueError("Category with this ID does not exist.")

            if not isinstance(difficulty, str):
                raise ValueError("Invalid difficulty format. Difficulty must be a string.")
            if not isinstance(type_, str):
                raise ValueError("Invalid type format. Type must be a string.")
            if not isinstance(country, str):
                raise ValueError("Invalid country format. Country must be a string.")

            self.model.update_category(category_id, difficulty, type_, country)
            self.view.show_message("Category updated successfully!")
            self.show_category_table()

        except ValueError as e:
            self.view.show_message(f"Input error: {e}")
        except Exception as e:
            self.view.show_message(f"An unexpected error occurred: {e}")

    def delete_author(self):
        try:
            login = self.view.get_login()

            if not self.model.author_exists(login):
                raise ValueError("Author with this login does not exist.")

            self.model.delete_author(login)
            self.view.show_message("Author deleted successfully!")
            self.show_author_table()
            self.show_recipe_table()

        except ValueError as e:
            self.view.show_message(f"Input error: {e}")
        except Exception as e:
            self.view.show_message(f"An unexpected error occurred: {e}")

    def delete_recipe(self):
        try:
            recipe_id = self.view.get_recipe_id()

            if not self.model.recipe_exists(recipe_id):
                raise ValueError("Recipe with this ID does not exist.")

            self.model.delete_recipe(recipe_id)
            self.view.show_message("Recipe deleted successfully!")
            self.show_recipe_table()
            self.show_includes_table()
            self.show_consists_table()
        except ValueError as e:
            self.view.show_message(f"Input error: {e}")
        except Exception as e:
            self.view.show_message(f"An unexpected error occurred: {e}")

    def delete_ingredient(self):
        try:
            ingredient_id = self.view.get_ingredient_id()

            if not self.model.ingredient_exists(ingredient_id):
                raise ValueError("Ingredient with this ID does not exist.")

            self.model.delete_ingredient(ingredient_id)
            self.view.show_message("Ingredient deleted successfully!")
            self.show_ingredients_table()
            self.show_consists_table()
        except ValueError as e:
            self.view.show_message(f"Input error: {e}")
        except Exception as e:
            self.view.show_message(f"An unexpected error occurred: {e}")

    def delete_category(self):
        try:
            category_id = self.view.get_category_id()

            if not self.model.category_id_exists(category_id):
                raise ValueError("Category with this ID does not exist.")

            self.model.delete_category(category_id)
            self.view.show_message("Category deleted successfully!")
            self.show_category_table()
            self.show_includes_table()
        except ValueError as e:
            self.view.show_message(f"Input error: {e}")
        except Exception as e:
            self.view.show_message(f"An unexpected error occurred: {e}")

    def generate_author(self):
        try:
            number_of_data = self.view.get_number()
            self.model.generate_author(number_of_data)
            self.view.show_message("Data generated successfully!")
            self.show_author_table()
        except ValueError as e:
            self.view.show_message(f"Input error: {e}")
        except Exception as e:
            self.view.show_message(f"An unexpected error occurred: {e}")

    def generate_recipe(self):
        try:
            number_of_data = self.view.get_number()
            self.model.generate_recipe(int(number_of_data))
            self.view.show_message("Data generated successfully!")
            self.show_recipe_table()
            self.show_ingredients_table()
            self.show_category_table()
            self.show_includes_table()
            self.show_consists_table()
        except ValueError as e:
            self.view.show_message(f"Input error: {e}")
        except Exception as e:
            self.view.show_message(f"An unexpected error occurred: {e}")

    def generate_ingredients(self):
        try:
            number_of_data = self.view.get_number()
            self.model.generate_ingredients(int(number_of_data))
            self.view.show_message("Data generated successfully!")
            self.show_ingredients_table()
            self.show_consists_table()
        except ValueError as e:
            self.view.show_message(f"Input error: {e}")
        except Exception as e:
            self.view.show_message(f"An unexpected error occurred: {e}")

    def generate_category(self):
        try:
            number_of_data = self.view.get_number()
            self.model.generate_category(int(number_of_data))
            self.show_category_table()
            self.view.show_message("Data generated successfully!")
        except ValueError as e:
            self.view.show_message(f"Input error: {e}")
        except Exception as e:
            self.view.show_message(f"An unexpected error occurred: {e}")

    def search_recipes_by_type_country_difficulty(self):
        category_type = self.view.get_type_input()
        category_country = self.view.get_country_input()
        category_difficulty = self.view.get_difficulty_input()
        try:
            results, execution_time = self.model.search_recipes_by_attributes(category_type, category_country, category_difficulty)
            self.view.display_request1_results(results)
            self.view.get_request_time(execution_time)
        except ValueError as e:
            self.view.show_message(f"Input error: {e}")
        except Exception as e:
            self.view.show_message(f"An unexpected error occurred: {e}")

    def search_recipes_by_ingredient_and_name(self):
        try:
            ingredient_name, recipe_name = self.view.get_ingredient_and_name()

            if not self.model.check_ingredient_exists(ingredient_name):
                raise Exception("Ingredient does not exist.")

            results, execution_time = self.model.search_recipes_by_ingredient_and_name(ingredient_name, recipe_name)
            if not results:
                self.view.show_message("No recipes matching the entered criteria were found.")

            self.view.display_request2_results(results)
            self.view.get_request_time(execution_time)
        except ValueError as e:
            self.view.show_message(f"Input error: {e}")
        except Exception as e:
            self.view.show_message(f"An unexpected error occurred: {e}")

    def get_author_recipe_counts(self):
        try:
            login = self.view.get_login()
            results, execution_time = self.model.get_author_recipe_counts(login)
            self.view.display_request3_results(results)
            self.view.get_request_time(execution_time)
        except ValueError as e:
            self.view.show_message(f"Input error: {e}")
        except Exception as e:
            self.view.show_message(f"An unexpected error occurred: {e}")

    def show_author_table(self):
        authors = self.model.get_authors()
        self.view.display_author_table(authors)

    def show_recipe_table(self):
        recipes = self.model.get_recipes()
        self.view.display_recipe_table(recipes)

    def show_ingredients_table(self):
        ingredients = self.model.get_ingredients()
        self.view.display_ingredients_table(ingredients)

    def show_category_table(self):
        category = self.model.get_categories()
        self.view.display_category_table(category)

    def show_includes_table(self):
        includes = self.model.get_includes()
        self.view.display_includes_table(includes)

    def show_consists_table(self):
        consists = self.model.get_consists()
        self.view.display_consists_table(consists)
