if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())
    
    first = -float("inf")
    second = -float("inf")
    
    for i in arr:
        if first < i:
            second = first
            first = i
        
        elif second < i != first:
            second = i
            
    print(second)
            
            
                
            
        


# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna