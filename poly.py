class Node():
    def __init__(self, coef, exp):
        self.coef=coef
        self.exp=exp
        self.next=None

    def get_coef(self):
        return self.coef

    def get_exp(self):
        return self.exp

    def get_next(self):
        return self.next

    def set_coef(self, new_coef):
        self.coef = new_coef

    def set_exp(self, new_exp):
        self.next = new_exp

    def set_next(self, new_next):
        self.next=new_next

    def __str__(self):  # returns the string representation of the object
        # it is called when print() or str() function is invoked on an object
        return  str(self.coef) + "x^"+str(self.exp)


#returns a new node
def multiply(Node1, Node2):
    c1=Node1.get_coef()
    c2=Node2.get_coef()
    e1=Node1.get_exp()
    e2=Node2.get_exp()
    m=Node(c1*c2 , e1+e2)
    return m



class Poly():
    def __init__(self, head=None):
        self.head=head

    def is_empty(self):
        return self.head == None

    def __str__(self):
        s = ""
        if self.is_empty():
            return s + "None"
        current = self.head
        while current:
            s += str(current) + '+'
            current = current.get_next()
        return s[:-1]

    def get_degree(self):
        return self.head.get_exp()
#add a node aka add c*x^e
    def add(self, c, e):
        if c==0:
            return None
        node=Node(c,e)
        #prima pensiamo alla testa
        if self.is_empty() or self.head.get_exp() < e:
            node.set_next(self.head)
            self.head=node
        elif self.head.get_exp()==e:
            if self.head.get_coef()==-c:
                self.head=self.head.get_next()
            else:
                self.head.set_coef(self.head.get_coef()+c)

        else:
            probe=self.head
            #in the while loop i check if there is a next and if the next has exponent grater
            while probe.get_next() and probe.get_next().get_exp() > e:
                probe=probe.get_next()

            if not probe.get_next():
                probe.set_next(node)

            elif probe.get_next().get_exp() == e:
                c1=probe.get_next().get_coef()
                if c1 == -c:
                    probe.set_next(probe.get_next().get_next())
                else:
                    probe.get_next().set_coef(c + c1)

            #in this case i'm sure the next has exponent lower than c
            #quindi metto in mezzo
            else:
                node.set_next(probe.get_next())
                probe.set_next(node)
        return node



def sum(p1,p2):
    if p1.is_empty():
        return p2
    if p2.is_empty():
        return p1
    s=Poly()
    probe1=p1.head
    probe2=p2.head
    #i do this in order to compare less nodes
    while probe1 and probe2:
        c1=probe1.get_coef()
        c2=probe2.get_coef()
        e1=probe1.get_exp()
        e2=probe2.get_exp()
        s.add(c1,e1)
        s.add(c2,e2)
        probe1 = probe1.get_next()
        probe2 = probe2.get_next()
    if probe1:
        while probe1:
            c1 = probe1.get_coef()
            e1 = probe1.get_exp()
            s.add(c1,e1)
            probe1 = probe1.get_next()
    if probe2:
        while probe2:
            c2 = probe2.get_coef()
            e2 = probe2.get_exp()
            s.add(c2,e2)
            probe2 = probe2.get_next()
    return s



#we assume node is not empty
def nodeMultiply(p1,node):
    p=Poly()
    if p1.is_empty():
        return p
    probe=p1.head
    while probe:
        c=multiply(probe,node).get_coef()
        e=multiply(probe,node).get_exp()
        p.add(c,e)
        probe=probe.get_next()
    return p


def pMultiply(p1,p2):
    p=Poly()
    if p1.is_empty() or p2.is_empty():
        return p
    #I first add the becuase I don't want to check again the first polynomial
    p=nodeMultiply(p1,p2.head)
    probe=p2.head.get_next()
    #traverse p2 and multiply each element for p1
    while probe:
        p=sum(p,nodeMultiply(p1,probe))
        probe=probe.get_next()
    return p











