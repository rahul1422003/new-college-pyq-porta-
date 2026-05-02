from docx import Document
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.enum.table import WD_TABLE_ALIGNMENT, WD_CELL_VERTICAL_ALIGNMENT
from docx.oxml import OxmlElement
from docx.oxml.ns import qn
from docx.shared import Cm, Pt, RGBColor


OUT = "Algorithm_Design_Analysis_35_Page_Notes_Rahul_Yadav.docx"


def shade(cell, fill):
    tc_pr = cell._tc.get_or_add_tcPr()
    shd = OxmlElement("w:shd")
    shd.set(qn("w:fill"), fill)
    tc_pr.append(shd)


def set_cell_text(cell, text, bold=False):
    cell.text = ""
    p = cell.paragraphs[0]
    p.paragraph_format.space_after = Pt(0)
    r = p.add_run(text)
    r.bold = bold
    r.font.size = Pt(8.5)
    r.font.name = "Arial"
    cell.vertical_alignment = WD_CELL_VERTICAL_ALIGNMENT.CENTER


def add_table(doc, headers, rows):
    table = doc.add_table(rows=1, cols=len(headers))
    table.alignment = WD_TABLE_ALIGNMENT.CENTER
    table.style = "Table Grid"
    for i, h in enumerate(headers):
        set_cell_text(table.rows[0].cells[i], h, True)
        shade(table.rows[0].cells[i], "DCEAF7")
    for row in rows:
        cells = table.add_row().cells
        for i, value in enumerate(row):
            set_cell_text(cells[i], value)
    return table


def add_heading(doc, text, level=1):
    p = doc.add_paragraph()
    p.paragraph_format.space_before = Pt(1)
    p.paragraph_format.space_after = Pt(3)
    r = p.add_run(text)
    r.bold = True
    r.font.name = "Arial"
    r.font.size = Pt(14 if level == 1 else 11)
    r.font.color.rgb = RGBColor(31, 78, 121 if level == 1 else 100)
    return p


def add_para(doc, text, style=None):
    p = doc.add_paragraph(style=style)
    p.paragraph_format.space_after = Pt(2)
    p.paragraph_format.line_spacing = 1.03
    r = p.add_run(text)
    r.font.name = "Arial"
    r.font.size = Pt(8.6)
    return p


def add_bullets(doc, items):
    for item in items:
        p = doc.add_paragraph(style="List Bullet")
        p.paragraph_format.space_after = Pt(1)
        p.paragraph_format.line_spacing = 1.0
        r = p.add_run(item)
        r.font.name = "Arial"
        r.font.size = Pt(8.5)


def add_code(doc, lines):
    for line in lines:
        p = doc.add_paragraph()
        p.paragraph_format.left_indent = Cm(0.45)
        p.paragraph_format.space_after = Pt(0)
        r = p.add_run(line)
        r.font.name = "Courier New"
        r.font.size = Pt(7.8)
        r.font.color.rgb = RGBColor(55, 55, 55)


def exam_questions(title):
    clean = title.split(":", 1)[-1].strip()
    return [
        f"Define/explain {clean} with a neat example.",
        f"Write algorithm steps or key method for {clean}, then mention time and space complexity.",
        f"State two advantages, two limitations and one exam application of {clean}.",
    ]


def unit_page(title, objectives, theory, bullets=None, table=None, code=None, remember=None):
    return {
        "title": title,
        "objectives": objectives,
        "theory": theory,
        "bullets": bullets or [],
        "table": table,
        "code": code or [],
        "remember": remember or [],
    }


pages = [
    unit_page(
        "Unit I: Algorithm and Complexity Basics",
        "Understand what an algorithm is and how efficiency is measured.",
        "These 35-page exam notes are based on the uploaded syllabus of Design and Analysis of Algorithms. An algorithm is a finite, ordered sequence of unambiguous steps that converts input into output and terminates after finite time. A good algorithm is correct, efficient, simple to implement, and scalable. Analysis of algorithm means estimating resources before actual execution. Main resources are time and memory. We usually analyze in terms of input size n, because exact machine time depends on hardware, compiler and programming language.",
        [
            "Course Outcomes: complexity evaluation, Prim MST, 8-queen backtracking, TSP branch and bound, 0/1 knapsack DP.",
            "Every algorithm answer should include: idea, steps/pseudocode, example/use, time complexity, space complexity, limitations.",
            "Characteristics: input, output, definiteness, finiteness, effectiveness, correctness.",
            "Time complexity counts elementary operations as a function of n.",
            "Space complexity counts total memory used: input space + auxiliary space.",
            "Worst case is used most often because it gives an upper guarantee.",
            "Average case needs probability distribution of inputs; best case is usually optimistic.",
        ],
        table=(["Case", "Meaning", "Example"], [
            ["Best", "Minimum operations", "Linear search finds key at first position"],
            ["Average", "Expected operations", "Key is equally likely at any position"],
            ["Worst", "Maximum operations", "Linear search key absent or last position"],
        ]),
        remember=["Efficiency is compared by growth rate, not by exact seconds.", "For large n, n log n is much better than n^2."],
    ),
    unit_page(
        "Unit I: Time and Space Complexity",
        "Evaluate time-space requirements and understand trade-off.",
        "Time complexity is commonly written using asymptotic notation. Space complexity includes fixed part such as program variables and variable part such as recursion stack, arrays, tables and dynamic structures. Time-space tradeoff means reducing time by using extra memory or reducing memory by accepting extra computation. Dynamic programming uses this tradeoff: it stores subproblem answers to avoid recomputation.",
        [
            "Example: Binary search time O(log n), space O(1) iterative, O(log n) recursive due to stack.",
            "Merge sort time O(n log n), extra space O(n) for merging.",
            "Quick sort average O(n log n), worst O(n^2), stack O(log n) average.",
            "Hashing gives average O(1) search using extra table memory.",
            "Precomputation stores answers in advance to save query time.",
        ],
        table=(["Complexity", "Growth", "Typical Algorithm"], [
            ["O(1)", "constant", "array access"],
            ["O(log n)", "slow", "binary search"],
            ["O(n)", "linear", "linear scan"],
            ["O(n log n)", "near linear", "merge sort, heap sort"],
            ["O(n^2)", "quadratic", "simple nested loops"],
            ["O(2^n)", "exponential", "subset generation"],
        ]),
    ),
    unit_page(
        "Unit I: Asymptotic Notations",
        "Write upper, lower and tight bounds correctly.",
        "Asymptotic notation describes algorithm growth for large input size. It ignores constants and lower-order terms. Big-O gives upper bound, Omega gives lower bound, and Theta gives tight bound. These notations help compare algorithms independently of hardware. Example: 3n^2 + 5n + 10 is Theta(n^2), because n^2 dominates for large n.",
        [
            "Big-O: f(n) = O(g(n)) if f grows no faster than c.g(n) after n0.",
            "Omega: f(n) = Omega(g(n)) if f grows at least c.g(n) after n0.",
            "Theta: f(n) = Theta(g(n)) if both upper and lower bounds match.",
            "Little-o means strictly smaller growth; little-omega means strictly larger growth.",
            "Drop constants: O(2n) = O(n); drop lower terms: O(n^2+n) = O(n^2).",
        ],
        table=(["Expression", "Simplified Bound", "Reason"], [
            ["5n + 20", "Theta(n)", "linear term dominates constant"],
            ["2n^2 + n log n", "Theta(n^2)", "n^2 dominates n log n"],
            ["log n + 100", "Theta(log n)", "constant ignored for large n"],
            ["n(n-1)/2", "Theta(n^2)", "quadratic pair count"],
        ]),
    ),
    unit_page(
        "Unit I: Recurrences and Solving Techniques",
        "Analyze recursive algorithms using recurrence relations.",
        "A recurrence expresses running time of a recursive algorithm in terms of smaller input sizes. Divide-and-conquer algorithms naturally form recurrences. Three common solving methods are substitution, recursion tree, and Master Theorem. In exams, identify a, b and f(n) in T(n)=aT(n/b)+f(n).",
        [
            "Substitution method: guess answer and prove by induction.",
            "Recursion tree: expand levels, calculate work per level and sum all levels.",
            "Master theorem: directly solves many divide and conquer recurrences.",
            "Merge sort: T(n)=2T(n/2)+n = Theta(n log n).",
            "Binary search: T(n)=T(n/2)+1 = Theta(log n).",
        ],
        table=(["Form", "Condition", "Answer"], [
            ["T(n)=aT(n/b)+f(n)", "f(n) smaller than n^log_b a", "Theta(n^log_b a)"],
            ["T(n)=aT(n/b)+f(n)", "f(n) equal to n^log_b a", "Theta(n^log_b a log n)"],
            ["T(n)=aT(n/b)+f(n)", "f(n) larger and regular", "Theta(f(n))"],
        ]),
        remember=["Always mention base case T(1)=Theta(1).", "Master theorem is not suitable for all irregular recurrences."],
    ),
    unit_page(
        "Unit I: Divide and Conquer Technique",
        "Use divide, conquer and combine pattern.",
        "Divide and conquer solves a large problem by dividing it into smaller independent subproblems, solving them recursively, and combining their results. It works best when subproblems are similar in form and balanced in size. The method improves performance by reducing repeated comparisons or by exploiting sorted/structured data.",
        [
            "Divide: split input into two or more parts.",
            "Conquer: solve each part recursively or directly if small.",
            "Combine: merge partial solutions into final answer.",
            "Examples: binary search, merge sort, quick sort, heap sort conceptually, Strassen multiplication.",
            "Advantages: simple analysis, parallelism possible, often efficient.",
            "Disadvantages: recursion overhead, extra space, poor performance if split is unbalanced.",
        ],
        table=(["Algorithm", "Divide", "Combine", "Time"], [
            ["Binary Search", "one half selected", "none", "O(log n)"],
            ["Merge Sort", "two halves", "merge sorted halves", "O(n log n)"],
            ["Quick Sort", "pivot partitions", "none heavy", "avg O(n log n)"],
            ["Strassen", "matrix subblocks", "matrix additions", "O(n^2.807)"],
        ]),
    ),
    unit_page(
        "Unit I: Binary Search",
        "Apply iterative and recursive binary search.",
        "Binary search finds an element in a sorted array by repeatedly comparing with the middle element and discarding half of the search space. It is a classic divide-and-conquer algorithm. The array must be sorted. If data is unsorted, sorting cost must also be considered.",
        [
            "Input: sorted array A[0..n-1], key x.",
            "If x == A[mid], answer found.",
            "If x < A[mid], search left half; otherwise search right half.",
            "Iterative version uses constant extra space.",
            "Recursive version is shorter but uses recursion stack.",
        ],
        code=[
            "low = 0, high = n-1",
            "while low <= high:",
            "    mid = (low + high) // 2",
            "    if A[mid] == x: return mid",
            "    elif x < A[mid]: high = mid - 1",
            "    else: low = mid + 1",
            "return -1",
        ],
        table=(["Measure", "Value"], [["Best", "O(1)"], ["Worst", "O(log n)"], ["Space iterative", "O(1)"], ["Space recursive", "O(log n)"]]),
    ),
    unit_page(
        "Unit I: Merge Sort",
        "Evaluate merge sort algorithm and complexity.",
        "Merge sort divides the array into two halves, recursively sorts both halves, and merges the sorted halves. It is stable and guarantees O(n log n) time in best, average and worst cases. Its main limitation is extra O(n) auxiliary memory.",
        [
            "Divide array until each subarray has one element.",
            "Merge two sorted arrays using two pointers.",
            "Stable: equal elements maintain original relative order.",
            "Useful for linked lists and external sorting.",
            "Recurrence: T(n)=2T(n/2)+Theta(n).",
        ],
        code=[
            "mergeSort(A, l, r):",
            "    if l < r:",
            "        m = (l+r)//2",
            "        mergeSort(A, l, m)",
            "        mergeSort(A, m+1, r)",
            "        merge(A, l, m, r)",
        ],
        table=(["Property", "Merge Sort"], [["Best/Average/Worst", "O(n log n)"], ["Extra Space", "O(n)"], ["Stable", "Yes"], ["In-place", "No"]]),
        remember=["For CO1, write recurrence and Master theorem result clearly."],
    ),
    unit_page(
        "Unit I: Quick Sort",
        "Understand partitioning and average-case efficiency.",
        "Quick sort chooses a pivot, partitions elements smaller than pivot to one side and larger elements to the other, then recursively sorts partitions. It is very fast in practice due to good cache behavior and in-place partitioning. Worst case occurs when pivot repeatedly gives highly unbalanced partitions, such as already sorted input with poor pivot choice.",
        [
            "Partition is the key operation.",
            "Average recurrence: T(n)=2T(n/2)+Theta(n).",
            "Worst recurrence: T(n)=T(n-1)+Theta(n).",
            "Randomized pivot reduces chance of worst case.",
            "Not stable by default.",
        ],
        code=[
            "quickSort(A, low, high):",
            "    if low < high:",
            "        p = partition(A, low, high)",
            "        quickSort(A, low, p-1)",
            "        quickSort(A, p+1, high)",
        ],
        table=(["Case", "Time"], [["Best", "O(n log n)"], ["Average", "O(n log n)"], ["Worst", "O(n^2)"], ["Auxiliary Space", "O(log n) average stack"]]),
    ),
    unit_page(
        "Unit I: Heap Sort",
        "Use heap structure for in-place sorting.",
        "Heap sort uses a binary heap, usually max-heap, to repeatedly place the largest element at the end of the array. A heap is a complete binary tree represented as an array where parent value is greater than or equal to its children for max-heap. Heap sort gives guaranteed O(n log n) time and O(1) extra space, but it is not stable.",
        [
            "Build max heap from array in O(n).",
            "Swap root with last element.",
            "Reduce heap size and heapify root.",
            "Repeat until heap size becomes 1.",
            "Parent index: (i-1)//2; children: 2i+1 and 2i+2.",
        ],
        code=[
            "heapSort(A):",
            "    buildMaxHeap(A)",
            "    for i = n-1 downto 1:",
            "        swap A[0], A[i]",
            "        heapSize = heapSize - 1",
            "        maxHeapify(A, 0)",
        ],
        table=(["Feature", "Value"], [["Time", "O(n log n)"], ["Build heap", "O(n)"], ["Extra Space", "O(1)"], ["Stable", "No"]]),
    ),
    unit_page(
        "Unit I: Strassen Matrix Multiplication",
        "Know divide-and-conquer improvement over classical multiplication.",
        "Classical matrix multiplication for two n x n matrices takes O(n^3) time. Strassen's algorithm reduces multiplications from 8 to 7 for each block division, increasing additions but reducing asymptotic time. Matrices are split into four submatrices. The seven products P1 to P7 are combined to obtain the result blocks.",
        [
            "Classical divide-and-conquer: 8 recursive multiplications of size n/2.",
            "Strassen: 7 recursive multiplications plus additions/subtractions.",
            "Recurrence: T(n)=7T(n/2)+Theta(n^2).",
            "Time: O(n^log2 7) approximately O(n^2.807).",
            "Practical only for large matrices due to overhead and numerical issues.",
        ],
        table=(["Method", "Recursive Multiplications", "Time"], [["Classical", "8", "O(n^3)"], ["Strassen", "7", "O(n^2.807)"]]),
        remember=["Exam point: fewer multiplications are more valuable than extra additions for large n."],
    ),
    unit_page(
        "Unit I: Code Tuning Techniques",
        "Improve program performance without changing algorithmic result.",
        "Code tuning means small implementation-level changes that reduce execution time or memory overhead. It should be done after choosing a good algorithm, not as a replacement for algorithm design. Measure before and after tuning because premature optimization can make code complex without real benefit.",
        [
            "Loop optimization: move invariant calculations outside loop, reduce nested loops, unroll small loops when useful.",
            "Data transfer optimization: avoid unnecessary copying, pass large objects by reference, use cache-friendly arrays.",
            "Logic optimization: simplify conditions, short-circuit frequent cases first, avoid repeated function calls.",
            "Use appropriate data structures: hash table, heap, balanced tree, adjacency list.",
            "Avoid recomputation using memoization or precomputed tables.",
        ],
        table=(["Technique", "Example"], [
            ["Loop invariant movement", "compute len once before loop"],
            ["Strength reduction", "replace expensive operation with cheaper equivalent"],
            ["Cache locality", "access arrays sequentially"],
            ["Early exit", "break when answer found"],
        ]),
    ),
    unit_page(
        "Unit II: Greedy Strategy",
        "Understand greedy choice and optimal substructure.",
        "A greedy algorithm builds the solution step by step by making the locally best choice at each stage. It never revisits previous choices. Greedy works only when local optimal choices lead to a globally optimal solution. Two important properties are greedy-choice property and optimal substructure.",
        [
            "Greedy-choice property: a global optimum can be reached by choosing local optimum first.",
            "Optimal substructure: optimal solution contains optimal solutions to subproblems.",
            "Greedy is usually faster and simpler than DP.",
            "Greedy may fail for 0/1 knapsack but works for fractional knapsack.",
            "Correctness proof is essential: exchange argument or cut property.",
        ],
        table=(["Problem", "Greedy Works?", "Reason"], [["Fractional knapsack", "Yes", "items divisible"], ["0/1 knapsack", "No", "choice may block better combination"], ["MST", "Yes", "cut property"], ["Dijkstra", "Yes with nonnegative weights", "settled vertex distance final"]]),
    ),
    unit_page(
        "Unit II: Optimal Merge Pattern",
        "Apply greedy method to minimize merge cost.",
        "Optimal merge pattern combines multiple sorted files with minimum total cost. At each step, merge the two smallest files first. This is greedy because small files should be used earlier to avoid repeatedly paying high merge cost. A min-heap is used to repeatedly extract two smallest sizes.",
        [
            "Insert all file sizes into min-heap.",
            "Remove two minimum sizes a and b.",
            "Merge cost = a+b; add it to total cost.",
            "Insert a+b back into heap.",
            "Repeat until one file remains.",
        ],
        code=[
            "total = 0",
            "while heap.size > 1:",
            "    a = extractMin(heap)",
            "    b = extractMin(heap)",
            "    total += a + b",
            "    insert(heap, a+b)",
        ],
        table=(["Files", "Greedy Merge", "Cost"], [["5, 10, 20, 30", "(5+10)=15", "15"], ["15, 20, 30", "(15+20)=35", "50"], ["35, 30", "(30+35)=65", "115"]]),
        remember=["Same idea appears in Huffman coding."],
    ),
    unit_page(
        "Unit II: Huffman Coding",
        "Use greedy strategy for optimal prefix codes.",
        "Huffman coding creates variable-length binary codes based on character frequencies. Frequent characters get shorter codes and rare characters get longer codes. The algorithm repeatedly combines the two least frequent nodes, forming a binary tree. It gives an optimal prefix-free code.",
        [
            "Prefix code: no codeword is prefix of another codeword.",
            "Use min-priority queue by frequency.",
            "Left/right edges are labeled 0/1.",
            "Final code for a character is path from root to leaf.",
            "Applications: file compression, data transmission.",
        ],
        code=[
            "for each character c: insert leaf(c, freq[c])",
            "while queue has more than one node:",
            "    x = extractMin()",
            "    y = extractMin()",
            "    z = new node with freq x.freq + y.freq",
            "    z.left = x; z.right = y",
            "    insert z",
        ],
        table=(["Property", "Huffman Coding"], [["Strategy", "combine two minimum frequencies"], ["Data Structure", "min heap"], ["Time", "O(n log n)"], ["Code Type", "prefix-free"]]),
    ),
    unit_page(
        "Unit II: Minimum Spanning Tree",
        "Find MST using greedy approach.",
        "A spanning tree of a connected undirected graph includes all vertices and has exactly V-1 edges. A minimum spanning tree has minimum total edge weight. MST algorithms use greedy choices based on safe edges. Two famous algorithms are Kruskal and Prim.",
        [
            "MST has no cycle.",
            "If graph has V vertices, MST has V-1 edges.",
            "Cut property: lightest edge crossing a cut is safe.",
            "Kruskal sorts edges and avoids cycles.",
            "Prim grows one tree from a starting vertex.",
        ],
        table=(["Algorithm", "Greedy Choice", "Data Structure", "Good For"], [["Kruskal", "smallest edge globally", "DSU/Union-Find", "sparse graphs"], ["Prim", "smallest edge from tree to outside", "priority queue", "dense/connected graphs"]]),
    ),
    unit_page(
        "Unit II: Prim's Algorithm",
        "Use greedy strategy to construct MST from a start vertex.",
        "Prim's algorithm starts with any vertex and repeatedly adds the minimum weight edge that connects the current tree to a vertex outside the tree. It maintains key[v], the minimum edge weight by which vertex v can be added to the MST. Parent array stores final MST edges.",
        [
            "Initialize key[start]=0 and all others infinity.",
            "Pick unvisited vertex u with minimum key.",
            "Mark u included in MST.",
            "For every neighbor v of u, update key[v] if edge(u,v) is smaller.",
            "After V picks, parent array gives MST.",
        ],
        code=[
            "Prim(G):",
            "    key[start] = 0",
            "    for count = 1 to V:",
            "        u = vertex with minimum key not in MST",
            "        add u to MST",
            "        for each edge (u,v,w):",
            "            if v not in MST and w < key[v]:",
            "                key[v] = w; parent[v] = u",
        ],
        table=(["Implementation", "Time"], [["Adjacency matrix", "O(V^2)"], ["Binary heap + list", "O(E log V)"], ["Space", "O(V+E)"]]),
    ),
    unit_page(
        "Unit II: Kruskal, Job Sequencing and Fractional Knapsack",
        "Compare common greedy algorithms.",
        "Kruskal's algorithm sorts all edges by weight and adds the next lightest edge if it does not create a cycle. Union-Find supports cycle checking. Job sequencing with deadlines selects profit-making jobs before deadlines using slots. Fractional knapsack selects items by maximum profit/weight ratio and can take fractions.",
        [
            "Kruskal: sort edges, add safe edges until V-1 edges selected.",
            "Union-Find operations: find parent, union sets.",
            "Job sequencing: sort jobs by profit descending; place each job in latest free slot before deadline.",
            "Fractional knapsack: sort by value/weight ratio and fill capacity greedily.",
            "0/1 knapsack cannot be solved greedily in general.",
        ],
        table=(["Problem", "Greedy Key", "Complexity"], [["Kruskal MST", "minimum edge avoiding cycle", "O(E log E)"], ["Job sequencing", "highest profit first", "O(n log n + nD)"], ["Fractional knapsack", "highest ratio first", "O(n log n)"]]),
    ),
    unit_page(
        "Unit II: Single Source Shortest Path",
        "Understand Dijkstra's greedy algorithm.",
        "Dijkstra's algorithm finds shortest paths from a single source to all vertices in a graph with nonnegative edge weights. It repeatedly selects the unvisited vertex with minimum tentative distance and relaxes its outgoing edges. Once a vertex is selected, its shortest distance becomes final.",
        [
            "Initialize dist[source]=0 and all others infinity.",
            "Pick vertex u with minimum dist among unvisited vertices.",
            "Relax each edge: if dist[u]+w < dist[v], update dist[v].",
            "Works only for nonnegative edge weights.",
            "For negative weights, Bellman-Ford is needed.",
        ],
        code=[
            "while priority queue not empty:",
            "    u = extractMin()",
            "    for each edge (u,v,w):",
            "        if dist[u] + w < dist[v]:",
            "            dist[v] = dist[u] + w",
            "            parent[v] = u",
        ],
        table=(["Implementation", "Time"], [["Matrix", "O(V^2)"], ["Binary heap", "O((V+E) log V)"], ["Condition", "No negative edges"]]),
    ),
    unit_page(
        "Unit II: Correctness Proof of Greedy Algorithms",
        "Write proof that greedy choice is safe.",
        "A greedy algorithm is not accepted only because it looks logical. It needs a correctness proof. Most greedy proofs show that there exists an optimal solution containing the greedy choice. Then the remaining problem is smaller and can be solved similarly. Common proof styles are exchange argument, cut property and induction.",
        [
            "Exchange argument: replace part of an optimal solution with greedy choice without worsening result.",
            "Cut property: in MST, minimum edge crossing any cut is safe.",
            "Induction: prove greedy is correct after each step.",
            "Counterexample is used to show greedy does not work for some problems.",
            "For exam answers, state property, prove safe choice, then show optimal substructure.",
        ],
        table=(["Algorithm", "Correctness Idea"], [["Prim/Kruskal", "cut property"], ["Huffman", "two least frequent symbols are siblings at deepest level"], ["Fractional knapsack", "exchange lower ratio item with higher ratio item"], ["Job sequencing", "latest slot keeps earlier slots free"]]),
    ),
    unit_page(
        "Unit III: Dynamic Programming Concept",
        "Solve problems with overlapping subproblems and optimal substructure.",
        "Dynamic programming stores solutions of subproblems and reuses them. It is suitable when the same subproblems occur repeatedly and the optimal answer can be built from optimal subanswers. DP may be top-down with memoization or bottom-up with tabulation.",
        [
            "Optimal substructure: optimal solution uses optimal subproblem solutions.",
            "Overlapping subproblems: recursive calls repeat same states.",
            "Memoization: recursive + cache.",
            "Tabulation: iterative table filling.",
            "DP often converts exponential recursion into polynomial time.",
        ],
        table=(["Approach", "Meaning", "Example"], [["Top-down", "solve recursively and store", "memoized Fibonacci"], ["Bottom-up", "fill table from base cases", "knapsack table"], ["State", "parameters defining subproblem", "i, capacity"], ["Transition", "formula between states", "include/exclude item"]]),
    ),
    unit_page(
        "Unit III: 0/1 Knapsack using DP",
        "Solve knapsack problem using dynamic programming.",
        "In 0/1 knapsack, each item can be either selected completely or rejected. Given weights, profits and capacity W, maximize profit without exceeding W. Greedy ratio does not always work because items are indivisible. DP state dp[i][w] means maximum profit using first i items with capacity w.",
        [
            "If weight[i] > w, item cannot be included.",
            "Otherwise choose max of exclude and include item.",
            "Transition: dp[i][w] = max(dp[i-1][w], profit[i] + dp[i-1][w-weight[i]]).",
            "Base: dp[0][w]=0 and dp[i][0]=0.",
            "Answer: dp[n][W].",
        ],
        code=[
            "for i = 1 to n:",
            "    for w = 0 to W:",
            "        if wt[i] <= w:",
            "            dp[i][w] = max(dp[i-1][w], val[i]+dp[i-1][w-wt[i]])",
            "        else:",
            "            dp[i][w] = dp[i-1][w]",
        ],
        table=(["Measure", "Value"], [["Time", "O(nW)"], ["Space", "O(nW), optimized O(W)"], ["Strategy", "DP not greedy"], ["Type", "pseudo-polynomial"]]),
    ),
    unit_page(
        "Unit III: Multistage Graph and Reliability Design",
        "Apply DP to staged decision problems.",
        "A multistage graph is a directed weighted graph whose vertices are divided into stages. Edges go from one stage to the next. The objective is usually to find the minimum cost path from source to sink. DP solves it backward from destination. Reliability design allocates resources among components to maximize system reliability under cost/weight constraints.",
        [
            "For multistage graph, cost[v] = min over edges(v,u) of c(v,u)+cost[u].",
            "Destination cost is zero.",
            "Decision at each stage depends on best future cost.",
            "Reliability design uses DP where state may be component index and budget.",
            "DP is useful when choices are sequential and constrained.",
        ],
        table=(["Problem", "State", "Transition"], [["Multistage graph", "vertex v", "minimum edge cost plus next state"], ["Reliability", "component i, budget b", "choose redundancy level"], ["Resource allocation", "stage, resource left", "maximize benefit"]]),
    ),
    unit_page(
        "Unit III: Floyd-Warshall Algorithm",
        "Find all-pairs shortest paths using dynamic programming.",
        "Floyd-Warshall finds shortest paths between every pair of vertices in a weighted graph. It allows negative edges but not negative cycles. The idea is to gradually allow intermediate vertices. dist[i][j] is improved by checking whether path i -> k -> j is shorter than current i -> j.",
        [
            "Initialize dist[i][j] with edge weights, 0 for i=j, infinity if no edge.",
            "For each intermediate vertex k, update all pairs i,j.",
            "Transition: dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j]).",
            "Negative cycle exists if dist[i][i] becomes negative.",
            "Also used for transitive closure with boolean operations.",
        ],
        code=[
            "for k = 1 to V:",
            "    for i = 1 to V:",
            "        for j = 1 to V:",
            "            if dist[i][k] + dist[k][j] < dist[i][j]:",
            "                dist[i][j] = dist[i][k] + dist[k][j]",
        ],
        table=(["Measure", "Value"], [["Time", "O(V^3)"], ["Space", "O(V^2)"], ["Negative edges", "Allowed"], ["Negative cycle", "Not allowed"]]),
    ),
    unit_page(
        "Unit IV: Backtracking Concept",
        "Use state-space tree and pruning.",
        "Backtracking is a systematic search technique that builds a solution step by step and abandons a partial solution as soon as it is known that it cannot lead to a valid answer. It is mainly used for constraint satisfaction problems. The search is represented as a state-space tree.",
        [
            "Choose: make one possible decision.",
            "Explore: recursively continue.",
            "Unchoose: undo decision and try next option.",
            "Pruning reduces unnecessary exploration.",
            "Examples: 8 queens, graph coloring, Hamiltonian cycle, subset sum.",
        ],
        table=(["Term", "Meaning"], [["State-space tree", "all possible partial and complete solutions"], ["Promising node", "partial solution that may lead to answer"], ["Pruning", "discarding non-promising branches"], ["Feasibility test", "checking constraints before deeper recursion"]]),
    ),
    unit_page(
        "Unit IV: Eight Queens Problem",
        "Apply backtracking to place queens safely.",
        "The 8 queens problem asks to place 8 queens on an 8x8 chessboard so that no two queens attack each other. A queen attacks same row, same column and diagonals. Standard backtracking places one queen per row and tries columns. If a placement is safe, recursion moves to next row; otherwise it tries another column.",
        [
            "Represent solution as x[row] = column of queen in that row.",
            "No two queens can share same column.",
            "Diagonal condition: abs(row1-row2) != abs(col1-col2).",
            "If row becomes 8, a full solution is found.",
            "Backtracking explores only safe partial boards.",
        ],
        code=[
            "solve(row):",
            "    if row == N: print solution",
            "    for col = 0 to N-1:",
            "        if isSafe(row, col):",
            "            place queen",
            "            solve(row + 1)",
            "            remove queen",
        ],
        table=(["Measure", "Value"], [["Naive possibilities", "8^8"], ["With one queen per row", "8!"], ["Technique", "backtracking + pruning"], ["General problem", "N-Queens"]]),
    ),
    unit_page(
        "Unit IV: Hamiltonian Cycle and Graph Coloring",
        "Use backtracking for graph problems.",
        "A Hamiltonian cycle visits every vertex exactly once and returns to the starting vertex. Backtracking tries to build a path by adding adjacent unused vertices. Graph coloring assigns colors to vertices so that adjacent vertices have different colors. Backtracking tries colors vertex by vertex and rejects unsafe assignments.",
        [
            "Hamiltonian cycle is different from Euler cycle: Hamiltonian focuses on vertices, Euler on edges.",
            "Graph coloring decision problem asks whether graph can be colored with m colors.",
            "Safe color check: no adjacent already-colored vertex has same color.",
            "Both problems are computationally hard for general graphs.",
            "Backtracking can solve small instances exactly.",
        ],
        table=(["Problem", "Decision", "Constraint"], [["Hamiltonian cycle", "next vertex in path", "adjacent and not already used"], ["Graph coloring", "color for vertex", "no same color on adjacent vertices"], ["Subset sum", "include/exclude item", "sum target not violated"]]),
    ),
    unit_page(
        "Unit IV: Branch and Bound Method",
        "Solve optimization problems using bounds.",
        "Branch and bound is used for optimization problems. It explores a state-space tree like backtracking but uses bounds to avoid branches that cannot improve the current best solution. Branch means splitting into subproblems. Bound means estimating the best possible solution from a node.",
        [
            "Maintain incumbent: best feasible solution found so far.",
            "If node bound is worse than incumbent, prune it.",
            "Live node: generated but not expanded.",
            "E-node: node currently being expanded.",
            "Least-cost branch and bound expands node with best bound first.",
        ],
        table=(["Backtracking", "Branch and Bound"], [["Mostly feasibility problems", "Mostly optimization problems"], ["Uses constraint pruning", "Uses objective bound pruning"], ["DFS common", "BFS/priority queue common"], ["Examples: N-queens", "Examples: TSP, 0/1 knapsack"]]),
    ),
    unit_page(
        "Unit IV: Traveling Salesman Problem using Branch and Bound",
        "Implement branch and bound idea for TSP.",
        "In TSP, a salesman must visit each city exactly once and return to the starting city with minimum total cost. Branch and bound avoids checking all tours by computing lower bounds. A common matrix reduction method subtracts row minima and column minima; the sum gives a lower bound.",
        [
            "State represents partial tour.",
            "Branch by choosing next city or including/excluding an edge.",
            "Bound estimates minimum possible completion cost.",
            "If bound >= best tour cost, discard node.",
            "Priority queue can expand node with smallest lower bound.",
        ],
        table=(["Step", "Action"], [["1", "Create cost matrix and set diagonal infinity"], ["2", "Reduce rows and columns to get initial lower bound"], ["3", "Branch to possible next cities"], ["4", "Add travel cost and new reduction cost"], ["5", "Update best complete tour and prune bad nodes"]]),
        remember=["TSP brute force is O(n!), so bounding is important."],
    ),
    unit_page(
        "Unit IV: Lower Bound Theory",
        "Understand lower bounds and their use.",
        "A lower bound is the minimum amount of work required by any algorithm to solve a problem under a model of computation. It helps prove that an algorithm is optimal. For example, comparison-based sorting has lower bound Omega(n log n), so merge sort and heap sort are asymptotically optimal in that model.",
        [
            "Lower bound is about the problem, not only one algorithm.",
            "Upper bound is shown by giving an algorithm.",
            "If lower and upper bounds match, the algorithm is optimal.",
            "Decision tree model proves sorting lower bound.",
            "In branch and bound, lower bound estimates best possible solution under a node.",
        ],
        table=(["Problem", "Known Lower Bound", "Matching Algorithm"], [["Comparison sorting", "Omega(n log n)", "merge sort, heap sort"], ["Searching unsorted list", "Omega(n)", "linear search"], ["Searching sorted array", "Omega(log n)", "binary search"], ["Matrix multiplication", "not fully settled", "advanced algorithms improve upper bound"]]),
    ),
    unit_page(
        "Unit V: Advanced Tree and Graph Algorithms",
        "Revise important graph and tree concepts.",
        "Advanced graph algorithms build on traversal, shortest path, spanning tree and connectivity ideas. Graph representation affects complexity. Adjacency matrix is simple but takes O(V^2) space. Adjacency list is efficient for sparse graphs. Tree algorithms often use traversal, balancing and divide-and-conquer.",
        [
            "BFS explores level by level using queue; useful for unweighted shortest path.",
            "DFS explores deeply using stack/recursion; useful for cycle detection and topological sort.",
            "Topological sorting applies to DAGs.",
            "Minimum spanning tree applies to undirected connected weighted graphs.",
            "Shortest path algorithms depend on weight conditions.",
        ],
        table=(["Algorithm", "Use", "Time"], [["BFS", "unweighted shortest path", "O(V+E)"], ["DFS", "components/cycle/topological", "O(V+E)"], ["Prim/Kruskal", "MST", "O(E log V) typical"], ["Dijkstra", "nonnegative SSSP", "O((V+E)logV)"]]),
    ),
    unit_page(
        "Unit V: NP-Hard and NP-Complete Problems",
        "Classify difficult computational problems.",
        "P is the class of problems solvable in polynomial time. NP is the class of decision problems whose solution can be verified in polynomial time. A problem is NP-hard if every problem in NP can be reduced to it in polynomial time. A problem is NP-complete if it is both in NP and NP-hard.",
        [
            "P: efficiently solvable problems.",
            "NP: efficiently verifiable problems.",
            "NP-complete problems are the hardest problems inside NP.",
            "NP-hard problems may be optimization problems and may not be in NP.",
            "If any NP-complete problem has polynomial solution, then P = NP.",
        ],
        table=(["Class", "Meaning", "Example"], [["P", "polynomial-time solvable", "MST, shortest path"], ["NP", "solution verifiable in polynomial time", "Hamiltonian cycle"], ["NP-complete", "in NP and NP-hard", "SAT, 3-SAT, Hamiltonian cycle"], ["NP-hard", "at least as hard as NP", "TSP optimization"]]),
    ),
    unit_page(
        "Unit V: Approximation Algorithms",
        "Use near-optimal solutions for hard problems.",
        "For NP-hard optimization problems, exact algorithms may be too slow for large inputs. Approximation algorithms run in polynomial time and guarantee solution quality within a factor of optimum. Approximation ratio measures this guarantee.",
        [
            "Used when exact optimal solution is computationally expensive.",
            "Approximation ratio for minimization: algorithm cost / optimal cost.",
            "For maximization: optimal value / algorithm value.",
            "A 2-approximation for minimization gives solution at most twice optimum.",
            "Heuristics may work well but do not always provide proof guarantee.",
        ],
        table=(["Problem", "Approximation Idea"], [["Vertex cover", "pick both endpoints of uncovered edge"], ["Metric TSP", "MST-based tour gives bounded ratio"], ["Set cover", "greedy gives logarithmic approximation"], ["Knapsack", "FPTAS possible for 0/1 knapsack"]]),
    ),
    unit_page(
        "Unit V: Randomized and Stream Algorithms",
        "Know algorithms for uncertainty and massive data.",
        "Randomized algorithms use random choices to improve simplicity or expected performance. Example: randomized quick sort selects random pivot, making worst-case input unlikely. Stream algorithms process data arriving continuously and cannot store all input. They use small memory and often give approximate answers.",
        [
            "Las Vegas algorithms always correct but running time is random.",
            "Monte Carlo algorithms have bounded probability of error.",
            "Randomized quick sort has expected O(n log n) time.",
            "Stream model: one pass or few passes over data.",
            "Examples: counting distinct elements, frequency estimation, heavy hitters.",
        ],
        table=(["Type", "Feature", "Example"], [["Las Vegas", "correct answer, random time", "randomized quicksort variant"], ["Monte Carlo", "fast, small error chance", "primality testing"], ["Streaming", "small memory", "count-min sketch"], ["Online", "input arrives over time", "online scheduling"]]),
    ),
    unit_page(
        "Unit V: Parallel Algorithms",
        "Understand basic design and complexity of parallel algorithms.",
        "Parallel algorithms divide computation among multiple processors to reduce running time. Important measures are work, span, speedup and efficiency. Work is total operations performed; span is longest dependency chain. A good parallel algorithm has enough independent tasks and low communication overhead.",
        [
            "Speedup = serial time / parallel time.",
            "Efficiency = speedup / number of processors.",
            "Amdahl's law: serial portion limits maximum speedup.",
            "Parallel divide-and-conquer works well when subproblems are independent.",
            "Communication and synchronization overhead can reduce benefit.",
        ],
        table=(["Term", "Meaning"], [["Work", "total computation over all processors"], ["Span", "critical path length"], ["Speedup", "how many times faster"], ["Efficiency", "processor utilization"], ["Scalability", "performance as processors increase"]]),
    ),
    unit_page(
        "Final Revision: Must-Write Algorithms and Answers",
        "Last-page quick revision for exams.",
        "Before the exam, revise definitions, properties, pseudocode and complexity table. In long answers, draw the state-space tree or table when possible. For numerical problems, show each step clearly because marks are given for method, not only final answer.",
        [
            "Merge sort: recurrence T(n)=2T(n/2)+n, time O(n log n), space O(n).",
            "Prim: start vertex, key array, pick minimum key outside MST, update neighbors.",
            "0/1 knapsack: include/exclude DP table, time O(nW).",
            "8 queens: one queen per row, check columns and diagonals.",
            "TSP branch and bound: partial tour, lower bound, prune when bound is worse.",
            "NP-complete: in NP + every NP problem reduces to it.",
        ],
        table=(["Question Type", "Write These Points"], [["Define/short note", "definition + properties + example"], ["Algorithm", "idea + pseudocode + complexity"], ["Compare", "table of differences"], ["Proof", "property + argument + conclusion"], ["Numerical", "steps + table/tree + final answer"]]),
        remember=["High scoring formulas: Master theorem, knapsack transition, Floyd transition, speedup and efficiency."],
    ),
]


def build():
    doc = Document()
    section = doc.sections[0]
    section.top_margin = Cm(1.15)
    section.bottom_margin = Cm(1.1)
    section.left_margin = Cm(1.25)
    section.right_margin = Cm(1.25)

    styles = doc.styles
    styles["Normal"].font.name = "Arial"
    styles["Normal"].font.size = Pt(8.6)
    styles["List Bullet"].font.name = "Arial"
    styles["List Bullet"].font.size = Pt(8.5)

    for idx, page in enumerate(pages, start=1):
        header = doc.add_paragraph()
        header.alignment = WD_ALIGN_PARAGRAPH.RIGHT
        header.paragraph_format.space_after = Pt(1)
        hr = header.add_run(f"Page {idx} of 35")
        hr.font.name = "Arial"
        hr.font.size = Pt(7.5)
        hr.font.color.rgb = RGBColor(110, 110, 110)

        if idx == 1:
            p = doc.add_paragraph()
            p.alignment = WD_ALIGN_PARAGRAPH.CENTER
            p.paragraph_format.space_before = Pt(18)
            r = p.add_run("DESIGN AND ANALYSIS OF ALGORITHMS")
            r.bold = True
            r.font.name = "Arial"
            r.font.size = Pt(20)
            r.font.color.rgb = RGBColor(31, 78, 121)
            p2 = doc.add_paragraph()
            p2.alignment = WD_ALIGN_PARAGRAPH.CENTER
            r2 = p2.add_run("35 Page Detailed Exam Notes")
            r2.bold = True
            r2.font.name = "Arial"
            r2.font.size = Pt(14)
            r2.font.color.rgb = RGBColor(80, 80, 80)
        add_heading(doc, page["title"], 1)
        add_para(doc, "Learning target: " + page["objectives"])
        add_para(doc, page["theory"])
        if page["bullets"]:
            add_heading(doc, "Important Points", 2)
            add_bullets(doc, page["bullets"])
        if page["code"]:
            add_heading(doc, "Algorithm / Pseudocode", 2)
            add_code(doc, page["code"])
        if page["table"]:
            add_heading(doc, "Quick Table", 2)
            add_table(doc, page["table"][0], page["table"][1])
        if page["remember"]:
            add_heading(doc, "Remember", 2)
            add_bullets(doc, page["remember"])
        add_heading(doc, "Practice Questions", 2)
        add_bullets(doc, exam_questions(page["title"]))
        if idx != len(pages):
            doc.add_page_break()

    doc.save(OUT)


if __name__ == "__main__":
    if len(pages) != 35:
        raise SystemExit(f"Expected 35 pages, got {len(pages)}")
    build()
    print(OUT)
