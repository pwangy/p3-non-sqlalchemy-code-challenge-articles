class Article:
    def __init__(self, author, magazine, title):
        self.author = author
        self.magazine = magazine
        self.title = title

    @property
    def title(self):
        return self._title

    @title.setter
    def title(self, title):
        if not isinstance(title, str):
            raise TypeError(f'Title must be a string.')
        elif not 5 <= len(title) <= 50:
            raise ValueError(f'Title must be between 5 and 50 characters long.')
        elif hasattr(self, "title"):
            raise AttributeError(f'Titles cannot be changed!')
        else:
            self._title = title


class Author:
    def __init__(self, name):
        self.name = name
        
    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name):
        if not isinstance(name, str):
            raise TypeError(f'Name must be a string.')
        elif not len(name) > 0:
            raise ValueError(f'Name cannot be empty.')
        elif hasattr(self, "name"):
            raise AttributeError(f'Names cannot be changed.')
        else:
            self._name = name

    def articles(self):
        pass

    def magazines(self):
        pass

    def add_article(self, magazine, title):
        pass

    def topic_areas(self):
        pass


class Magazine:
    def __init__(self, name, category):
        self.name = name
        self.category = category

    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, name):
        if not isinstance(name, str):
            raise TypeError(f'Name must be a string.')
        elif not 2 <= len(name) <= 16:
            raise ValueError(f'Name must be between 2 and 16 characters long.')
        else:
            self._name = name

    @property
    def category(self):
        return self._category
    
    @category.setter
    def category(self, category):
        if not isinstance(category, str):
            raise TypeError(f'Category must be a string.')
        elif not len(category) > 0:
            raise ValueError(f'Name cannot be empty.')
        else:
            self._category = category

    def articles(self):
        pass

    def contributors(self):
        pass

    def article_titles(self):
        pass

    def contributing_authors(self):
        pass

# ### Object Relationship Methods and Properties
# #### Article

# - `Article property author`
#   - Returns the author object for that article
#   - Must be of type `Author`
#   - Authors **can be changed** after the article object is initialized
# - `Article property magazine`
#   - Returns the magazine object for that article
#   - Must be of type `Magazine`
#   - Magazines **can be changed** after the article object is initialized

# #### Author

# - `Author articles()`
#   - Returns a list of all the articles the author has written
#   - Must be of type `Article`
# - `Author magazines()`
#   - Returns a **unique** list of magazines for which the author has contributed
#     to
#   - Must be of type `Magazine`

# #### Magazine

# - `Magazine articles()`
#   - Returns a list of all the articles the magazine has published
#   - Must be of type `Article`
# - `Magazine contributors()`
#   - Returns a **unique** list of authors who have written for this magazine
#   - Must be of type `Author`

# ### Aggregate and Association Methods

# #### Author

# - `Author add_article(magazine, title)`
#   - Receives a `Magazine` instance, and a title as arguments
#   - Creates and returns a new `Article` instance and associates it with that
#     author, the magazine provided
# - `Author topic_areas()`
#   - Returns a **unique** list of strings with the categories of the magazines
#     the author has contributed to
#   - Returns `None` if the author has no articles

# #### Magazine

# - `Magazine article_titles()`
#   - Returns a list of the titles strings of all articles written for that
#     magazine
#   - Returns `None` if the magazine has no articles
# - `Magazine contributing_authors()`
#   - Returns a list of authors who have written more than 2 articles for the
#     magazine
#   - Authors must be of type `Author`
#   - Returns `None` if the magazine has no authors with more than 2 publications

# ### Advanced Deliverables

# These deliverables are not required to pass the code challenge, but if you have
# the extra time, or even after the code challenge, they are a great way to
# stretch your skills.

# #### Bonus: Aggregate and Association Method

# - `Magazine classmethod top_publisher()`
#   - Returns the `Magazine` instance with the most articles
#   - Returns `None` if there are no articles.
#   - Uncomment lines 206-224 in the magazine_test file
#   - _hint: will need a way to remember all magazine objects_

# #### Bonus: For any invalid inputs raise an `Exception`

# - First, **comment out** the following lines
#   - **article_test.py**
#     - lines 28-29
#   - **author_test.py**
#     - lines 31-32, and 35-36
#   - **magazine_test.py**
#     - lines 31-32, 47-48, 51-52, 84-85, and 100-102
# - Then, **uncomment** the following lines in the test files
#   - **article_test.py**
#     - lines 34-35, 46-47, and 50-51
#   - **author_test.py**
#     - lines 39-40, and 53-54
#   - **magazine_test.py**
#     - lines 35-36, 55-56, 59-60, 90-91, and 105-106




## Topics
# Classes and Instances
# Class and Instance Methods
# Variable Scope
# Object Relationships
# lists and list Methods


# Writing error-free code is more important than completing all of the deliverables listed - prioritize writing methods that work over writing more methods that don't work. You should test your code in the console as you write.

# Similarly, messy code that works is better than clean code that doesn't. First, prioritize getting things working. Then, if there is time at the end, refactor your code to adhere to best practices. When you encounter duplicated logic, extract it into a shared helper method.

