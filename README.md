The N-Queens problem:  
> " place N queens on an N×N chessboard so that no two queens attack each other"

That means:
- Only one queen per **row**
- Only one queen per **column**
- No queens on the **same diagonal**

How the Algorithm Works

Instead of brute force or backtracking, this project uses a **Genetic Algorithm**:
- Each board is a list of integers (queen positions)
- We start with a **random population** of boards
- Over generations, we:
  - **Select** the best boards
  - **Crossover** parts of them
  - **Mutate** some positions
- Eventually, the algorithm finds a **conflict-free solution**

  simple output :
  ![image](https://github.com/user-attachments/assets/8de62beb-dfbf-4e5f-b7d8-1af91abbf22f)
