#αυτο ειναι το πρωτο ερωτημα
my_int = 42
my_float = 3.14
my_string = "Hello, World!"

print("Integer:", my_int)
print("Float:", my_float)
print("String:", my_string)

#εδω ειναι το δευτερο ερωτημα
print(f"ο ακεραιος αριθμος ειναι {my_int}, ο πραγματικος αριθμος ειναι {my_float}, και το κειμενο λεει: '{my_string}'.")


#εδω ειναι το τριτο ερωτημα
print(f"η συμβολοσειρα μου για τον τιτλο: '{my_string.title()}', στα μικρα γραμματα: '{my_string.lower()}', στα κεφαλαια γραμματα: '{my_string.upper()}'.")


#εδω ειναι το τεταρτο ερωτημα
my_list = ["μηλο", "αχλαδι", "μπανανα", 7, 410]
print(f"η λιστα μου ειναι αυτη: {my_list}")


#  βαζω στοιχεια στην λιστα
my_list.append("κερασι")
print(f"η λιστα μετα που βαλαμε τα στοιχεια: {my_list}")


# βγαζω στοιχεια απο την λιστα
my_list.remove(410)
print(f"η λιστα μετα που βγαλαμε τα στοιχεια: {my_list}")


# εκτυπωση ολων των στοιχειων της λιστας
print("Ολα τα στοιχεια της λιστας:")
for item in my_list:
    print(item)
