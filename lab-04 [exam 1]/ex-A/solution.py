import random

def simulate():
    flips = []
    consecutive = 1

    last = 'H' if random.randint(0,1) == 0 else 'T'
    flips.append(last)

    while consecutive < 3:
        current = 'H' if random.randint(0,1) == 0 else 'T'
        flips.append(current)

        if current == last:
            consecutive += 1
        else:
            consecutive = 1

        last = current

    return flips

total_flips = 0
simulations = 10

for _ in range(simulations):
	result = simulate()
	total_flips += len(result)

	print(' '.join(result), f"({len(result)} flips)")

print(f"On average, {total_flips / simulations:.1f} flips were needed.")