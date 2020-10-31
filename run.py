
from nnf import Var 

from lib204 import Encoding 

# Variables 

t1 = Var('t1') #Olivia 

t2 = Var('t2') #Ulric 

t3= Var('t3') #Alice 

t4= Var('t4') #Yates 

t5= Var('t5') #Bob 

t6= Var('t6') #Zara 

t7= Var('t7') #Sam 

t8= Var('t8') #Jeff 

t9= Var('t9') #Quentin 

t10= Var('t10') #Valerie 

t11= Var('t11') #Roslina 

t12= Var('t12') #Wallace 

t13= Var('t13') #Nate 

t14= Var('t14') #Harry 

t15= Var('t15') #Karen 

t16= Var('t16') #Eva 

t17= Var('t17') #Gale 

t18= Var('t18') #Chloe 

t19= Var('t19') #Larry 

t20= Var('t20') #Farrel 

t21= Var('t21') #Michelle 

t22= Var('t22') #Perry 

  

  

# Build an example full theory for your setting and return it. 

#  There should be at least 10 variables, and a sufficiently large formula to describe it (>50 operators). 

#  This restriction is fairly minimal, and if there is any concern, reach out to the teaching staff to clarify 

#  what the expectations are. 

def example_theory(): 

    E = Encoding() 

    E.add_constraint(t1 >> (~t2 & ~t3)) 

    E.add_constraint(t4 >> (~t4 & t5)) 

    E.add_constraint(t1 >> (t6)) 

    E.add_constraint(t7 >> (~t8 | ~t9)) 

    E.add_constraint(t10 >> (~t11)) 

    E.add_constraint(t12 >> ((~t7 | t1) & ~(~t7 & t1)))   

    E.add_constraint(t13 >> (t14 | t15)) 

    E.add_constraint(t16 >> (~t7)) 

    E.add_constraint(t7 >> (t13)) 

    E.add_constraint(t10 >> (t17 >> (~t16 & t4))) 

    E.add_constraint(t9 >> (~t18 | ~t19)) 

    E.add_constraint(t20 >> (t14 & t21)) 

    E.add_constraint(t5 >> (t10 | t22)) 

    E.add_constraint(t11 >> (t15 >> (~t9 | t14))) 

    E.add_constraint(t12 >> (t10)) 

    E.add_constraint(t10 >> (~t21 & t4)) 

    E.add_constraint(t19 >> (t22)) 

    E.add_constraint(t18 >> (~t13 & ~t5) & t7) 

    E.add_constraint(t3 >> (~t21 & (t16 & t22))) 

    return E 


if __name__ == "__main__":

    T = example_theory()

    print("\nSatisfiable: %s" % T.is_satisfiable())
    print("# Solutions: %d" % T.count_solutions())
    print("   Solution: %s" % T.solve())

    #print("\nVariable likelihoods:")
    #for v,vn in zip([a,b,c,x,y,z], 'abcxyz'):
        #print(" %s: %.2f" % (vn, T.likelihood(v)))
    #print()
