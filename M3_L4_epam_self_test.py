# Loops
import time

def find_nth_prime(n):
    conditional = 0
    a = 1
    prev = []
    while conditional < n:
        a += 1
        prev.append(a)
        for num in prev:
            if a == num:
                conditional += 1
            else:
                if a % num == 0:
                    break
    return a

def find_nth_prime_refined(n):
    a = 1
    num_primes_found = 0
    prev_primes = []
    while num_primes_found < n:
        a += 1
        is_prime = True
        for prime in prev_primes:
            if a % prime == 0:
                is_prime = False
                break

        if is_prime:
            prev_primes.append(a)
            num_primes_found += 1
    return a

# --- Efficiency check script ---
n_value = 6767

# Time the original function
start_time_orig = time.perf_counter()
result_orig = find_nth_prime(n_value)
end_time_orig = time.perf_counter()
duration_orig = end_time_orig - start_time_orig

print(f"Original function result: {result_orig} in {duration_orig:.4f} seconds.")

# Time the refined function
start_time_refined = time.perf_counter()
result_refined = find_nth_prime_refined(n_value)
end_time_refined = time.perf_counter()
duration_refined = end_time_refined - start_time_refined

print(f"Refined function result: {result_refined} in {duration_refined:.4f} seconds.")

