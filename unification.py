def unify(a, b, subst):
    if a == b:
        return subst

    if isinstance(a, str) and a.islower():
        if a in subst:
            return unify(subst[a], b, subst)

        if a in str(b):
            return None

        subst[a] = b
        return subst

    if isinstance(b, str) and b.islower():
        return unify(b, a, subst)

    if isinstance(a, tuple) and isinstance(b, tuple):
        if len(a) != len(b):
            return None

        for x, y in zip(a, b):
            subst = unify(x, y, subst)

            if subst is None:
                return None

        return subst

    return None


# Main program
e1 = ("Likes", "x", "Mango")
e2 = ("Likes", "Rahul", "y")

result = unify(e1, e2, {})

if result is None:
    print("Unification Failed")
else:
    print("Unification Successful")
    print("Substitution:", result)