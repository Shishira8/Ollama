import ollama
import os

model = "llama3.2"

input = "data/groceries.txt"
output = "data/categorised_groceries.txt"

if not os.path.exists(input):
    print(f"{input} not found")
    exit(1)

with open(input, "r") as f:
    items = f.read().strip()

prompt = f"""
You are an assistant that categorizes and sorts grocery items.

Here is a list of grocery items:

{items}

Please:

1. Categorize these items into appropriate categories such as Produce, Dairy, Meat, Bakery, Beverages, etc.
2. Sort the items alphabetically within each category.
3. Present the categorized list in a clear and organized manner, using bullet points or numbering.

"""
try:
    response = ollama.generate(model=model, prompt=prompt)
    generated_text = response.get("response", "")
    print("==== Categorized List: ===== \n")
    print(generated_text)

    # Write the categorized list to the output file
    with open(output, "w") as f:
        f.write(generated_text.strip())

    print(f"Categorized grocery list has been saved to '{output}'.")
except Exception as e:
    print("An error occurred:", str(e))