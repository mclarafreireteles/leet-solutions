class Solution:
    def romanToInt(self, s: str) -> int:
        valores = {
        'I': 1, 'V': 5, 'X': 10, 'L': 50,
        'C': 100, 'D': 500, 'M': 1000
        }
    
        total = 0
        prev = 0 

        for char in reversed(s):  
            atual = valores[char]
            if atual < prev:  
                total -= atual
            else:  
                total += atual
            prev = atual  
        
        return total