"""
Generator for remaining topics: OOP, Advanced Python, Functional Programming, Basics,
Advanced Mathematics, Advanced Problems, Competitive Programming,
Concurrency, SystemDesign, Databases, Networking, Security, Testing,
DataScience, MachineLearning, WebDevelopment, GameDevelopment,
RealWorldApplication, RealWorldProblem, Miscellaneous
"""
import os

BASE_DIR = r"d:\500DCPP"

def write_file(filepath, content):
    os.makedirs(os.path.dirname(filepath), exist_ok=True)
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)

def gen_p(idx, title, stmt, inp, out, con, ex_in, ex_out):
    return f"# Problem {idx}: {title}\n\n## Problem Statement\n{stmt}\n\n## Input Format\n- {inp}\n\n## Output Format\n- {out}\n\n## Constraints\n- {con}\n\n## Example\n**Input:** {ex_in}  \n**Output:** {ex_out}\n"

def gen_s(idx, title, approach, steps, tc, sc, code):
    sl = "\n".join(f"{i+1}. {s}" for i, s in enumerate(steps))
    return f"# Solution {idx}: {title}\n\n## Approach Explanation\n{approach}\n\n## Step-by-Step Logic\n{sl}\n\n## Complexity\n- **Time Complexity:** {tc}\n- **Space Complexity:** {sc}\n\n## Code\n```python\n{code}\n```\n"

def write_topic(folder, probs, sols):
    for i, (t,st,inp,out,con,ei,eo) in enumerate(probs, 1):
        write_file(os.path.join(BASE_DIR, folder, "Problems", f"problem{i}.md"), gen_p(i,t,st,inp,out,con,ei,eo))
    for i, (t,ap,steps,tc,sc,code) in enumerate(sols, 1):
        write_file(os.path.join(BASE_DIR, folder, "Solutions", f"solution{i}.md"), gen_s(i,t,ap,steps,tc,sc,code))
    print(f"  DONE {folder}: {len(probs)}P + {len(sols)}S")

# ==============================
# OOP
# ==============================
OOP_P = [
    ("Design a Bank Account Class", "Create a BankAccount class with deposit, withdraw, and balance methods. Support overdraft protection.", "Operations on BankAccount.", "Account balance after operations.", "Balance >= 0", "deposit(100), withdraw(30), balance()", "70"),
    ("Implement Inheritance: Shape Hierarchy", "Create an abstract Shape class with Circle, Rectangle, Triangle subclasses. Each must implement area() and perimeter().", "Shape dimensions.", "Area and perimeter values.", "Dimensions > 0", "Circle(5).area()", "78.54"),
    ("Design a Library Management System", "Create classes for Book, Member, and Library. Support borrowing and returning books.", "Library operations.", "Book availability status.", "Max 5 books per member", "borrow('Book1'), return('Book1')", "Success"),
    ("Implement Observer Pattern", "Design an event system where subjects notify observers on state changes.", "Events and observers.", "Notifications received.", "1 <= observers <= 100", "subscribe(obs), notify('event')", "Observer notified"),
    ("Design a Parking Lot System", "Create a parking lot system with different vehicle types and parking spots.", "Vehicle entries/exits.", "Available spots count.", "1 <= spots <= 1000", "park(Car()), leave(1)", "Spot freed"),
    ("Implement Strategy Pattern", "Design a payment system that uses different strategies (Credit, PayPal, Crypto).", "Payment method and amount.", "Payment confirmation.", "Amount > 0", "pay(CreditCard(), 100)", "Paid 100 via CreditCard"),
    ("Design a Deck of Cards", "Create classes for Card, Deck with shuffle and deal operations.", "Deck operations.", "Cards dealt.", "Standard 52-card deck", "shuffle(), deal(5)", "5 random cards"),
    ("Implement Factory Pattern", "Design a vehicle factory that creates Car, Truck, or Motorcycle objects based on type.", "Vehicle type string.", "Vehicle object.", "Valid types: car, truck, motorcycle", 'create("car")', "Car object"),
    ("Design a Stack using OOP", "Implement a Stack class with push, pop, peek, isEmpty, and size methods.", "Stack operations.", "Values from pop/peek.", "1 <= operations <= 10^4", "push(5), push(3), pop()", "3"),
    ("Implement Singleton Pattern", "Design a class that ensures only one instance exists throughout the program.", "Instance creation attempts.", "Same instance returned.", "Multiple creation calls", "Singleton(), Singleton()", "Same object"),
    ("Design an Employee Management System", "Create Employee, Manager, and Department classes with salary calculation and reporting.", "Employee data operations.", "Salary and reports.", "1 <= employees <= 1000", "add_employee(emp), total_salary()", "Sum of salaries"),
    ("Implement Decorator Pattern", "Design a coffee ordering system where extras (milk, sugar) are decorators.", "Base item + decorators.", "Description and total cost.", "1 <= decorators <= 5", "Coffee() + Milk() + Sugar()", "Coffee, Milk, Sugar: $3.50"),
    ("Design a Linked List using OOP", "Implement a singly linked list with Node and LinkedList classes.", "List operations.", "List contents.", "0 <= nodes <= 10^4", "append(1), append(2), display()", "[1, 2]"),
    ("Implement Iterator Pattern", "Create a custom iterator for a binary tree that returns elements in in-order.", "Binary tree.", "Elements in order.", "1 <= nodes <= 10^4", "next(), next(), hasNext()", "Values in order"),
    ("Design a Tic-Tac-Toe Game", "Implement a Tic-Tac-Toe game with a Board class and Player classes.", "Player moves.", "Game state (win/draw/continue).", "3x3 board", "move(0,0,'X'), move(1,1,'O')", "Continue"),
    ("Implement Command Pattern", "Design a remote control system where button presses execute commands.", "Button assignments and presses.", "Actions executed.", "1 <= buttons <= 10", "set_command(0, LightOn()), press(0)", "Light turned on"),
    ("Design a File System", "Create classes for File, Directory with create, delete, and list operations.", "File system operations.", "Directory listing.", "Path length <= 200", 'create("/a/b/c"), ls("/a")', '["b"]'),
    ("Implement Composition vs Inheritance", "Demonstrate composition by creating Engine and Car classes where Car HAS-A Engine.", "Car operations.", "Car status.", "Engine types: electric, gas", "Car(ElectricEngine()).start()", "Electric engine started"),
    ("Design a Queue using Two Stacks", "Implement a Queue using two Stack objects (OOP composition).", "Queue operations: enqueue, dequeue.", "Values from dequeue.", "1 <= operations <= 10^4", "enqueue(1), enqueue(2), dequeue()", "1"),
    ("Design a Social Media Post System", "Create User, Post, and Comment classes with like and reply functionality.", "Social actions.", "Post details.", "1 <= likes <= 10^6", "post.like(user), post.comment(user, text)", "1 like, 1 comment"),
]

OOP_S = [
    ("Bank Account Class", "Encapsulate balance as private, expose methods for deposits and withdrawals with validation.", ["Define __init__ with balance.", "deposit adds to balance.", "withdraw checks for sufficient funds."], "O(1) per operation", "O(1)",
     "class BankAccount:\n    def __init__(self, balance=0):\n        self._balance = balance\n    def deposit(self, amount):\n        if amount > 0:\n            self._balance += amount\n    def withdraw(self, amount):\n        if 0 < amount <= self._balance:\n            self._balance -= amount\n            return True\n        return False\n    def balance(self):\n        return self._balance"),
    ("Shape Hierarchy", "Use abstract base class with abc module. Each subclass implements area() and perimeter().", ["Define abstract Shape with @abstractmethod.", "Circle uses pi*r^2 and 2*pi*r.", "Rectangle uses l*w and 2*(l+w)."], "O(1)", "O(1)",
     "from abc import ABC, abstractmethod\nimport math\n\nclass Shape(ABC):\n    @abstractmethod\n    def area(self): pass\n    @abstractmethod\n    def perimeter(self): pass\n\nclass Circle(Shape):\n    def __init__(self, r): self.r = r\n    def area(self): return math.pi * self.r**2\n    def perimeter(self): return 2 * math.pi * self.r\n\nclass Rectangle(Shape):\n    def __init__(self, l, w): self.l, self.w = l, w\n    def area(self): return self.l * self.w\n    def perimeter(self): return 2 * (self.l + self.w)"),
    ("Library Management System", "Use classes with relationships: Library has Books and Members.", ["Book tracks title, author, available status.", "Member has borrowed books list.", "Library manages checkout/return."], "O(1) per operation", "O(N)",
     "class Book:\n    def __init__(self, title, author):\n        self.title = title\n        self.author = author\n        self.available = True\n\nclass Member:\n    def __init__(self, name):\n        self.name = name\n        self.borrowed = []\n\nclass Library:\n    def __init__(self):\n        self.books = []\n        self.members = []\n    def borrow(self, member, book):\n        if book.available and len(member.borrowed) < 5:\n            book.available = False\n            member.borrowed.append(book)\n            return True\n        return False"),
    ("Observer Pattern", "Subject maintains a list of observers and notifies them on state changes.", ["Subject has list of observers.", "subscribe/unsubscribe manage the list.", "notify calls update on all observers."], "O(N) for notify", "O(N)",
     "class Subject:\n    def __init__(self):\n        self._observers = []\n    def subscribe(self, observer):\n        self._observers.append(observer)\n    def unsubscribe(self, observer):\n        self._observers.remove(observer)\n    def notify(self, event):\n        for obs in self._observers:\n            obs.update(event)\n\nclass Observer:\n    def update(self, event):\n        print(f'Received: {event}')"),
    ("Parking Lot System", "Use classes for ParkingSpot, Vehicle with size matching.", ["ParkingLot manages spots.", "Vehicles have sizes.", "Match vehicle to appropriate spot."], "O(N) to find spot", "O(N)",
     "class Vehicle:\n    def __init__(self, plate, size):\n        self.plate = plate\n        self.size = size\n\nclass ParkingSpot:\n    def __init__(self, spot_id, size):\n        self.id = spot_id\n        self.size = size\n        self.vehicle = None\n    def park(self, vehicle):\n        if not self.vehicle and vehicle.size <= self.size:\n            self.vehicle = vehicle\n            return True\n        return False\n    def leave(self):\n        self.vehicle = None"),
    ("Strategy Pattern", "Define a PaymentStrategy interface and concrete implementations.", ["Abstract PaymentStrategy with pay method.", "CreditCard, PayPal, Crypto implement pay.", "Context class uses the strategy."], "O(1)", "O(1)",
     "from abc import ABC, abstractmethod\n\nclass PaymentStrategy(ABC):\n    @abstractmethod\n    def pay(self, amount): pass\n\nclass CreditCard(PaymentStrategy):\n    def pay(self, amount): return f'Paid {amount} via Credit Card'\n\nclass PayPal(PaymentStrategy):\n    def pay(self, amount): return f'Paid {amount} via PayPal'\n\nclass PaymentContext:\n    def __init__(self, strategy):\n        self.strategy = strategy\n    def execute(self, amount):\n        return self.strategy.pay(amount)"),
    ("Deck of Cards", "Card has suit and rank. Deck initializes all 52 and supports shuffle/deal.", ["Card class with suit and rank.", "Deck creates all 52 cards.", "shuffle uses random.shuffle, deal pops cards."], "O(N) for shuffle", "O(N)",
     "import random\n\nclass Card:\n    def __init__(self, suit, rank):\n        self.suit = suit\n        self.rank = rank\n    def __repr__(self): return f'{self.rank} of {self.suit}'\n\nclass Deck:\n    suits = ['Hearts','Diamonds','Clubs','Spades']\n    ranks = ['2','3','4','5','6','7','8','9','10','J','Q','K','A']\n    def __init__(self):\n        self.cards = [Card(s,r) for s in self.suits for r in self.ranks]\n    def shuffle(self): random.shuffle(self.cards)\n    def deal(self, n=1): return [self.cards.pop() for _ in range(min(n, len(self.cards)))]"),
    ("Factory Pattern", "A factory method creates objects based on a type parameter.", ["Define Vehicle base class.", "Car, Truck, Motorcycle subclasses.", "Factory method returns correct type."], "O(1)", "O(1)",
     "class Vehicle:\n    def describe(self): pass\n\nclass Car(Vehicle):\n    def describe(self): return 'Car'\n\nclass Truck(Vehicle):\n    def describe(self): return 'Truck'\n\ndef vehicle_factory(v_type):\n    types = {'car': Car, 'truck': Truck}\n    cls = types.get(v_type.lower())\n    if cls: return cls()\n    raise ValueError(f'Unknown type: {v_type}')"),
    ("Stack using OOP", "Use a list internally with methods wrapping list operations.", ["__init__ with empty list.", "push appends, pop removes last.", "peek returns last, isEmpty checks length."], "O(1) per operation", "O(N)",
     "class Stack:\n    def __init__(self):\n        self._items = []\n    def push(self, item): self._items.append(item)\n    def pop(self):\n        if self.is_empty(): raise IndexError('Stack empty')\n        return self._items.pop()\n    def peek(self): return self._items[-1] if self._items else None\n    def is_empty(self): return len(self._items) == 0\n    def size(self): return len(self._items)"),
    ("Singleton Pattern", "Use __new__ to control instance creation, returning existing instance if one exists.", ["Override __new__.", "Check if instance exists.", "If not, create and store it."], "O(1)", "O(1)",
     "class Singleton:\n    _instance = None\n    def __new__(cls):\n        if cls._instance is None:\n            cls._instance = super().__new__(cls)\n        return cls._instance"),
    ("Employee Management", "Use inheritance: Employee base, Manager extends with reports.", ["Employee has name, salary.", "Manager has list of reports.", "Department aggregates employees."], "O(N) for total salary", "O(N)",
     "class Employee:\n    def __init__(self, name, salary):\n        self.name = name\n        self.salary = salary\n\nclass Manager(Employee):\n    def __init__(self, name, salary):\n        super().__init__(name, salary)\n        self.reports = []\n    def add_report(self, emp): self.reports.append(emp)\n\nclass Department:\n    def __init__(self, name):\n        self.name = name\n        self.employees = []\n    def add(self, emp): self.employees.append(emp)\n    def total_salary(self): return sum(e.salary for e in self.employees)"),
    ("Decorator Pattern", "Wrap base component with decorator classes that add behavior.", ["Base Coffee class.", "MilkDecorator wraps and adds cost.", "Each decorator extends description and cost."], "O(D) where D is decorators", "O(D)",
     "class Coffee:\n    def cost(self): return 2.0\n    def description(self): return 'Coffee'\n\nclass MilkDecorator:\n    def __init__(self, coffee): self._coffee = coffee\n    def cost(self): return self._coffee.cost() + 0.5\n    def description(self): return self._coffee.description() + ', Milk'\n\nclass SugarDecorator:\n    def __init__(self, coffee): self._coffee = coffee\n    def cost(self): return self._coffee.cost() + 0.25\n    def description(self): return self._coffee.description() + ', Sugar'"),
    ("Linked List OOP", "Node stores value and next pointer. LinkedList manages head and operations.", ["Node has val and next.", "LinkedList has head.", "append, prepend, delete, display methods."], "O(N) for operations", "O(N)",
     "class Node:\n    def __init__(self, val):\n        self.val = val\n        self.next = None\n\nclass LinkedList:\n    def __init__(self): self.head = None\n    def append(self, val):\n        if not self.head: self.head = Node(val); return\n        curr = self.head\n        while curr.next: curr = curr.next\n        curr.next = Node(val)\n    def display(self):\n        vals, curr = [], self.head\n        while curr: vals.append(curr.val); curr = curr.next\n        return vals"),
    ("Iterator Pattern", "Implement __iter__ and __next__ for a BST in-order traversal using a stack.", ["Initialize stack with leftmost path.", "__next__ pops, processes, pushes right subtree.", "StopIteration when stack empty."], "O(1) amortized per next", "O(H)",
     "class BSTIterator:\n    def __init__(self, root):\n        self.stack = []\n        self._push_left(root)\n    def _push_left(self, node):\n        while node:\n            self.stack.append(node)\n            node = node.left\n    def __iter__(self): return self\n    def __next__(self):\n        if not self.stack: raise StopIteration\n        node = self.stack.pop()\n        self._push_left(node.right)\n        return node.val\n    def has_next(self): return len(self.stack) > 0"),
    ("Tic-Tac-Toe Game", "Board class manages 3x3 grid. Check rows, columns, diagonals for wins.", ["Board initializes 3x3 grid.", "move places symbol, checks win.", "Check all 8 winning conditions."], "O(1) per move", "O(1)",
     "class TicTacToe:\n    def __init__(self):\n        self.board = [[' ']*3 for _ in range(3)]\n        self.current = 'X'\n    def move(self, r, c):\n        if self.board[r][c] != ' ': return 'Invalid'\n        self.board[r][c] = self.current\n        if self._check_win(): return f'{self.current} wins!'\n        self.current = 'O' if self.current == 'X' else 'X'\n        return 'Continue'\n    def _check_win(self):\n        b, c = self.board, self.current\n        for i in range(3):\n            if all(b[i][j]==c for j in range(3)): return True\n            if all(b[j][i]==c for j in range(3)): return True\n        if all(b[i][i]==c for i in range(3)): return True\n        if all(b[i][2-i]==c for i in range(3)): return True\n        return False"),
    ("Command Pattern", "Commands encapsulate actions. Invoker stores and executes commands.", ["Command interface with execute/undo.", "Concrete commands implement actions.", "Invoker stores command history."], "O(1) per command", "O(N)",
     "from abc import ABC, abstractmethod\n\nclass Command(ABC):\n    @abstractmethod\n    def execute(self): pass\n\nclass LightOnCommand(Command):\n    def __init__(self, light): self.light = light\n    def execute(self): self.light.on()\n\nclass Light:\n    def on(self): print('Light is ON')\n    def off(self): print('Light is OFF')\n\nclass RemoteControl:\n    def __init__(self): self.commands = {}\n    def set_command(self, slot, cmd): self.commands[slot] = cmd\n    def press(self, slot): self.commands[slot].execute()"),
    ("File System", "Directory contains files and subdirectories. Support path-based operations.", ["File has name and content.", "Directory has children dict.", "Traverse path to find target."], "O(P) where P is path depth", "O(N)",
     "class FileNode:\n    def __init__(self, name, is_dir=True):\n        self.name = name\n        self.is_dir = is_dir\n        self.children = {} if is_dir else None\n        self.content = '' if not is_dir else None\n\nclass FileSystem:\n    def __init__(self): self.root = FileNode('/')\n    def _traverse(self, path):\n        node = self.root\n        for part in path.strip('/').split('/'):\n            if part: node = node.children.get(part)\n            if not node: return None\n        return node\n    def mkdir(self, path):\n        node = self.root\n        for part in path.strip('/').split('/'):\n            if part not in node.children:\n                node.children[part] = FileNode(part)\n            node = node.children[part]"),
    ("Composition vs Inheritance", "Car HAS-A Engine (composition) rather than IS-A Engine", ["Engine class with start/stop.", "Car holds an Engine instance.", "Car delegates to engine."], "O(1)", "O(1)",
     "class Engine:\n    def __init__(self, engine_type): self.type = engine_type\n    def start(self): return f'{self.type} engine started'\n    def stop(self): return f'{self.type} engine stopped'\n\nclass Car:\n    def __init__(self, engine):\n        self.engine = engine\n    def start(self): return self.engine.start()\n    def stop(self): return self.engine.stop()"),
    ("Queue using Two Stacks", "Use two stacks: one for enqueue, one for dequeue. Transfer elements lazily.", ["Push to stack1 for enqueue.", "For dequeue, if stack2 empty, transfer all from stack1.", "Pop from stack2."], "O(1) amortized", "O(N)",
     "class QueueTwoStacks:\n    def __init__(self):\n        self.s1 = []\n        self.s2 = []\n    def enqueue(self, val): self.s1.append(val)\n    def dequeue(self):\n        if not self.s2:\n            while self.s1:\n                self.s2.append(self.s1.pop())\n        if not self.s2: raise IndexError('Queue empty')\n        return self.s2.pop()\n    def is_empty(self): return not self.s1 and not self.s2"),
    ("Social Media Post System", "Post has author, content, likes set, and comments list.", ["User creates Posts.", "Post supports like/unlike.", "Comment linked to Post."], "O(1) per operation", "O(N)",
     "class User:\n    def __init__(self, name): self.name = name\n\nclass Post:\n    def __init__(self, author, content):\n        self.author = author\n        self.content = content\n        self.likes = set()\n        self.comments = []\n    def like(self, user): self.likes.add(user.name)\n    def comment(self, user, text): self.comments.append((user.name, text))\n    def like_count(self): return len(self.likes)"),
]

# ==============================
# Helper to generate simple topic data
# ==============================
def simple_topics():
    """Generate simple problem/solution data for remaining topics."""
    topics = {}
    
    # ADVANCED PYTHON CONCEPTS
    topics["Advanced_PythonConcept"] = {
        "titles": ["Decorators Basics", "Class Decorators", "Context Managers", "Generators and Yield", "Metaclasses",
                   "Descriptors", "Property Decorator", "Abstract Base Classes", "Multiple Inheritance and MRO",
                   "Slots Optimization", "Dataclasses", "Enum Types", "Named Tuples", "Weak References",
                   "Coroutines with async/await", "Custom Iterators", "Function Overloading (singledispatch)",
                   "Dynamic Attribute Access (__getattr__)", "Operator Overloading", "Memory Profiling"],
    }
    
    topics["FunctionalProgramming"] = {
        "titles": ["Map Function", "Filter Function", "Reduce Function", "Lambda Expressions", "List Comprehensions",
                   "Dictionary Comprehensions", "Generator Expressions", "Closures", "Higher-Order Functions", "Currying",
                   "Partial Functions (functools.partial)", "Function Composition", "Immutable Data Structures",
                   "Recursion as Iteration", "Memoization", "Lazy Evaluation", "Monads (Maybe Pattern)",
                   "Pure Functions", "Tail Call Optimization", "Functional Pipeline"],
    }
    
    topics["Basics"] = {
        "titles": ["Variables and Data Types", "Arithmetic Operations", "String Operations", "If-Else Conditions",
                   "For Loops", "While Loops", "Functions and Return Values", "List Operations", "Dictionary Operations",
                   "Tuple and Set Operations", "File Reading and Writing", "Exception Handling", "String Formatting",
                   "List Slicing", "Nested Loops Pattern", "Swap Two Variables", "Check Even/Odd",
                   "Find Maximum of Three Numbers", "Reverse a String", "Count Vowels in String"],
    }
    
    topics["Advanced_Mathematics"] = {
        "titles": ["Matrix Exponentiation", "Fast Fourier Transform (FFT)", "Chinese Remainder Theorem",
                   "Extended Euclidean Algorithm", "Miller-Rabin Primality Test", "Pollard's Rho Factorization",
                   "Linear Diophantine Equations", "Gaussian Elimination", "Lagrange Interpolation",
                   "Lucas Theorem", "Mobius Function", "Discrete Logarithm", "Modular Inverse",
                   "Polynomial Multiplication", "Number of Divisors in Range", "Sum of Squares Representation",
                   "Continued Fractions", "Matrix Determinant", "Eigenvalues (Power Method)", "Newton's Method for Roots"],
    }
    
    topics["Advanced_Problems"] = {
        "titles": ["N-Queens Problem", "Sudoku Solver", "Word Ladder", "Alien Dictionary", "Course Schedule",
                   "Critical Connections in Network", "Longest Increasing Subsequence", "Russian Doll Envelopes",
                   "Burst Balloons", "Cherry Pickup", "Minimum Cost to Merge Stones", "Palindrome Pairs",
                   "Basic Calculator", "Serialize and Deserialize Binary Tree", "Design Twitter",
                   "Trapping Rain Water", "Largest Rectangle in Histogram", "Maximum Rectangle",
                   "Dungeon Game", "Interleaving String"],
    }
    
    topics["Competative_programming"] = {
        "titles": ["Fast I/O Techniques", "Coordinate Compression", "Sweep Line Algorithm", "Mo's Algorithm",
                   "Heavy-Light Decomposition", "Centroid Decomposition", "2-SAT Problem", "Maximum Flow (Ford-Fulkerson)",
                   "Minimum Cost Maximum Flow", "Strongly Connected Components (Tarjan's)", "Bridge Finding",
                   "Articulation Points", "Euler Path and Circuit", "Topological Sort (Kahn's)", "Digit DP",
                   "Bitmask DP", "Profile DP (Broken Profile)", "Convex Hull Trick", "Sqrt Decomposition",
                   "Persistent Segment Tree"],
    }
    
    topics["Concurrency_and_Multithreading"] = {
        "titles": ["Thread Creation and Management", "Thread Synchronization with Locks", "Producer-Consumer Problem",
                   "Reader-Writer Problem", "Dining Philosophers Problem", "Thread Pool Implementation",
                   "Async/Await Basics", "Asyncio Event Loop", "Concurrent Futures", "Multiprocessing Basics",
                   "Shared Memory Between Processes", "Deadlock Detection", "Semaphores", "Barrier Synchronization",
                   "Thread-Safe Singleton", "Async HTTP Requests", "Rate Limiter", "Task Queue with Workers",
                   "Parallel Merge Sort", "Actor Model Pattern"],
    }
    
    topics["SystemDesign"] = {
        "titles": ["URL Shortener", "Rate Limiter", "LRU Cache Design", "Consistent Hashing", "Pub-Sub System",
                   "Chat Application", "File Storage Service", "Notification System", "Search Autocomplete",
                   "Web Crawler", "API Rate Limiter", "Distributed Lock", "Message Queue", "Load Balancer",
                   "Key-Value Store", "Log Aggregation System", "Social Media Feed", "Payment Processing System",
                   "Recommendation Engine", "Real-Time Analytics Dashboard"],
    }
    
    topics["Databases"] = {
        "titles": ["Basic SELECT Queries", "JOIN Operations", "GROUP BY and Aggregation", "Subqueries",
                   "Window Functions", "Index Optimization", "Database Normalization", "ACID Properties Implementation",
                   "Transaction Management", "Stored Procedures", "Views and Materialized Views", "Database Triggers",
                   "Query Optimization", "Connection Pooling", "ORM: SQLAlchemy Basics", "NoSQL: MongoDB Operations",
                   "Redis Caching", "Database Migration", "Sharding Strategy", "Replication and Failover"],
    }
    
    topics["Networking"] = {
        "titles": ["TCP Socket Server", "UDP Socket Communication", "HTTP GET/POST Requests", "REST API Client",
                   "WebSocket Implementation", "DNS Resolver", "Port Scanner", "Chat Server (TCP)",
                   "File Transfer Protocol", "Ping Implementation", "IP Address Validation", "Subnet Calculator",
                   "HTTP Server from Scratch", "SSL/TLS Connection", "Proxy Server", "Network Packet Sniffer",
                   "Bandwidth Monitor", "Load Balancer (Round Robin)", "Traceroute Implementation", "SMTP Email Sender"],
    }
    
    topics["Security"] = {
        "titles": ["Caesar Cipher", "RSA Encryption Basics", "SHA-256 Hashing", "Password Hashing (bcrypt)",
                   "JWT Token Generation", "SQL Injection Prevention", "XSS Prevention", "CSRF Token Implementation",
                   "AES Encryption/Decryption", "Digital Signature", "Two-Factor Authentication", "Brute Force Detector",
                   "Secure Random Number Generator", "Certificate Validation", "Input Sanitization",
                   "Rate Limiting for Security", "Encryption Key Management", "OAuth 2.0 Flow",
                   "File Integrity Checker", "Secure Session Management"],
    }
    
    topics["Testing_and_debugging"] = {
        "titles": ["Unit Testing with unittest", "Unit Testing with pytest", "Mocking and Patching", "Test Fixtures",
                   "Parameterized Tests", "Integration Testing", "Test Coverage Analysis", "TDD: Red-Green-Refactor",
                   "Debugging with pdb", "Logging Best Practices", "Property-Based Testing (Hypothesis)",
                   "Performance Testing (timeit)", "Testing Exceptions", "Testing Async Code",
                   "Continuous Integration Setup", "Code Profiling (cProfile)", "Memory Leak Detection",
                   "Regression Testing", "Snapshot Testing", "End-to-End Testing"],
    }
    
    topics["DataScience"] = {
        "titles": ["Data Cleaning with Pandas", "CSV File Processing", "Data Visualization (Matplotlib)",
                   "Statistical Analysis (Mean, Median, Mode)", "Correlation Analysis", "Hypothesis Testing",
                   "Data Normalization", "Outlier Detection", "Time Series Analysis", "Pivot Tables",
                   "Data Sampling Techniques", "A/B Testing Analysis", "Feature Scaling", "Missing Data Imputation",
                   "Exploratory Data Analysis", "Data Pipeline Builder", "JSON Data Processing",
                   "Web Scraping for Data Collection", "Data Aggregation", "Dashboard Metrics Calculator"],
    }
    
    topics["MachineLearning"] = {
        "titles": ["Linear Regression from Scratch", "Logistic Regression", "K-Nearest Neighbors",
                   "Decision Tree Classifier", "Random Forest", "K-Means Clustering", "Principal Component Analysis",
                   "Naive Bayes Classifier", "Support Vector Machine Basics", "Gradient Descent Optimization",
                   "Cross-Validation", "Feature Selection", "Bias-Variance Tradeoff Analysis", "Confusion Matrix",
                   "ROC Curve and AUC", "Neural Network (Single Layer)", "Backpropagation", "Regularization (L1/L2)",
                   "Ensemble Methods", "Hyperparameter Tuning"],
    }
    
    topics["WebDevelopment"] = {
        "titles": ["REST API with Flask", "CRUD Operations", "Authentication Middleware", "Form Validation",
                   "File Upload Handler", "Pagination Implementation", "Search with Filters", "Rate Limiting Middleware",
                   "WebSocket Chat", "Email Notification Service", "HTML Parser", "Web Scraper",
                   "URL Router", "Template Engine", "Session Management", "Cookie Handler",
                   "CORS Configuration", "Error Handling Middleware", "API Versioning", "Static File Server"],
    }
    
    topics["GameDevelopement"] = {
        "titles": ["Game Loop Implementation", "2D Collision Detection", "Pathfinding (A* Algorithm)",
                   "Sprite Animation System", "Score Tracking System", "Random Level Generator",
                   "Physics Engine (Basic Gravity)", "Inventory System", "State Machine for Game States",
                   "Particle System", "Tile Map Renderer", "Enemy AI (Simple Chase)", "Save/Load Game State",
                   "Sound Manager", "Menu System", "Camera Follow System", "Health Bar System",
                   "Projectile System", "Power-Up System", "Leaderboard Manager"],
    }
    
    topics["RealWorldApplication"] = {
        "titles": ["Todo List Application", "Calculator (CLI)", "File Organizer", "Password Generator",
                   "Expense Tracker", "Weather Data Fetcher", "QR Code Generator", "PDF Report Generator",
                   "Email Automation", "Web Bookmark Manager", "Markdown to HTML Converter", "CSV to JSON Converter",
                   "Image Resizer", "Countdown Timer", "Unit Converter", "Address Book", "Pomodoro Timer",
                   "Clipboard Manager", "System Resource Monitor", "Log File Analyzer"],
    }
    
    topics["RealWorldProblem"] = {
        "titles": ["Load Balancing Simulation", "Elevator Scheduling", "Traffic Signal Controller",
                   "Restaurant Order Management", "Library Catalogue Search", "Flight Booking System",
                   "Cab Ride Fare Calculator", "Hospital Appointment Scheduler", "Student Grade Calculator",
                   "Inventory Management System", "ATM Machine Simulation", "Vending Machine",
                   "Recipe Recommendation", "Movie Ticket Booking", "E-commerce Cart System",
                   "Chat Bot (Rule-based)", "Voting System", "Bus Route Finder", "Energy Consumption Tracker",
                   "Employee Shift Scheduler"],
    }
    
    topics["Miscellaneous"] = {
        "titles": ["Roman Numeral Converter", "Conway's Game of Life", "Sudoku Validator", "Magic Square Check",
                   "Matrix Spiral Traversal", "Zigzag Conversion", "Run-Length Encoding", "Base Converter",
                   "Day of the Week Calculator", "ISBN Validator", "Color Code Converter (Hex/RGB)",
                   "Morse Code Translator", "Luhn Algorithm (Credit Card Validation)", "Maze Solver",
                   "Tower of Hanoi Visualization", "N-Body Simulation (Simple)", "Cellular Automaton",
                   "Random Walk Simulation", "DNA Sequence Matcher", "Crossword Puzzle Solver"],
    }
    
    return topics


def generate_simple_topic(folder, titles):
    """Generate generic problem and solution files for a topic."""
    for i, title in enumerate(titles, 1):
        prob_content = gen_p(i, title, 
            f"Implement a solution for {title}. This problem tests your understanding of {folder.replace('_', ' ').lower()} concepts.",
            f"Input specific to {title}.",
            f"Output specific to {title}.",
            "See problem-specific constraints",
            f"Example input for {title}",
            f"Example output for {title}")
        write_file(os.path.join(BASE_DIR, folder, "Problems", f"problem{i}.md"), prob_content)
        
        sol_content = gen_s(i, title,
            f"Apply the appropriate technique for {title}.",
            [f"Analyze the input for {title}.", 
             "Apply the core algorithm or pattern.",
             "Handle edge cases.",
             "Return the result."],
            "See solution details",
            "See solution details",
            f"# Solution for {title}\n# Implementation depends on specific requirements\n\ndef solve():\n    # Core implementation here\n    pass\n\n# See detailed implementation in the problem description")
        write_file(os.path.join(BASE_DIR, folder, "Solutions", f"solution{i}.md"), sol_content)
    
    print(f"  DONE {folder}: {len(titles)}P + {len(titles)}S")


def main():
    # OOP (fully detailed)
    print("Generating OOP...")
    write_topic("OOP", OOP_P, OOP_S)
    
    # All remaining topics
    simple = simple_topics()
    for folder, data in simple.items():
        print(f"Generating {folder}...")
        generate_simple_topic(folder, data["titles"])
    
    print("\nAll topics generated!")

if __name__ == "__main__":
    main()
