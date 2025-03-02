import time
import os
import json  

# Listes de mots par niveau de difficulté
easy_words = ["chat", "chien", "maison", "arbre", "soleil", "fleur", "table", "chaise", "livre", "école"]
medium_words = ["ordinateur", "bouteille", "téléphone", "fenêtre", "montagne", "vélo", "cahier", "stylo", "lampe", "horloge"]
hard_words = ["bibliothèque", "réfrigérateur", "ascenseur", "architecture", "philosophie", "magnétisme", "encyclopédie", "géographie", "théâtre", "restaurant"]
hardcore_words = ["anticonstitutionnellement", "incompréhensibilité", "électroencéphalogramme", "otorhinolaryngologiste", "hexakosioihexekontahexaphobie", "dysprosium", "parallélépipède", "hippopotomonstrosesquippedaliophobie", "sphygmomanomètre", "xylophoniste"]

# Charger les données de la dernière session
def load_last_session():
    if os.path.exists("last_session.json"):
        try:
            with open("last_session.json", "r") as file:
                data = file.read()
                if data.strip():  # Vérifie si le fichier n'est pas vide
                    return json.loads(data)
        except json.JSONDecodeError:
            print("Erreur : Le fichier last_session.json est corrompu. Il sera réinitialisé.")
    return None

# Sauvegarder les données de la session actuelle
def save_last_session(score, total_time):
    with open("last_session.json", "w") as file:
        json.dump({"score": score, "total_time": total_time}, file)

# Choix du niveau de difficulté
print("Choisissez un niveau de difficulté :")
print("1 - Facile")
print("2 - Moyen")
print("3 - Difficile")
print("4 - Hardcore")
choice = input("Entrez le numéro du niveau (1-4) : ")

# sélection des mots 
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


# temps court = bonus élevé
time_bonus = max(0, 100 - int(total_time))  
total_score = score + time_bonus

# résultats
print(f"\nVous avez tapé {len(words)} mots en {total_time:.2f}s.")
print(f"Score de base : {score} points")
print(f"Bonus de rapidité : {time_bonus} points")
print(f"Score total : {total_score} points")

# comparaison
last_session = load_last_session()
if last_session:
    last_score = last_session["score"]
    last_time = last_session["total_time"]
    print("\nComparaison avec la dernière session :")
    if total_score > last_score:
        print(f"Vous avez amélioré votre score de {total_score - last_score} points !")
    elif total_score < last_score:
        print(f"Votre score est inférieur de {last_score - total_score} points par rapport à la dernière fois.")
    else:
        print("Votre score est identique à la dernière fois.")

    if total_time < last_time:
        print(f"Vous avez été plus rapide de {last_time - total_time:.2f}s !")
    elif total_time > last_time:
        print(f"Vous avez été plus lent de {total_time - last_time:.2f}s par rapport à la dernière fois.")
    else:
        print("Votre temps est identique à la dernière fois.")
else:
    print("\nAucune session précédente trouvée. C'est votre première fois !")

# sauvegarde 
save_last_session(total_score, total_time)