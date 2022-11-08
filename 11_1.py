class Publication:
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
    pub.print_info()
