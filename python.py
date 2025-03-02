import time

words = ["estérifia", "dégrafasses", "sourissiez", "écroueras", "exprès", "reportera", "déchargerais", "galipotas", "débarbouillages", "agitez"]

start_time = time.time()

for word in words:
    while True:
        user_input = input(f"Type '{word}': ")
        if user_input == word:
            break
        else:
            print("Perdu, réessayez.")

end_time = time.time()
total_time = end_time - start_time

print(f"Vous avez tapé {len(words)} mots en {total_time:.2f}s")