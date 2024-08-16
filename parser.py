import requests
from bs4 import BeautifulSoup
import re

def fetch_recipe(url):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0.0 Safari/537.36',
        'Accept-Language': 'en-US,en;q=0.9',
        'Referer': 'https://www.google.com',
    }

    response = requests.get(url, headers=headers)
    
    if response.status_code != 200:
        raise Exception(f"Failed to fetch the recipe. Status code: {response.status_code}")
    
    print(f"URL:{url}. Loaded")

    soup = BeautifulSoup(response.content, 'html.parser')
    
    # Extract recipe title
    title = soup.find('h1', class_='article-heading type--lion').text.strip()
    
    # Extract ingredients

    # Extract ingredients
    ingredients = parse_ingredients(soup,'mm-recipes-structured-ingredients__list-item')
    
    # Extract steps
    steps = parse_steps(soup,'comp mntl-sc-block mntl-sc-block-startgroup mntl-sc-block-group--LI')

    print(f"{title.upper()} Recipe Loaded")
    
    return {
        "title": title,
        "ingredients": ingredients,
        "steps": steps
    }

def parse_ingredients(soup,classingredients):
    ingredients = []
    for ingredient in soup.find_all('li', class_=classingredients):
        details = ingredient.text.strip().split(' ')
        quantity = details[0] if details[0].isdigit() else ''
        measurement = details[1] if len(details) > 1 else ''
        name = ' '.join(details[2:]) if len(details) > 2 else ' '.join(details[1:])
        ingredients.append({
            "name": name,
            "quantity": quantity,
            "measurement": measurement
        })
    return ingredients

def parse_steps(soup,stepsclass):
    steps = []
    for step in soup.find_all('li', class_=stepsclass):
        step_text = step.text.strip()
        
        # Extract methods and tools using regex
        methods = extract_methods(step_text)
        tools = extract_tools(step_text)
        
        steps.append({
            "text": step_text,
            "methods": methods,
            "tools": tools
        })
    return steps

def extract_methods(text):
    methods = []
    method_patterns = [
        'saute', 'broil', 'boil', 'poach', 'bake', 'roast', 'grill', 'fry',
        'chop', 'grate', 'stir', 'shake', 'mince', 'crush', 'squeeze'
    ]
    for method in method_patterns:
        if re.search(r'\b' + re.escape(method) + r'\b', text, re.IGNORECASE):
            methods.append(method)
    return methods

def extract_tools(text):
    tools = []
    tool_patterns = [
        'pan', 'grater', 'whisk', 'spoon', 'fork', 'knife', 'bowl', 'pot', 'ladle'
    ]
    for tool in tool_patterns:
        if re.search(r'\b' + re.escape(tool) + r'\b', text, re.IGNORECASE):
            tools.append(tool)
    return tools
