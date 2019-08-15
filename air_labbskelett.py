# coding=utf-8
import csv;

############################################################################################
#
#  Hjälpfunktioner. Här behöver ni inte göra några ändringar.
#
############################################################################################
NorthernEurope = {'Sweden', 'Norway', 'Finland', 'Iceland', 'Denmark'}

def get_airports():
    """Helper function to read all the airports from a file, filters out all non-Nordic airports"""
    with open('data/airports.dat', 'r') as f:
        reader = csv.reader(f, delimiter=',')
        return  {line[4] for line in reader if (line[3] in NorthernEurope and len(line[4]) == 3)}

def get_routes(A):
    """
    Helper function to read all the routes from a file, keeps only routes where the
    airports belong to the set A
    """
    with open('data/routes.dat', 'r') as f:
        reader = csv.reader(f, delimiter=',')
        return {(line[2], line[4]) for line in reader if line[2] in A and line[4] in A}

def compose(R1,R2):
    """Composes two relations as R2 o R1"""
    return {(a,d) for (a,b) in R1 for (c,d) in R2 if b == c}


############################################################################################
#
# Funktioner ni behöver ändra eller skapa själva
#
############################################################################################
      
#Används i uppgift 3
def is_symmetrical(R):
    """Checks if the relation R is symmetrical"""
    #Ersätt med er egen kod.
    return False;

#Funktionen för uppgift 4 måste ni skriva själva här

#Används i uppgift 5
def get_dead_ends(A, R):
    """Returns all elements from A from which there is no outgoing relation in R"""
    #Ersätt med er egen kod.
    return set()

#Kan behövas i någon av uppgifterna
def get_source_matching_pairs(s, R):
    """Returns all pairs (i,j) from R where i matches the source s"""
    #Ersätt med lämplig kod
    return set()

#Kan behövas i flera av uppgifterna
def transitive_closure(R):
    """Returns the transitive closure of the relation R"""
    Rtrans = set(R); 
    #Ersätt med lämplig kod
    return Rtrans;

#Kan behövas i någon av uppgifterna
def get_number_of_hops(s, d, R):
    """
    Returns the number of hops required to reach from the source s to the 
    destination d, given the specified routes in R
    """
    #Ersätt med lämplig kod
    return -1;


############################################################################################
#
# Initialisering av mängden A och relationen R som används
# (flygplatser och rutter). Ingen ändring krävs här.
#
############################################################################################

A = get_airports()
R = get_routes(A)

#Get the transitive closure of the routes. Currently does not give the correct solution!
R_plus = transitive_closure(R);

############################################################################################
#
# Svar på frågorna, ändra och fyll i som lämpligt. 
#
############################################################################################


print ("*********************************************************************")
print ("1. Hur många flygplatser finns det i datamängden?")
#Ersätt 0 med rätt uttryck
print ("Svar: " + str(0));

print ("*********************************************************************")
print ("2. Hur många rutter finns det?")
#Ersätt 0 med rätt uttryck
print ("Svar: " + str(0))

print ("*********************************************************************")
print ("3. Om man kan flyga från flygplats A till flygplats B, går det då att flyga B till A?");
print ("För att besvara frågan undersöker  om relationen routes är symmetrisk");
#Lösning här. Obs ni behöver också göra ändringar i funktionen is_symmetrical.

print ("*********************************************************************")
print ("4. Finns det rutter som startar och stannar på samma flygplats?")
#Lösning här. Obs en ny funktion behövs för detta.

print ("*********************************************************************")
print ("5. Finns det flygplatser som man inte kan flyga ut ifrån?")
#Lösning här.

print ("*********************************************************************")
print ("6. Hur många flygplatser inom norden finns det direktflyg till från Arlanda (ARN)?")
#Lösning här.

print ("*********************************************************************")
print ("7. Kan man flyga från Linköping (LPI) till Bodö (BOO) utan att lämna norden?")
#Lösning här.

print ("*********************************************************************")
print ("8. Kan man flyga från Linköping till alla flygplatser i Norden utan att lämna Norden?")
#Lösning här.

print ("*********************************************************************")
print ("9. Hur många hopp måste man ta för att flyga från Linköping (LPI) för att komma till Florö (FRO) flygplats i Norge?")
#Lösning här.

print ("*********************************************************************")







