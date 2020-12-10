# Import Libraries
from nnf import Var
from nnf import NNF
from nnf.operators import iff
from lib204 import Encoding

# Define functions for 'missing' operators
def implication(l, r):
    return l.negate() | r

def neg(f):
    return f.negate()

NNF.__rshift__ = implication
NNF.__invert__ = neg


# Define a variable for each person in the problem
Olivia= Var('t1') #Olivia
Ulric= Var('t2') #Ulric
Alice= Var('t3') #Alice
Yates= Var('t4') #Yates
Bob= Var('t5') #Bob
Zara= Var('t6') #Zara
Sam= Var('t7') #Sam
Jeff= Var('t8') #Jeff
Quentin= Var('t9') #Quentin
Valerie= Var('t10') #Valerie
Rosalina= Var('t11') #Rosalina
Wallace= Var('t12') #Wallace
Nate= Var('t13') #Nate
Harry= Var('t14') #Harry
Karen= Var('t15') #Karen
Eva= Var('t16') #Eva
Gale= Var('t17') #Gale
Chloe= Var('t18') #Chloe
Larry= Var('t19') #Larry
Farrel= Var('t20') #Farrel
Michelle= Var('t21') #Michelle
Perry= Var('t22') #Perry

# List of people in the problem
people = [Olivia,Ulric,Alice,Yates,Bob,Zara,Sam,Jeff,Quentin,Valerie,Rosalina,Wallace,Nate,Harry,
    Karen,Eva,Gale,Chloe,Larry,Farrel,Michelle,Perry]

# Create model
def knight_knaves():
    E = Encoding()
    # Statement 1: Olivia says "Ulric and Alice lie"
    E.add_constraint(iff(Olivia , (~Ulric & ~Alice)))
    # Statement 2: Yates says "Yayes lies, and also Bob is truthful"
    E.add_constraint(iff(Yates , (~Yates & Bob)))
    # Statement 3: Olivia says "Zara is truthful"
    E.add_constraint(iff(Olivia , (Zara)))
    # Statement 4: Sam says "At least on of Jess or Quentin lies"
    E.add_constraint(iff(Sam , (~Jeff | ~Quentin)))
    # Statement 5: Valerie says "Roslina lies"
    E.add_constraint(iff(Valerie , (~Rosalina)))
    # Statement 6: Wallace says "Either Sam lies, or Olivia is truthful"
    E.add_constraint(iff(Wallace , ((~Sam | Olivia) & neg((~Sam & Olivia)))))
    # Statement 7: Nate says "At east one of Harry or Karen is truthful"
    E.add_constraint(iff(Nate , (Harry | Karen)))
    # Statement 8: Eva says "Sam lies"
    E.add_constraint(iff(Eva , (~Sam)))
    # Statement 9: Sam says "Nate is truthful"
    E.add_constraint(iff(Sam , (Nate)))
    # Statement 10: Valerie says "Gale would say 'Eva lies, and also Yates is truthful'"
    E.add_constraint(iff(Valerie , (iff(Gale , (~Eva & Yates)))))
    # Statement 11: Quentin says "At least one of Chloe or Larry lies"
    E.add_constraint(iff(Quentin , (~Chloe | ~Larry)))
    # Statement 12: Farrel says "Harry and Michelle are truthful"
    E.add_constraint(iff(Farrel , (Harry & Michelle)))
    # Statement 13: Bob says "At least one of Valerie or Perry is truthful"
    E.add_constraint(iff(Bob , (Valerie | Perry)))
    ## Statement 14: Rosalina says "Karen would say 'Either Quentin lies, or Harry is truthful'"
    E.add_constraint(iff(Rosalina , (iff(Karen , (~Quentin | Harry) & neg((~Quentin & Harry))))))
    # Statement 15: Wallace says "Valerie is truthful"
    E.add_constraint(iff(Wallace , (Valerie)))
    # Statement 16: Valerie says "Either Michelle lies, or Yates is truthful"
    E.add_constraint(iff(Valerie , (~Michelle | Yates) & neg((~Michelle & Yates))))
    # Statement 17: Larry says "Perry is truthful"
    E.add_constraint(iff(Larry , (Perry)))
        ### Explore: What happens if Larry instead says that "Perry lies"?
        ### E.add_constraint(iff(Larry , (~Perry)))
    # Statement 18: Chloe says "Nate and Bob lie, and also Sam is truthful"
    E.add_constraint(iff(Chloe , (~Nate & ~Bob) & Sam))
    # Statement 19: Alice says "Michelle lies, and also Eva and Perry are truthful"
    E.add_constraint(iff(Alice , (~Michelle & (Eva & Perry))))
        ### Explore: Quentin says "Olivia is truthful, and also Ulric lies"?
        ### (solves the issue of multiple solution)
    E.add_constraint(iff(Quentin, (Olivia & ~Ulric)))
    return E



if __name__ == "__main__":

    T = knight_knaves()

    print("\nSatisfiable: %s" % T.is_satisfiable())
    print("# Solutions: %d" % T.count_solutions())
    print("    Solution: %s" % T.solve())

    ### A more readable way to display results for model exploration purposes
    # Sol = T.solve()
    # Knights=[]
    # Knaves=[]
    # for i in Sol:
    #     if Sol[i]==True:
    #         Knights.append(i)
    #     else:
    #         Knaves.append(i)
    # print("Solution:\n     Knights: %s \n     Knaves: %s" %(sorted(Knights), sorted(Knaves)))

    print("\nVariable likelihoods:")
    for v,vn in zip(people, ['t1','t2','t3','t4','t5','t6','t7','t8','t9','t10','t11','t12','t13','t14','t15','t16','t17','t18','t19','t20','t21','t22']):
        print(" %s: %.2f" % (vn, T.likelihood(v)))
    print()
