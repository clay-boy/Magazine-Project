class Author:
    def __init__(self, name):
        if isinstance(name, str) and len(name) > 0:
            self._name = name
        else:
            raise Exception("Name must be a non-empty string.")
    
    @property
    def name(self):
        return self._name
    
    def articles(self):
        return "This method depends on Article class"

    def magazines(self):
        return "This method depends on Article class"

    def add_article(self, magazine, title):
        return "This method depends on Article class"
    
    def topic_areas(self):
        return "This method depends on Magazine and Article class"

# Test the Author class directly in this file
if __name__ == "__main__":
    print("Testing Author class")

    # Test author initialization
    print("Testing valid Author initialization")
    author = Author("John Doe")
    print(f"Author name: {author.name}")

    # Test invalid author initialization
    print("Testing invalid Author initialization")
    try:
        invalid_author = Author("")
    except Exception as e:
        print(f"Error: {e}")
