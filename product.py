class Product(object):
    def __init__(self, id, max_weight):
        self.id = id
        self.max_weight = max_weight

    #http://stackoverflow.com/questions/4901815/object-of-custom-type-as-dictionary-key
    def __hash__(self):
        return hash((self.id, self.max_weight))

    def __eq__(self, other):
        return (self.id, self.max_weight) == (other.id, other.max_weight)

    def __repr__(self):
        return '<Product id=%r,max_weight=%r>' % (self.id, self.max_weight)
