import re
import nltk
from handlequery import handle_question
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords

nltk.download('punkt')
nltk.download('punkt_tab')
nltk.download('stopwords')

def preprocess_input(user_input):
    stop_words = set(stopwords.words('english'))
    tokens = word_tokenize(user_input.lower())
    filtered_tokens = [word for word in tokens if word.isalnum() and word not in stop_words]
    return filtered_tokens

def extract_step_number(tokens):
    for token in tokens:
        if token.isdigit():
            return int(token)
    return None

def start_conversation(recipe):
    print(f"Let's start with the recipe for {recipe.title}. What would you like to do?")
    while True:
        print("\nOptions: [1] Go over ingredients list, [2] Go over recipe steps, [3] Help, [4] Exit")
        user_input = input("Enter your choice or type your request: ")
        tokens = preprocess_input(user_input)

        if any(word in {'ingredient', 'ingredients', '1'} for word in tokens):
            print("\nIngredients:")
            for ingredient in recipe.get_ingredients():
                print(f"- {ingredient['quantity']} {ingredient['measurement']} {ingredient['name']}")
        elif any(word in {'step', 'steps', '2'} for word in tokens):
            handle_step_navigation(recipe)
        elif any(word in {'help', '3'} for word in tokens):
            handle_help()
        elif contains_exit_command(tokens) or '4' in tokens:
            print("Goodbye!")
            break

def handle_step_navigation(recipe):
    while True:
        step = recipe.get_current_step()
        print(f"\nStep {recipe.get_step_number()}/{recipe.get_total_steps()}: {step['text']}")
        
        user_input = input(
            "\nOptions: [1] Next step, [2] Previous step, [3] Go to specific step, [4] Show methods, "
            "[5] Show tools, [6] Help, [7] Go back to main menu\nEnter your choice or type your request: ")
        tokens = preprocess_input(user_input)

        if any(word in {'next', '1'} for word in tokens):
            if not recipe.is_last_step():
                recipe.next_step()
                step = recipe.get_current_step()
                print(f"\nStep {recipe.get_step_number()}/{recipe.get_total_steps()}: {step['text']}")
            else:
                print("You've reached the last step.")
        elif any(word in {'previous', '2'} for word in tokens):
            if not recipe.is_first_step():
                recipe.previous_step()
                step = recipe.get_current_step()
                print(f"\nStep {recipe.get_step_number()}/{recipe.get_total_steps()}: {step['text']}")
            else:
                print("You are already at the first step.")
        elif any(word in {'go', 'step', '3'} for word in tokens):
            step_number = extract_step_number(tokens)
            if step_number is not None:
                result = recipe.go_to_step(step_number)
                print(f"\nStep {recipe.get_step_number()}/{recipe.get_total_steps()}: {result['text']}")
            else:
                text_query = ' '.join(tokens)
                result = recipe.go_to_step_by_text(text_query)
                print(f"\n{result}")
        elif any(word in {'show', 'methods', 'method', '4'} for word in tokens) or any(word in {'list', 'share'} for word in tokens):
            methods = recipe.get_current_step_methods()
            if methods:
                print(f"\nMethods for this step: {', '.join(methods)}")
            else:
                print("No methods listed for this step.")
        elif any(word in {'show', 'tools', 'tool', '5'} for word in tokens) or any(word in {'list', 'share'} for word in tokens):
            tools = recipe.get_current_step_tools()
            if tools:
                print(f"\nTools for this step: {', '.join(tools)}")
            else:
                print("No tools listed for this step.")
        elif any(word in {'help', 'what', 'to', 'when', '6'} for word in tokens):
            handle_help()
        elif all(word in {'how','much','quantity'} for word in tokens):
            ingredient_name = extract_ingredient_name(user_input)
            if ingredient_name:
                quantity = recipe.get_ingredient_quantity(ingredient_name)
                print(quantity)
            else:
                print("Ingredient not found in this recipe.")
        elif contains_exit_command(tokens) or '7' in tokens:
            break

def contains_exit_command(tokens):
    exit_commands = {'back', 'exit', 'quit', 'bye'}
    return any(command in tokens for command in exit_commands)

def extract_ingredient_name(user_input):
    # Regex to match common patterns in user queries about ingredient quantities
    patterns = [
        r"how much (?P<ingredient>\w+)",                  # Matches "how much sugar do I need?"
        r"how many (?P<ingredient>\w+)",                  # Matches "how many carrots do I need?"
        r"tell me the quantity of (?P<ingredient>\w+)",   # Matches "tell me the quantity of salt"
        r"quantity of (?P<ingredient>\w+)",               # Matches "what's the quantity of flour?"
        r"amount of (?P<ingredient>\w+)",                 # Matches "what's the amount of flour?"
        r"what quantity of (?P<ingredient>\w+)",          # Matches "what quantity of butter?"
        r"what amount of (?P<ingredient>\w+)",            # Matches "what amount of sugar?"
        r"how much of (?P<ingredient>\w+)",               # Matches "how much of salt is needed?"
        r"how many of (?P<ingredient>\w+)",               # Matches "how many of the eggs do I need?"
        r"need (?P<ingredient>\w+)",                      # Matches "how many eggs do I need?"
        r"how much do I need of (?P<ingredient>\w+)",     # Matches "how much do I need of sugar?"
        r"what's the amount of (?P<ingredient>\w+)",      # Matches "what's the amount of flour?"
        r"how much (?P<ingredient>\w+) is required",      # Matches "how much sugar is required?"
    ]
    
    for pattern in patterns:
        match = re.search(pattern, user_input, re.IGNORECASE)
        if match:
            return match.group('ingredient')
    return None

def handle_help():
    question = input("What help do you need? ")
    platform_choice = input("\nOptions: [1] Google, [2] YouTube\nEnter your choice: ")
    platform = 'YouTube' if platform_choice == '2' else 'Google'
    solution = handle_question(question, platform)
    print(f"{platform} Search: {solution}")
