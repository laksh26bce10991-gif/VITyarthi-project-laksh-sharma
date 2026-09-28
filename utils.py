def generate_fibonacci(n_terms: int) -> list:
    """Generates Fibonacci Sequence up to n_terms (Unit 3)[cite: 1]."""
    if n_terms <= 0:
        return []
    elif n_terms == 1:
        return [0]
    seq = [0, 1]
    while len(seq) < n_terms:
        seq.append(seq[-1] + seq[-2])
    return seq

def reverse_array(arr: list) -> list:
    """Array Order Reversal Algorithm without built-in functions (Unit 5)[cite: 1]."""
    reversed_arr = []
    for i in range(len(arr) - 1, -1, -1):
        reversed_arr.append(arr[i])
    return reversed_arr

def find_maximum(numbers: list):
    """Finds maximum value in a list using iterative comparison (Unit 5)[cite: 1]."""
    if not numbers:
        return None
    max_val = numbers[0]
    for num in numbers:
        if num > max_val:
            max_val = num
    return max_val