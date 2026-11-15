# Author: Ali Zaboli

def greet(name):
    """Return a friendly greeting for the given name."""
    return f"Hello, {name}!"

def greet_formally(name):
    """Return a formal greeting for the given name."""
    return f"Good day, {name}. How do you do?"

def farewell(name):
    return f"Goodbye, {name}!"

if __name__ == "__main__":
    print(greet("World"))
    print(greet_formally("Professor"))
    print(farewell("World"))