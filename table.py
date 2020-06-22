# table.py
import pickle
import itertools

class Table:
    def __init__(self, name='', fields = tuple(), tups = None):
        self.name = name
        self.fields = fields
        self.tups = tups
    def select(self, field, val):# takes a field name and a value as params
        self.field = field
        self.val = val
        # should name returned table result
        # returns a result table with each row having the value of the
        # specified field matching the passed in value
        result = []
        temp = []
        #store = {s for s in self.tups if s == val}
        '''thing = self.fields
        thing2 = thing.split(',')
        thing3 = thing2.index(field)
        # tups is a list of lists
        # self.tups[0] is the values 'p1, nut, red, 12, london'
        # need to split up the lists of lists so I can compare the values
        # in each sublist by the index
        for x in self.tups:
            c = x.split(',')
            if c[thing3] == val:
                result.append(c)
                return(result)
            #if x[thing3] == val:
                #result.append(x)'''
        indexes = []
        result = []
        fields = self.fields
        fields2 = fields.split(',')
        indexed = fields2.index(field)
        for x in self.tups:
            c = x.split(',')
            if(c[indexed] == val):    
                result.append(c)
        return(result)
    def project(self, *field):
        self.field = field
        # returns a result table with name result
        # takes one or more field names and returns a result
        # table with only the associated columns from each row
        indexes = []
        result = []
        fields = self.fields
        fields2 = fields.split(',')
        for item in field:
            indexed = fields2.index(item)
            indexes.append(indexed)
        thing = self.fields
        thing2 = thing.split(',')
        tupsTup = []
        for x in self.tups:
            for z in indexes:
                c = x.split(',')
                values =(c[z])
                result.append(values)
        return(result)
    @staticmethod
    def join(tab1, tab2):
        # return table named result
        # prints the rows of the cartesian product of its two tables
        # where the values in the like-named field are equal
        # assume joined tables only have one field name in common
        #print(tab1 + tab2)
        table1 = tab1.tups
        table2 = tab2.tups
        result = []
        '''print(table1)
        print(type(table1))
        first = itertools.product(table1,table2)
        second = itertools.product(table2,table1)
        joined = first + second
        return(joined)'''
        for t1 in table1:
            for t2 in table2:
                result += ((t1,t2))
        return(result)
    def insert(self, *tup):
        self.tup = tup
        # only attempt to add tuples to a table that
        # have the correct no. of fields
        # allow no duplicate tuples
        result = []
        for x in self.tups:
            c = x.split(',')    
            result.append(c)
        for z in tup:
            result.append(z)
        return(result)

    def remove(self, field, val):
        # removes all tuples from a table where the indicated
        # field matches the passed in value
        indexes = []
        result = []
        fields = self.fields
        fields2 = fields.split(',')
        indexed = fields2.index(field)
        for x in self.tups:
            c = x.split(',')
            result.append(c)
        for z in self.tups:
            c = z.split(',')
            if(c[indexed] == val):
                result.remove(c)

        return(result)

    def store(self):
        # store writes to a file named "<name>.db" where name is
        # the internal name of the table
        # use pickle.dump()
        name = self.name
        fileName = "%s.db" % name
        
        pickle.dump(self, open((fileName), "wb"))
    @staticmethod
    def restore(fname):
    # use pickle.load() read
        return pickle.load(open(fname, "rb"))
        
    @staticmethod
    def read(fname):
        # reads a text file and stores it in an object
        with open(fname, 'r') as f:
            stored = []
            stuff = [line.strip() for line in f]
            fname = stuff[0]
            fields = stuff[1]
            stuff.pop(0)
            stuff.pop(0)
            for x in stuff:
                stored.append(x)
                #tupleList = [tuple(l) for l in stored]
            return Table(fname, fields, stored)

    def write(self, fname):
        file = open(fname, 'w')
        file.write(self.name)
        file.write('\n')
        file.write(str(self.fields))
        file.write('\n')
        for z in self.tups:
            file.write(str(z))
            file.write('\n')
        file.close
        


    def __str__(self):
        tups = str(self.tups)
                
        return (self.name) + '\n' + ('=====') + '\n' + \
           str(self.fields) + '\n' + str(self.tups)
       
       
        
