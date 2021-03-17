def twoStacks(x, a, b):
    a.reverse()
    b.reverse()
    stack = []
    total, score = 0, 0

    while a:
        item = a.pop()
        if (total + item) <= x:
            total += item
            score += 1
            stack.append(item)
        else: break
    
    maxScore = score

    while b:
        item = b.pop()
        total += item
        score += 1
        while total > x and stack:
            total -= stack.pop()
            score -= 1
        if total <= x and score > maxScore: maxScore = score
    
    return maxScore
        
