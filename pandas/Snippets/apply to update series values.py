def multiply_by_self_with_min(x, min_servings):
    if x < min_servings:
        return x**2
    return x


alcohol.apply(multiply_by_self_with_min, min_servings=200)

# alcohol.apply(multiply_by_self_with_min, args=(200,))