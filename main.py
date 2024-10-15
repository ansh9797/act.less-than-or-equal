class a:
    def __init__(self,x):
        self.x=x

    def __lt__(self,y):
        if self.x<y:
            print("x is less than y.")
        else:
            print("x is not less than y.")

    def __eq__(self,y):
        if self.x==y:
            print("x is eqaul to y.")
        else:
            print("x is not eqaul to y.")

a1 = a(7)
a1.__lt__(2)
a1.__eq__(6)