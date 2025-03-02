import time

words = ["estérifia", "dégrafasses", "sourissiez", "écroueras", "exprès", "reportera", "déchargerais", "galipotas", "débarbouillages", "agitez"]
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