from flask import Blueprint, render_template

examples_bp = Blueprint('examples', __name__)

EXAMPLES = [
    {
        "slug": "hello-world",
        "title": "Hello Bakery",
        "description": "Your very first recipe - make Chef SnackPie talk!",
        "difficulty": "beginner",
        "tags": ["say", "strings"],
        "code": 'say "Welcome to the SnackPie Bakery!"\nsay \'Fresh code baked daily 🥧\'',
        "previewOutput": ">>>>Welcome to the SnackPie Bakery!\n>>>>Fresh code baked daily 🥧"
    },
    {
        "slug": "variables",
        "title": "Ingredient Jars",
        "description": "Store your favorite ingredients in labeled jars!",
        "difficulty": "beginner",
        "tags": ["say", "variables"],
        "code": 'chef_name = "Alex"\nsay chef_name\nage = "12"\nsay age',
        "previewOutput": ">>>>Alex\n>>>>12"
    },
    {
        "slug": "ask-name",
        "title": "Meet the Chef",
        "description": "Ask for someone's name and greet them!",
        "difficulty": "beginner",
        "tags": ["ask", "say", "variables"],
        "code": 'name = ask "What is your name? "\nsay "Hello, "',
        "previewOutput": '>>>>What is your name? \n>>>>Hello, '
    },
    {
        "slug": "math",
        "title": "Kitchen Calculator",
        "description": "Crunch numbers like a pro chef!",
        "difficulty": "beginner",
        "tags": ["math"],
        "code": '3 * 5\n120 / 5\n10 + 20',
        "previewOutput": ">>>>15\n>>>>24.0\n>>>>30"
    },
    {
        "slug": "guessing-game",
        "title": "Guess the Secret Number",
        "description": "Can you guess Chef's secret ingredient number?",
        "difficulty": "intermediate",
        "tags": ["ask", "if", "math", "variables"],
        "code": '_secret = 7\nguess = ask "Guess a number 1-10: "\nif guess == _secret:\n say "You found the secret! 🎉"\nelse:\n say "Not quite, try again!"\nend',
        "previewOutput": ">>>>Guess a number 1-10: \n>>>>You found the secret! 🎉"
    },
    {
        "slug": "cookie-counter",
        "title": "Cookie Clicker",
        "description": "Count your cookies with style!",
        "difficulty": "intermediate",
        "tags": ["variables", "math", "if"],
        "code": 'cookies = 0\ncookies = cookies + 1\nif cookies > 0:\n say "You have cookies! 🍪"\nelse:\n say "No cookies yet!"\nend',
        "previewOutput": ">>>>You have cookies! 🍪"
    },
    {
        "slug": "recipe-maker",
        "title": "Recipe Builder",
        "description": "Build your own custom recipe!",
        "difficulty": "advanced",
        "tags": ["ask", "say", "variables", "if"],
        "code": 'recipe_name = ask "What are we making? "\ningredient = ask "Main ingredient: "\nsay "Let\'s make " + recipe_name\nsay "Main ingredient: " + ingredient',
        "previewOutput": ">>>>What are we making? \n>>>>Main ingredient: \n>>>>Let's make "
    }
]


@examples_bp.route('/')
def index():
    """Gallery of code examples."""
    return render_template('examples/index.html', examples=EXAMPLES)


@examples_bp.route('/<slug>')
def detail(slug):
    """Single example with editor."""
    example = next((e for e in EXAMPLES if e['slug'] == slug), None)
    if not example:
        from flask import abort
        abort(404)
    return render_template('examples/detail.html', example=example)