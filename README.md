# 🥧 SnackPie: The Easiest Programming Language for Kid Chefs! 🍕✨

Welcome to **SnackPie**, the friendly, delicious, and bite-sized programming language inspired by Python! Designed especially for kids and beginner coding chefs, SnackPie turns writing code into **baking delicious software recipes**! 

---

## 👩‍🍳 Meet Chef SnackPie! (The Project Persona)

In the SnackPie kitchen, we don't believe in scary error messages or confusing jargon. **Chef SnackPie** is your helpful kitchen buddy. 

Instead of typing scary "code," kids are building **Recipes** (using `.pie` files).
Instead of "compiling and executing," Chef SnackPie helps us **Bake** our recipe in the kitchen to see how it tastes!

SnackPie is built to be read like a simple recipe book, ensuring that young learners build confidence, have fun, and learn the core concepts of Python without the stress.

---

## 🍳 The SnackPie Kitchen Pantry (How to Code)

Here is a guide to the basic ingredients you can find in the SnackPie kitchen:

### 1. Serving Up Words (`say`) 🗣️
To show something on the screen, just tell Chef SnackPie to `say` it!
```pie
say "Welcome to the SnackPie Bakery!"
say 'Baking is fun!'
```
*Chef SnackPie will serve it right up:*
```text
>>>>"Welcome to the SnackPie Bakery!"
```

### 2. Storing Ingredients in Jars (Variables) 📦
When you want to save a value, put it in a labeled jar using `=`! 
> [!IMPORTANT]
> Keep your values inside quotes (`"` or `'`) when putting them in jars. Chef SnackPie will figure out if they are words or numbers!
```pie
chef_name = "Alex"
say chef_name
```

### 3. Secret Ingredients (Constants) 🔒
Sometimes, you have a special ingredient that **nobody** is allowed to change (like the secret recipe!). Just start the jar's name with an underscore `_`, and Chef SnackPie will protect it!
```pie
_secret_sauce = "Honey & Mustard"
# If anyone tries to change _secret_sauce later, Chef SnackPie will say:
# "ERROR: This is a const, it can't be changed" 🛑
```

### 4. Asking the Diner (`ask`) 🙋‍♂️
Need to get an ingredient or an answer from the person running your recipe? Use `ask`!
```pie
favorite_pie = ask "What is your favorite kind of pie? "
```

### 5. Quick Kitchen Math 🧮
Chef SnackPie is super fast at counting cookies. Just type a simple math problem:
```pie
3 * 5
120 / 5
```
*Chef SnackPie will instantly say:*
```text
>>>>15
>>>>24.0
```

### 6. The Taste Test (Conditionals) 🧭
To make decisions, use an `if` block, add extra tests with `orif`, write a backup with `else`, and finish with `end`!
> [!NOTE]
> Make sure to add a single space before the instructions inside the taste test, so Chef SnackPie knows they belong to that step!
```pie
cookies_in_oven = "12"

if cookies_in_oven == 12:
 say 'Perfect batch!'
orif cookies_in_oven > 12:
 say 'The oven is too full!'
else:
 say 'We need to bake more!'
end
```

---

## 👩‍🍳 Baking Your First Recipe!

Let's get cooking! Here is how to run SnackPie on your computer.

### Step 1: Fire up the Oven (Interactive Console)
Open your terminal and run:
```bash
python3 snackpie.py
```
This opens the interactive kitchen. You can type commands one line at a time and see the results instantly! Type `exit()` to leave the kitchen.

### Step 2: Read from a Recipe Book (Run a `.pie` file)
You can write a whole recipe inside a file ending with `.pie` (like `test.pie`), then run:
```bash
python3 interpreter.py
```
Chef SnackPie will ask you for the file name. Type `test.pie` and hit Enter to watch your program run from top to bottom!

---

## 🍕 Join the Bakery!

SnackPie is an open-source baking school. If you want to add new ingredients (like loops, lists, or new functions), feel free to fork the repository, make a new recipe, and send a Pull Request! 

Happy baking! 🥧✨