
from itertools import product

# Implication function
def implies(a, b):
    return (not a) or b


# Knowledge Base
def KB(P, Q, R):
    return (
        implies(Q, P)
        and implies(P, not Q)
        and (Q or R)
    )


# Main program
print("P Q R | Q->P | P->~Q | QvR | KB")

models = []

# Generate all possible combinations
for P, Q, R in product([False, True], repeat=3):

    a = implies(Q, P)
    b = implies(P, not Q)
    c = Q or R

    kb_value = KB(P, Q, R)

    print(
        int(P), int(Q), int(R), "|",
        int(a), "   |",
        int(b), "    |",
        int(c), "  |",
        int(kb_value)
    )

    if kb_value:
        models.append((P, Q, R))


# Entailment checking function
def entails(query):
    for P, Q, R in models:
        if not query(P, Q, R):
            return False
    return True


# Queries
print("\nModels of KB:", models)

print("\nKB entails R:",
      entails(lambda P, Q, R: R))

print("KB entails R -> P:",
      entails(lambda P, Q, R: implies(R, P)))

print("KB entails Q -> R:",
      entails(lambda P, Q, R: implies(Q, R)))
                                                                              