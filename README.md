# NLP_Group12_CookBook

---

# Recipe Chatbot

This project is a recipe chatbot that can interactively guide users through recipes, answer questions about the ingredients, methods, tools, and provide step-by-step instructions. The chatbot can also handle queries about ingredient quantities, cooking techniques, and more.

## Features

- **Recipe Retrieval and Display**: Fetches and displays recipes from supported websites.
- **Interactive Navigation**: Allows users to navigate through recipe steps, view ingredients, methods, and tools.
- **Query Support**: Handles specific queries about ingredient quantities, cooking methods, and tools.
- **Customizable Parsing**: Can parse recipes from multiple websites with the ability to extract ingredients, steps, methods, and tools.
- **Flexible Query Handling**: Supports a variety of user queries, including vague questions inferred from the current step.

## Getting Started

### Prerequisites

Ensure you have Python installed on your system. The required libraries are listed in the `requirements.txt` file. You can install them using:

```bash
pip install -r requirements.txt
```

### How to Use

1. **Run the Main Script**:
   - To start the chatbot, run the `main.py` file.
   - The chatbot will prompt you to enter the URL of a recipe from a supported website.

   ```bash
   python main.py
   ```

2. **Interactive Chat**:
   - The chatbot will guide you through the recipe, allowing you to view ingredients, methods, and tools, or navigate through the steps.
   - You can ask questions like:
     - "How much sugar do I need?"
     - "What is a whisk?"
     - "How do I sauté?"
     - "Take me to the next step."
   - The chatbot will respond accordingly, providing the relevant information or moving through the recipe.

3. **Example Queries**:
   - "Show me the ingredients list."
   - "What temperature should I bake this at?"
   - "When is it done?"
   - "What tools do I need for this step?"

### Code Overview

- **main.py**: The entry point of the application. It handles user input and starts the chatbot interaction.
- **parser.py**: Contains the `fetch_recipe` function to fetch and parse recipe data from a given URL.
- **recipe.py**: Defines the `Recipe` class, which manages the recipe details like ingredients, steps, and methods.
- **chatbot.py**: Manages the interactive conversation with the user, handling various queries and commands.
- **handlequery.py**: Provides functions to generate search queries for help questions on Google or YouTube.

### Extending the Code

- **Adding New Parsers**: To support additional recipe websites, you can extend the `fetch_recipe` function in `parser.py` with specific parsing logic for each new site.
- **Enhancing Query Handling**: Modify `chatbot.py` to handle more complex queries or improve the conversational capabilities.

## Troubleshooting

- **Common Errors**: If the chatbot doesn't fetch the recipe, ensure the URL is from a supported website and that your internet connection is stable.
- **Parsing Issues**: If the parser fails to extract information, you may need to update the parsing logic in `parser.py` to account for changes in the website's HTML structure.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgments

- Inspired by cooking and recipe enthusiasts.
- Built using Python and various open-source libraries.

---
