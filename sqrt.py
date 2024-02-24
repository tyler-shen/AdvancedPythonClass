def sqrt_binary_search(number, epsilon=1e-10):
    if number < 0:
        raise ValueError("Cannot calculate square root of a negative number.")

    if number == 0 or number == 1:
        return round(number, 2)

    low, high = 0, number
    while high - low > epsilon:
        mid = (low + high) / 2
        mid_squared = mid * mid

        if mid_squared < number:
            low = mid
        else:
            high = mid

    result = low + (high - low) / 2
    return round(result, 2)

# Example usage:
number_to_sqrt = 25
result = sqrt_binary_search(number_to_sqrt)
print(f"The square root of {number_to_sqrt} is approximately {result}")
