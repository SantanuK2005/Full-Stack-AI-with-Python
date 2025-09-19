fevrate_chais = [
    "Red tea",
    "Lemon tea",
    "Masala Chai",
    "Red tea",
    "Masala Chai",
    "Lemon tea"
]

unique_chai = {chai for chai in fevrate_chais}
print(unique_chai)



recipes = {
    "masala chai" : ["ginger", "cardmom", "clove"],
    "elaichi chai" : ["cardamom", "mlik"],
    "spicy chai" : ["ginger", "red chai", "clove"]
}

unique_spices = {spice for ingredients in recipes.values()for spice in ingredients}
print(unique_spices)