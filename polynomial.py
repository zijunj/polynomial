class X:
    def __init__(self):
        pass

    def __repr__(self):
        return "X"
    
    def evaluate(self,i):
        return Int(i)
class Int:
    def __init__(self, i):
        self.i = i
    
    def __repr__(self):
        return str(self.i)
    
    def evaluate(self,i):
        return Int(self.i)

class Add:
    def __init__(self, p1, p2):
        self.p1 = p1
        self.p2 = p2
    
    def __repr__(self):
        return repr(self.p1) + " + " + repr(self.p2)
    
    def evaluate(self,i):
        p1 = self.p1.evaluate(i)
        p2 = self.p2.evaluate(i)
        return Int(p1.i + p2.i)


class Mul:
    def __init__(self, p1, p2):
        self.p1 = p1
        self.p2 = p2
    
    def __repr__(self):
        if isinstance(self.p1, Add):
            if isinstance(self.p2, Add):
                 return "( " + repr(self.p1) + " ) * ( " + repr(self.p2) + " )"
            return "( " + repr(self.p1) + " ) * " + repr(self.p2)
        if isinstance(self.p2, Add):
            return repr(self.p1) + " * ( " + repr(self.p2) + " )"
        return repr(self.p1) + " * " + repr(self.p2)
    
    def evaluate(self,i):
        p1 = self.p1.evaluate(i)
        p2 = self.p2.evaluate(i)
        return Int(p1.i * p2.i)
        

poly = Add( Add( Int(4), Int(3)), Add( X(), Mul( Int(1), Add( Mul(X(), X()), Int(1)))))
print(poly.evaluate(-1))