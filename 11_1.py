"""class Publication:
    def __init__(self, name):
       self.name = name

    def print_info(self):
        print(self.name, end= " ")

class Book(Publication):
    def __init__(self, name, author, page_num,):
        super().__init__(name)
        self.author = author
        self.page_num = page_num
    def print_info(self):
        super().print_info()
        print(" Author:" + self.author + "," + str(self.page_num) + "pages)")

class Magazine(Publication):
    def __init__(self, name, editor):
        super().__init__(name)
        self.editor = editor

    def print_info(self):
        super().print_info()
        print("(chief editor" + ":" + self.editor + ")")


pubs = []
pubs.append(Magazine("Awesome Ghimire", "Subu Ghimire"))
pubs.append(Book("Compartment No.6", "Rose Likesom", 192))

for pub in pubs:
    pub.print_info()"""

class Publication:
    def __init__(self, name):
        self.name = name
    def print_info(self):
        print(self.name)

class Book(Publication):
    def __init__(self,name, author, page_count):
        super().__init__(name)
        self.author = author
        self.page_count = page_count


    def print_info(self):
        super().print_info()
        print(f"Author: {self.author}, Pages: {self.page_count}")

class Magazine(Publication):
    def __init__(self,name, chief_editor):
        super().__init__(name)
        self.chief_editor = chief_editor


    def print_info(self):
        super().print_info()
        print(f"Chief Editor: {self.chief_editor}")

publications=[]
publications.append(Book("Compartment no. 6","Rosa Liksom", 192))
publications.append(Magazine("Donald Duck", "Aki Hyyppä"))


for p in publications:
    p.print_info()


