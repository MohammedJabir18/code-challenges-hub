if __name__ == '__main__':
    low1 = float('inf')
    low2 = float('inf')
    names1 = []
    names2 = []
    
    for _ in range(int(input())):
        name = input()
        score = float(input())
        
        if score < low1:
            low2, names2 = low1, names1
            low1, names1 = score, [name]
            
        elif score == low1:
            names1.append(name)
            
        elif score < low2:
            low2 = score
            names2 = [name]
            
        elif score == low2:
            names2.append(name)
            
    names2.sort()
    for name in names2:
        print(name)


# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna