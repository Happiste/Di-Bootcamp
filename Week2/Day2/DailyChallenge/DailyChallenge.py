class Pagination:
    def __init__(self, items=None, pageSize=10):
        self.items = items
        self.pageSize = pageSize
        self.currentPage = 1
        self.totalPage = 

    def getVisibleItems(self):

        start= (self.currentPage - 1) * self.pageSize
        ending = self.currentPage * self.pageSize
        print(self.items[start:ending])

    def next_page(self):
        self.currentPage += 1

    def prev_page(self):
        self.currentPage -= 1

    def first_page(self):
        self.currentPage = 1
    
    def last_page(self):
        pass

    def goToPage(self, num=1):
        self.currentPage = num
        


if __name__=='__main__':
    alphabetList = list("abcdefghijklmnopqrstuvwxyz")
    p = Pagination(alphabetList, 4)
    p.getVisibleItems()
    p.next_page()
    p.getVisibleItems()
    p.next_page()
    p.getVisibleItems()
    p.prev_page()
    p.getVisibleItems()
    p.first_page()
    p.getVisibleItems()
    #p.last_page()
    p.goToPage(7)
    p.getVisibleItems()
