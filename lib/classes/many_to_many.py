class Article:
    all = []

    def __init__(self, author, magazine, title):
        self.author = author
        self.magazine = magazine
        self.title = title
        type(self).all.append(self)

    @property
    def title(self):
        return self._title

    @title.setter
    def title(self, title):
        if hasattr(self, "title"):
            raise AttributeError(f"Titles cannot be changed!")
        elif not isinstance(title, str):
            raise TypeError(f"Title must be a string.")
        elif not 5 <= len(title) <= 50:
            raise ValueError(f"Title must be between 5 and 50 characters long.")
        else:
            self._title = title

    @property
    def author(self):
        return self._author

    @author.setter
    def author(self, author):
        if not isinstance(author, Author):
            raise TypeError(f"author must be Author.")
        else:
            self._author = author

    @property
    def magazine(self):
        return self._magazine

    @magazine.setter
    def magazine(self, magazine):
        if not isinstance(magazine, Magazine):
            raise TypeError(f"magazine must be Magazine.")
        else:
            self._magazine = magazine


class Author:
    def __init__(self, name):
        self.name = name

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name):
        if hasattr(self, "name"):
            raise AttributeError(f"Names cannot be changed.")
        elif not isinstance(name, str):
            raise TypeError(f"Name must be a string.")
        elif not len(name) > 0:
            raise ValueError(f"Name cannot be empty.")
        else:
            self._name = name

    def articles(self):
        return list({article for article in Article.all if article.author is self})

    def magazines(self):
        return list(
            {article.magazine for article in Article.all if article.author is self}
        )

    def add_article(self, magazine, title):
        return Article(self, magazine, title)

    def topic_areas(self):
        topics = list(
            {
                article.magazine.category
                for article in Article.all
                if article.author is self
            }
        )
        if len(topics) > 0:
            return topics
        else:
            return None


class Magazine:
    all = []

    def __init__(self, name, category):
        self.name = name
        self.category = category
        type(self).all.append(self)

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name):
        if not isinstance(name, str):
            raise TypeError(f"Name must be a string.")
        elif not 2 <= len(name) <= 16:
            raise ValueError(f"Name must be between 2 and 16 characters long.")
        else:
            self._name = name

    @property
    def category(self):
        return self._category

    @category.setter
    def category(self, category):
        if not isinstance(category, str):
            raise TypeError(f"Category must be a string.")
        elif not len(category) > 0:
            raise ValueError(f"Name cannot be empty.")
        else:
            self._category = category

    def articles(self):
        return list({article for article in Article.all if article.magazine is self})

    def contributors(self):
        return list(
            {article.author for article in Article.all if article.magazine is self}
        )

    def article_titles(self):
        every_article_title = list(
            article.title for article in Article.all if article.magazine is self
        )
        if not len(every_article_title) > 0:
            return None
        else:
            return every_article_title

    def contributing_authors(self):
        count_author_articles = {}

        for article in self.articles():
            author = article.author
            if author in count_author_articles:
                count_author_articles[author] += 1
            else:
                count_author_articles[author] = 1

        repeat_contributors = [
            author for author, count in count_author_articles.items() if count > 2
        ]

        if repeat_contributors:
            return repeat_contributors
        else:
            None

    #   - Returns the `Magazine` instance with the most articles
    #   - Returns `None` if there are no articles.
    @classmethod
    def top_publisher(cls):
        try:
            return max(
                cls.all,
                key=lambda magazine:
                    len(magazine.articles()) if magazine.articles() else None
            )
        except Exception as e:
            print(e)
            return None

# author_1 = Author("Isabella Blow")
# author_2 = Author("Nathaniel Hawthorne")
# magazine_1 = Magazine("Vogue", "Fashion")
# magazine_2 = Magazine("Eye", "Design")
# Article(author_1, magazine_1, "How to wear a hat with style")
# Article(author_2, magazine_1, "Miss Lonely Hearts")
# Article(author_1, magazine_1, "How to wear a tutu with style")
# Article(author_1, magazine_2, "Dating life in NYC")
# Article(author_1, magazine_2, "2023 Eccentric Design Trends")
