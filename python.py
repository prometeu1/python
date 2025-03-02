import time

# Listes de mots par niveau de difficulté
easy_words = ["chat", "chien", "maison", "arbre", "soleil", "fleur", "table", "chaise", "livre", "école"]
medium_words = ["ordinateur", "bouteille", "téléphone", "fenêtre", "montagne", "vélo", "cahier", "stylo", "lampe", "horloge"]
hard_words = ["bibliothèque", "réfrigérateur", "ascenseur", "architecture", "philosophie", "magnétisme", "encyclopédie", "géographie", "théâtre", "restaurant"]
hardcore_words = ["anticonstitutionnellement", "incompréhensibilité", "électroencéphalogramme", "otorhinolaryngologiste", "hexakosioihexekontahexaphobie", "dysprosium", "parallélépipède", "hippopotomonstrosesquippedaliophobie", "sphygmomanomètre", "xylophoniste"]

# Choix du niveau de difficulté
print("Choisissez un niveau de difficulté :")
print("1 - Facile")
print("2 - Moyen")
print("3 - Difficile")
print("4 - Hardcore")
choice = input("Entrez le numéro du niveau (1-4) : ")

# Sélection des mots en fonction du niveau
if choice == "1":
    words = easy_words
elif choice == "2":
    words = medium_words
elif choice == "3":
    words = hard_words
elif choice == "4":
    words = hardcore_words
else:
    print("Choix invalide. Mode Facile activé par défaut.")
    words = easy_words

score = 0
start_time = time.time()

for word in words:
    while True:
        user_input = input(f"Type '{word}': ")
        if user_input == word:
            score += 1
            break
        else:
            print("Perdu, réessayez.")
            score -= 1

end_time = time.time()
total_time = end_time - start_time

print(f"Vous avez tapé {len(words)} mots en {total_time:.2f}s avec un score de {score} points.")