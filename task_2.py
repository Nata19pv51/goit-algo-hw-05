def binary_search(arr, x):
    low = 0
    high = len(arr) - 1
    iterations = 0
    boundary_high_value = None

    while low <= high:
        iterations += 1
        mid = (high + low) // 2
 
        # якщо x дорівнює значенню посередині списку, ігноруємо праву половину
        if arr[mid] == x:
            boundary_high_value = arr[mid]
            high = mid - 1
 
        # якщо x більше за значення посередині списку, ігноруємо ліву половину
        elif arr[mid] > x:
            boundary_high_value = arr[mid]
            high = mid - 1
            
        # інакше x менший за значення посередини списку, ігноруємо праву половину
        else:
            low = mid + 1
 
    return (iterations, boundary_high_value)

arr = [2.5, 3.1, 4.0, 4.0, 5.2, 6.7, 7.0]
x = 8.0

iterartions, value = binary_search(arr, x)
print(
    f"Iterations: {iterartions}\nUpper boundary: {value}")

