"""
Problem: D - https://www3.facens.br/maratona/arquivos/Maratona2023.pdf 
Platform: Maratona de Programação FACENS 2023
Date: 2025-05-30
Complexity: o(N)
"""

import sys

input = sys.stdin.readline

INF = 10**9 + 7  # Um número bem grande

def main():
    T = int(input())
    for test in range(T):
        N = int(input())
        best_10 = INF
        best_01 = INF
        best_11 = INF
        
        for _ in range(N):
            m, s = input().split()
            m = int(m)
            if s == "11":
                best_11 = min(best_11, m)
            elif s == "10":
                best_10 = min(best_10, m)
            elif s == "01":
                best_01 = min(best_01, m)
        
        ans = min(best_11, best_10 + best_01)
        
        if ans >= INF:
            print(-1)
        else:
            print(ans)

if __name__ == "__main__":
    main()

