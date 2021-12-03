class HomeLibrary(): 
 
    def init(self,author, publication,genre): 
        self.author = author 
        self.publication = publication 
        self.genre = genre 
        print("Книга выбрана") 
 
 
my_book = HomeLibrary("Robert Kiyosaki", "Sharon Lecter",1997,"startup") 
print(my_book.publication)