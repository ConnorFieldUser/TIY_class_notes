

class A:

    def __init__(self):
        self.ready = True


class B(A):
    def __init__(self, favorite):
        super().__init__()  # calls parent method first
        self.favorite = favorite


x = A()
print(x.ready)


y = B("jelly beans")
print(y.favorite)
print(y.ready)
