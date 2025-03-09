import time
import os
import json
import random
from colorama import init, Fore


init(autoreset=True)

# J'ai préféré utiliser des mots ajoutés manuellement plutôt que le dictionnaire sur Linux, car je pouvais plus facilement les modifier pour les niveaux. De plus, je suis sous Windows, donc c'était plus simple pour moi.
easy_groups = [
    ["chat", "chien", "maison", "arbre", "soleil", "fleur", "table", "chaise", "livre", "école"],
    ["pomme", "banane", "orange", "fraise", "citron", "kiwi", "ananas", "raisin", "melon", "cerise"],
    ["voiture", "vélo", "train", "avion", "bateau", "bus", "moto", "camion", "tramway", "scooter"]
]

medium_groups = [
    ["ordinateur", "bouteille", "téléphone", "fenêtre", "montagne", "vélo", "cahier", "stylo", "lampe", "horloge"],
    ["restaurant", "cinéma", "théâtre", "musée", "bibliothèque", "école", "hôpital", "supermarché", "pharmacie", "banque"],
    ["jardin", "forêt", "plage", "rivière", "océan", "désert", "montagne", "vallée", "campagne", "ville"]
]

hard_groups = [
    ["bibliothèque", "réfrigérateur", "ascenseur", "architecture", "philosophie", "magnétisme", "encyclopédie", "géographie", "théâtre", "restaurant"],
    ["électricité", "télécommunication", "informatique", "astronomie", "biologie", "chimie", "physique", "mathématiques", "géologie", "météorologie"],
    ["philosophie", "psychologie", "sociologie", "anthropologie", "économie", "politique", "histoire", "géographie", "littérature", "linguistique"]
]

hardcore_groups = [
    ["anticonstitutionnellement", "incompréhensibilité", "électroencéphalogramme", "otorhinolaryngologiste", "hexakosioihexekontahexaphobie", "dysprosium", "parallélépipède", "hippopotomonstrosesquippedaliophobie", "sphygmomanomètre", "xylophoniste"],
    ["intergouvernementalisation", "désinstitutionnalisation", "contre-révolutionnaire", "hyperconscientisation", "microprogrammabilité", "macroéconométrie", "télétransmission", "cryoconservation", "neuropharmacologie", "radiogoniométrie"],
    ["spectrophotométrie", "thermodynamique", "cryptographie", "paléontologie", "astrophysique", "biotechnologie", "nanotechnologie", "cristallographie", "épidémiologie", "sismologie"]
]


def load_last_session():
    if os.path.exists("last_session.json"):
        try:
            with open("last_session.json", "r") as file:
                data = file.read()
                if data.strip(): 
                    return json.loads(data)
        except json.JSONDecodeError:
            print(Fore.RED + "Erreur : Le fichier last_session.json est corrompu. Il sera réinitialisé.")
    return None


def load_personal_best():
    if os.path.exists("personal_best.json"):
        try:
            with open("personal_best.json", "r") as file:
                data = file.read()
                if data.strip():
                    return json.loads(data)
        except json.JSONDecodeError:
            print(Fore.RED + "Erreur : Le fichier personal_best.json est corrompu. Il sera réinitialisé.")
    return {"score": 0, "total_time": float('inf')} 


def save_last_session(score, total_time):
    with open("last_session.json", "w") as file:
        json.dump({"score": score, "total_time": total_time}, file)


def save_personal_best(score, total_time):
    with open("personal_best.json", "w") as file:
        json.dump({"score": score, "total_time": total_time}, file)


print(Fore.CYAN + "🌟 Choisissez un niveau de difficulté :")
print(Fore.GREEN + "1 - Facile 🌱")
print(Fore.YELLOW + "2 - Moyen 🚀")
print(Fore.RED + "3 - Difficile 🔥")
print(Fore.MAGENTA + "4 - Hardcore 💀")
choice = input(Fore.CYAN + "Entrez le numéro du niveau (1-4) : ")


if choice == "1":
    words = random.choice(easy_groups)  
    print(Fore.GREEN + "Mode Facile activé ! 🌱")
elif choice == "2":
    words = random.choice(medium_groups)
    print(Fore.YELLOW + "Mode Moyen activé ! 🚀")
elif choice == "3":
    words = random.choice(hard_groups)
    print(Fore.RED + "Mode Difficile activé ! 🔥")
elif choice == "4":
    words = random.choice(hardcore_groups)
    print(Fore.MAGENTA + "Mode Hardcore activé ! 💀")
else:
    print(Fore.RED + "Choix invalide. Mode Facile activé par défaut. 🌱")
    words = random.choice(easy_groups)


random.shuffle(words)

score = 0
start_time = time.time()

for word in words:
    while True:
        user_input = input(Fore.BLUE + f"✍️  Écris '{word}': ")
        if user_input == word:
            print(Fore.GREEN + "✅ Correct !")
            score += 1
            break
        else:
            print(Fore.RED + "❌ Perdu, réessayez.")
            score -= 1

end_time = time.time()
total_time = end_time - start_time


time_bonus = max(0, 100 - int(total_time))  
total_score = score + time_bonus


print(Fore.CYAN + "\n🎉 Résultats :")
print(Fore.YELLOW + f"Vous avez tapé {len(words)} mots en {total_time:.2f}s.")
print(Fore.GREEN + f"Score de base : {score} points")
print(Fore.BLUE + f"Bonus de rapidité : {time_bonus} points")
print(Fore.MAGENTA + f"Score total : {total_score} points")


last_session = load_last_session()
if last_session:
    last_score = last_session["score"]
    last_time = last_session["total_time"]
    print(Fore.CYAN + "\n🔍 Comparaison avec la dernière session :")
    if total_score > last_score:
        print(Fore.GREEN + f"🎉 Vous avez amélioré votre score de {total_score - last_score} points !")
    elif total_score < last_score:
        print(Fore.RED + f"😢 Votre score est inférieur de {last_score - total_score} points par rapport à la dernière fois.")
    else:
        print(Fore.YELLOW + "🤔 Votre score est identique à la dernière fois.")

    if total_time < last_time:
        print(Fore.GREEN + f"⚡ Vous avez été plus rapide de {last_time - total_time:.2f}s !")
    elif total_time > last_time:
        print(Fore.RED + f"🐢 Vous avez été plus lent de {total_time - last_time:.2f}s par rapport à la dernière fois.")
    else:
        print(Fore.YELLOW + "⏱️ Votre temps est identique à la dernière fois.")
else:
    print(Fore.CYAN + "\n🌟 Aucune session précédente trouvée. C'est votre première fois !")


personal_best = load_personal_best()
print(Fore.CYAN + "\n🏆 Meilleur score personnel :")
print(Fore.YELLOW + f"Score : {personal_best['score']} points")
print(Fore.YELLOW + f"Temps : {personal_best['total_time']:.2f}s")


if total_score > personal_best["score"] or (total_score == personal_best["score"] and total_time < personal_best["total_time"]):
    print(Fore.GREEN + "🎉 Nouveau record personnel ! 🎉")
    save_personal_best(total_score, total_time)
else:
    print(Fore.YELLOW + "Vous n'avez pas battu votre record personnel.")


save_last_session(total_score, total_time)