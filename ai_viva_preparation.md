# 🎓 AI Practical Exam — Viva Preparation Guide

---

## Assignment A1: DFS & BFS

**Problem:** Implement DFS and BFS on an undirected graph using recursion.

### How the Code Works

| Aspect | Details |
|---|---|
| **Data Structure** | `Graph` class with adjacency list (`dict` of lists) |
| **DFS** | Recursive; uses a `set` for visited nodes |
| **BFS** | Uses `deque` as a queue; implemented via a recursive helper (`bfs_helper`) |
| **Graph Type** | Undirected (each `add_edge(u,v)` adds both `u→v` and `v→u`) |

**DFS Flow:** Visit node → mark visited → recurse on unvisited neighbors.  
**BFS Flow:** Enqueue start → dequeue front → enqueue unvisited neighbors → repeat.

### Complexity

| Algorithm | Time | Space |
|---|---|---|
| DFS | O(V + E) | O(V) for visited + O(V) recursion stack |
| BFS | O(V + E) | O(V) for visited + queue |

### Viva Q&A

**Q: What is the difference between DFS and BFS?**  
A: DFS explores as deep as possible along a branch before backtracking (uses stack/recursion). BFS explores all neighbors at the current depth before moving deeper (uses queue).

**Q: Why use `deque` instead of a regular list for BFS?**  
A: `deque.popleft()` is **O(1)**, while `list.pop(0)` is **O(n)** since it shifts all elements.

**Q: What is the role of the `visited` set?**  
A: Prevents infinite loops by ensuring each node is processed only once — critical for graphs with cycles.

**Q: Is this BFS truly recursive?**  
A: It uses a recursive helper function `bfs_helper()`, but logically it still relies on a queue. It's a recursive *implementation* of BFS, not a fundamentally recursive algorithm like DFS.

**Q: Can DFS be used for shortest path in unweighted graphs?**  
A: No. BFS guarantees the shortest path in unweighted graphs; DFS does not.

**Q: What happens if the graph is disconnected?**  
A: Only the connected component containing the start node will be traversed. You'd need to loop through all nodes to cover disconnected components.

**Q: Applications of DFS vs BFS?**  
A: DFS → cycle detection, topological sort, maze solving. BFS → shortest path (unweighted), level-order traversal, peer-to-peer networks.

---

## Assignment A2: A* Algorithm (8-Puzzle)

**Problem:** Solve the 8-puzzle using the A* search algorithm.

### How the Code Works

| Aspect | Details |
|---|---|
| **Heuristic** | `h_misplaced_tiles` — counts tiles not in their goal position (excluding blank) |
| **f(n)** | `f = g + h` where `g` = moves so far, `h` = heuristic estimate |
| **Data Structure** | Min-heap (`heapq`) as priority queue |
| **State Representation** | 3×3 list; blank tile = `0` |
| **Visited** | `set` of tuples (immutable representation of states) |

**Flow:** Push initial state → pop state with lowest `f` → if goal, return path → else generate neighbors by moving blank tile (up/down/left/right) → push unvisited neighbors → repeat.

### Complexity

| Aspect | Value |
|---|---|
| Time | O(b^d) worst case, where b = branching factor, d = depth |
| Space | O(b^d) for the priority queue and visited set |
| 8-Puzzle States | 9! / 2 = 181,440 reachable states |

### Viva Q&A

**Q: What makes A* optimal?**  
A: A* is optimal when the heuristic is **admissible** (never overestimates the true cost). Misplaced tiles heuristic is admissible since each misplaced tile needs at least one move.

**Q: What is the difference between A* and Greedy Best-First Search?**  
A: Greedy uses only `h(n)` (heuristic), so it's fast but not optimal. A* uses `f(n) = g(n) + h(n)`, which guarantees optimality.

**Q: Why convert state to tuple for the visited set?**  
A: Lists are **unhashable** in Python and cannot be added to sets. Tuples are immutable and hashable.

**Q: What is an admissible heuristic?**  
A: A heuristic that **never overestimates** the actual cost to reach the goal. Examples for 8-puzzle: misplaced tiles, Manhattan distance.

**Q: Is Manhattan distance better than misplaced tiles?**  
A: Yes. Manhattan distance is more **informed** (closer to the true cost) while still being admissible, so A* explores fewer nodes.

**Q: Can all 8-puzzle initial states be solved?**  
A: No. Only half the permutations are solvable. You can check solvability by counting **inversions** — solvable if inversions are even.

**Q: What is the role of `heapq`?**  
A: It maintains a **min-heap** priority queue, so the state with the smallest `f` value is always popped first — essential for A*'s correctness.

---

## Assignment A3: Greedy Algorithm (Selection Sort & Job Scheduling)

**Problem:** Implement Greedy search for Selection Sort and Job Scheduling.

### Part I — Selection Sort

**Greedy Strategy:** At each step, find the **minimum** element from the unsorted portion and place it at the current position.

**Flow:** For each position `i`, scan `i+1` to `n-1` → find minimum → swap with position `i`.

| Aspect | Value |
|---|---|
| Time Complexity | O(n²) always (best, average, worst) |
| Space Complexity | O(1) — in-place |
| Stable? | **No** (swapping can change relative order of equal elements) |

### Part IV — Job Scheduling

**Greedy Strategy:** Sort jobs by **profit in descending order**, then assign each job to the **latest available slot** before its deadline.

**Flow:** Sort by profit → for each job, try to place it in the latest free slot ≤ deadline → if placed, add profit.

| Aspect | Value |
|---|---|
| Time Complexity | O(n log n) for sorting + O(n × d) for scheduling |
| Space Complexity | O(d) for slots array |

### Viva Q&A

**Q: Why is Selection Sort considered greedy?**  
A: It makes a **locally optimal choice** at each step (selecting the minimum) hoping to achieve a globally sorted array.

**Q: What is the Greedy approach?**  
A: An algorithmic paradigm that makes the locally optimal choice at each step, without reconsidering past decisions. It doesn't always guarantee a global optimum.

**Q: Why sort jobs by profit (not deadline)?**  
A: Maximizing profit requires prioritizing high-profit jobs. Sorting by deadline would not optimize total profit.

**Q: Why assign to the latest available slot?**  
A: To keep earlier slots free for jobs with tighter deadlines, maximizing the number of jobs that can be scheduled.

**Q: Greedy vs Dynamic Programming?**  
A: Greedy makes one irrevocable choice per step (faster, simpler). DP considers all sub-problems and stores results (slower, but always optimal for problems with overlapping subproblems).

**Q: Does Greedy always give the optimal solution?**  
A: No. It works for problems with the **greedy-choice property** and **optimal substructure** (e.g., job scheduling, Huffman coding), but fails for others (e.g., 0/1 knapsack).

---

## Assignment B4: N-Queens (Backtracking + Branch & Bound)

**Problem:** Solve the N-Queens problem using Branch and Bound with Backtracking.

### How the Code Works

| Aspect | Details |
|---|---|
| **Approach** | Place queens row by row; prune using column & diagonal constraints |
| **Constraint Arrays** | `cols[j]` — column `j` occupied; `rightDiagonal[i+j]` — right diagonal; `leftDiagonal[i-j+n-1]` — left diagonal |
| **Backtracking** | If a queen can't be placed in any column of row `i`, undo (pop) and try next column in previous row |

**Key Insight:** Two queens share a right diagonal if `row+col` is the same; they share a left diagonal if `row-col` is the same. The arrays use these as indices.

### Complexity

| Aspect | Value |
|---|---|
| Time | O(n!) worst case (pruned significantly by branch & bound) |
| Space | O(n) for arrays + O(n) recursion stack |

### Viva Q&A

**Q: What is Backtracking?**  
A: A systematic way to search through all possible solutions by building candidates incrementally and **abandoning** a candidate ("backtracking") as soon as it violates constraints.

**Q: What is Branch and Bound?**  
A: An optimization of backtracking where entire **branches** of the search tree are pruned using **bound functions** (here: the diagonal and column arrays).

**Q: How are diagonal conflicts detected?**  
A: For right diagonal: all cells with the same `i + j` value lie on the same diagonal. For left diagonal: all cells with the same `i - j` value lie on the same diagonal. The `+ n - 1` offset prevents negative indices.

**Q: Why does this code return only one solution?**  
A: It returns `True` as soon as the first valid placement is found. To find all solutions, you'd remove the early return and collect all valid boards.

**Q: What is a Constraint Satisfaction Problem (CSP)?**  
A: A problem defined by **variables** (queen positions), **domains** (possible columns), and **constraints** (no two queens attack each other).

**Q: For what value of N is there no solution?**  
A: N = 2 and N = 3 have no solutions. N = 1 and N ≥ 4 always have solutions.

---

## Assignment B5: Chatbot (Restaurant)

**Problem:** Develop an elementary chatbot for customer interaction.

### How the Code Works

| Aspect | Details |
|---|---|
| **Technique** | Keyword matching using `in` operator on lowercased user input |
| **Categories** | Menu, cost/price, contact, reservation, hours, date/time, greetings |
| **Exit** | User types "exit" or "quit" |
| **Library** | `datetime` for current date/time |

**Flow:** Take input → convert to lowercase → check for keywords using `if-elif` chain → print matching response → repeat until "exit"/"quit".

### Viva Q&A

**Q: What NLP technique is used here?**  
A: **Keyword-based pattern matching** — the simplest form of NLP. No actual NLP library is used.

**Q: Limitations of this approach?**  
A: Cannot handle synonyms, misspellings, context, or multi-turn conversations. Only responds to predefined keywords.

**Q: How could this chatbot be improved?**  
A: Use NLP libraries (NLTK, spaCy), regular expressions for flexible matching, machine learning models (intent classification), or APIs like Dialogflow/Rasa.

**Q: What is the role of `.lower()`?**  
A: Makes matching case-insensitive so "MENU", "Menu", and "menu" all trigger the same response.

**Q: What are the types of chatbots?**  
A: **Rule-based** (like this one — predefined rules), **Retrieval-based** (selects best response from a database), **Generative** (uses ML/DL to generate responses, e.g., GPT).

**Q: What is the Turing Test and does this chatbot pass it?**  
A: The Turing Test checks if a machine can exhibit intelligent behavior indistinguishable from a human. This chatbot would **not** pass it due to its rigid keyword matching.

---

## Assignment C6: Expert System (Medical Diagnosis)

**Problem:** Implement an Expert System for hospitals/medical facilities.

### How the Code Works

| Aspect | Details |
|---|---|
| **Knowledge Base** | Dictionary mapping symptoms → diseases |
| **Inference Engine** | Simple forward chaining — matches user-reported symptoms against the knowledge base |
| **User Interface** | Yes/No questions for each symptom |

**Components of the Expert System:**
1. **Knowledge Base** (`knowledge()`) — stores symptom-disease rules
2. **Question List** (`questions_List()`) — maps symptoms to human-readable questions
3. **Inference Engine** (`doctor()`) — collects symptoms, matches against KB, outputs diagnosis
4. **User Interface** (`ask()`) — handles Yes/No input validation

### Viva Q&A

**Q: What is an Expert System?**  
A: A computer program that emulates the decision-making ability of a human expert using **knowledge base** (facts/rules) and an **inference engine** (reasoning mechanism).

**Q: What are the components of an Expert System?**  
A: (1) Knowledge Base, (2) Inference Engine, (3) User Interface, (4) Explanation Facility (optional), (5) Knowledge Acquisition Module (optional).

**Q: What type of inference is used here?**  
A: **Forward Chaining** — starts from known facts (symptoms) and derives conclusions (diagnosis). The opposite is **Backward Chaining** — starts from a hypothesis and checks if facts support it.

**Q: Forward Chaining vs Backward Chaining?**  
A: Forward = data-driven (from facts to conclusion). Backward = goal-driven (from hypothesis to facts). This code uses forward chaining.

**Q: Limitations of this expert system?**  
A: Fixed knowledge base, no learning capability, no confidence scores/probabilities, cannot handle unknown symptoms, and no explanation of reasoning.

**Q: How could it be improved?**  
A: Add probability/certainty factors, use fuzzy logic, implement backward chaining, add more diseases and symptoms, integrate with ML for learning from data.

**Q: What is the difference between an Expert System and a Neural Network?**  
A: Expert Systems use explicit rules created by human experts (transparent, explainable). Neural Networks learn patterns from data (can handle complex inputs but are less explainable — "black box").

---

## 📋 Quick Reference: Algorithm Comparison

| Assignment | Algorithm | Paradigm | Time Complexity | Key Data Structure |
|---|---|---|---|---|
| A1 | DFS | Uninformed Search | O(V+E) | Stack (recursion) |
| A1 | BFS | Uninformed Search | O(V+E) | Queue (deque) |
| A2 | A* | Informed Search | O(b^d) | Min-Heap (heapq) |
| A3 | Selection Sort | Greedy | O(n²) | Array |
| A3 | Job Scheduling | Greedy | O(n log n) | Array + Sorting |
| B4 | N-Queens | Backtracking + B&B | O(n!) | Arrays (constraints) |
| B5 | Chatbot | Rule-based AI | O(k) per query | Dictionary |
| C6 | Expert System | Knowledge-based AI | O(n) per diagnosis | Dictionary |

---

## 🔑 General AI Concepts (Commonly Asked)

**Q: Informed vs Uninformed Search?**  
A: Informed uses heuristics (A*, Greedy BFS). Uninformed has no domain knowledge (DFS, BFS).

**Q: What is a heuristic?**  
A: An estimate of the cost from current state to the goal. Must be admissible (never overestimate) for A* optimality.

**Q: What is NP-Complete?**  
A: Problems where no known polynomial-time algorithm exists (e.g., N-Queens is NP-hard for finding all solutions).

**Q: What is the difference between AI, ML, and DL?**  
A: AI is the broadest concept (machines mimicking intelligence). ML is a subset (learning from data). DL is a subset of ML (using neural networks with many layers).

> [!TIP]
> **During the viva:** Always explain the *why* behind your code choices, not just the *what*. Examiners value understanding over memorization.
