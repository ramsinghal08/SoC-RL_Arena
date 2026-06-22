import numpy as np

def capture_area(board, num, r, c):
    seen = np.zeros((r, c), dtype=bool)
    check = []
    
    for i in range(r):
        if board[i, 0] != num and board[i, 0] != -num: 
            check.append((i, 0))
        if board[i, c-1] != num and board[i, c-1] != -num: 
            check.append((i, c-1))
            
    for j in range(c):
        if board[0, j] != num and board[0, j] != -num: 
            check.append((0, j))
        if board[r-1, j] != num and board[r-1, j] != -num: 
            check.append((r-1, j))
            
    while len(check) > 0:
        curr_r, curr_c = check.pop()
        if not seen[curr_r, curr_c]:
            seen[curr_r, curr_c] = True
            
            for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                nr = curr_r + dr
                nc = curr_c + dc
                if 0 <= nr < r and 0 <= nc < c:
                    if not seen[nr, nc] and board[nr, nc] != num and board[nr, nc] != -num:
                        check.append((nr, nc))
                        
    for i in range(r):
        for j in range(c):
            if not seen[i, j]:
                board[i, j] = num