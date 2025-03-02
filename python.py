import time

# je suis sur windows donc je vais pour l'instant tester de cette manière sans utiliser de dictionnaire de mots français 
words = ["estérifia", "dégrafasses", "sourissiez", "écroueras", "exprès", "reportera", "déchargerais", "galipotas", "débarbouillages", "agitez"]

start_time = time.time()

for word in words:
    input(f"Type '{word}': ")

end_time = time.time()
total_time = end_time - start_time

print(f"Vous avez tapez {len(words)} mots en {total_time:.2f}s")