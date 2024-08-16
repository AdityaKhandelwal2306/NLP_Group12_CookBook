from difflib import get_close_matches

class Recipe:
    def __init__(self, recipe_data):
        self.title = recipe_data['title']
        self.ingredients = recipe_data['ingredients']
        self.steps = recipe_data['steps']
        self.current_step = 0
    
    def get_ingredients(self):
        return self.ingredients
    
    def get_current_step(self):
        return self.steps[self.current_step]
    
    def next_step(self):
        if self.current_step < len(self.steps) - 1:
            self.current_step += 1
        return self.get_current_step()
    
    def previous_step(self):
        if self.current_step > 0:
            self.current_step -= 1
        return self.get_current_step()
    
    def is_first_step(self):
        return self.current_step == 0
    
    def is_last_step(self):
        return self.current_step == len(self.steps) - 1
    
    def get_step_number(self):
        return self.current_step + 1
    
    def get_total_steps(self):
        return len(self.steps)
    
    def go_to_step(self, step_number):
        if 1 <= step_number <= len(self.steps):
            self.current_step = step_number - 1
            return self.get_current_step()
        else:
            return f"Invalid step number. Please provide a number between 1 and {len(self.steps)}."
    
    def go_to_step_by_text(self, text_query):
        step_descriptions = [step['text'].lower() for step in self.steps]
        matches = get_close_matches(text_query.lower(), step_descriptions, n=1, cutoff=0.6)
        if matches:
            matched_step_index = step_descriptions.index(matches[0])
            self.current_step = matched_step_index
            return self.get_current_step()
        else:
            return "No matching step found. Please refine your query."
    
    def get_current_step_methods(self):
        return self.steps[self.current_step]['methods']
    
    def get_current_step_tools(self):
        return self.steps[self.current_step]['tools']
    
    def get_ingredient_quantity(self, ingredient_name):
        ingredient_name = ingredient_name.lower()
        for ingredient in self.ingredients:
            if ingredient_name in ingredient['name'].lower():
                return f"{ingredient['quantity']} {ingredient['measurement']} {ingredient['name']}"
        return "Ingredient not found."


