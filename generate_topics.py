"""
Script to generate Problems and Solutions for all remaining empty topic folders.
"""
import os

BASE_DIR = r"d:\500DCPP"

# Define all remaining topics with their problems and solutions
TOPICS = {
    "Matchematical_problem": {
        "problems": [
            ("GCD and LCM", "Given two integers `a` and `b`, find their Greatest Common Divisor (GCD) and Least Common Multiple (LCM).", "Two integers `a` and `b`.", "A tuple `(gcd, lcm)`.", "1 <= a, b <= 10^9", "a = 12, b = 18", "(6, 36)"),
            ("Sieve of Eratosthenes", "Find all prime numbers less than or equal to `n` using the Sieve of Eratosthenes.", "An integer `n`.", "A list of prime numbers.", "2 <= n <= 10^7", "n = 30", "[2, 3, 5, 7, 11, 13, 17, 19, 23, 29]"),
            ("Check Prime Number", "Given an integer `n`, determine if it is a prime number.", "An integer `n`.", "A boolean.", "1 <= n <= 10^9", "n = 29", "True"),
            ("Fibonacci Number", "Find the nth Fibonacci number. F(0)=0, F(1)=1, F(n)=F(n-1)+F(n-2).", "An integer `n`.", "An integer — the nth Fibonacci number.", "0 <= n <= 45", "n = 10", "55"),
            ("Power Modular Exponentiation", "Compute `(base^exp) % mod` efficiently using modular exponentiation.", "Three integers `base`, `exp`, `mod`.", "An integer.", "1 <= base, exp, mod <= 10^9", "base=2, exp=10, mod=1000", "24"),
            ("Factorial Trailing Zeros", "Given an integer `n`, return the number of trailing zeros in `n!`.", "An integer `n`.", "An integer.", "0 <= n <= 10^4", "n = 25", "6"),
            ("Count Digits in Factorial", "Find the number of digits in `n!`.", "An integer `n`.", "An integer — number of digits.", "1 <= n <= 10^6", "n = 100", "158"),
            ("Catalan Number", "Find the nth Catalan number.", "An integer `n`.", "An integer — the nth Catalan number.", "0 <= n <= 20", "n = 5", "42"),
            ("Pascal's Triangle", "Generate the first `n` rows of Pascal's triangle.", "An integer `n`.", "A list of lists.", "1 <= n <= 30", "n = 5", "[[1],[1,1],[1,2,1],[1,3,3,1],[1,4,6,4,1]]"),
            ("nCr (Binomial Coefficient)", "Compute the binomial coefficient C(n, r).", "Two integers `n` and `r`.", "An integer.", "0 <= r <= n <= 1000", "n=5, r=2", "10"),
            ("Check Perfect Number", "Determine if a number is perfect (sum of proper divisors equals the number).", "An integer `n`.", "A boolean.", "1 <= n <= 10^8", "n = 28", "True (1+2+4+7+14=28)"),
            ("Sum of Divisors", "Find the sum of all divisors of `n`.", "An integer `n`.", "An integer.", "1 <= n <= 10^6", "n = 12", "28 (1+2+3+4+6+12)"),
            ("Euler's Totient Function", "Compute Euler's totient function φ(n) — count of integers from 1 to n that are coprime with n.", "An integer `n`.", "An integer.", "1 <= n <= 10^6", "n = 10", "4"),
            ("Integer to Roman", "Convert an integer to its Roman numeral representation.", "An integer `num`.", "A string.", "1 <= num <= 3999", "num = 1994", "'MCMXCIV'"),
            ("Roman to Integer", "Convert a Roman numeral string to an integer.", "A string `s`.", "An integer.", "Valid Roman numeral, 1 <= result <= 3999", "s = 'MCMXCIV'", "1994"),
            ("Happy Number", "Determine if a number is happy. Replace the number by the sum of squares of its digits repeatedly. If it reaches 1, it's happy.", "An integer `n`.", "A boolean.", "1 <= n <= 2^31 - 1", "n = 19", "True"),
            ("Ugly Number", "Check if a number is ugly (prime factors only include 2, 3, 5).", "An integer `n`.", "A boolean.", "-2^31 <= n <= 2^31 - 1", "n = 6", "True"),
            ("Nth Ugly Number", "Find the nth ugly number (1 is the first ugly number).", "An integer `n`.", "An integer.", "1 <= n <= 1690", "n = 10", "12"),
            ("Armstrong Number", "Check if a number is an Armstrong number (sum of cubes of digits equals the number for 3-digit numbers, generalized for k-digit).", "An integer `n`.", "A boolean.", "1 <= n <= 10^9", "n = 153", "True (1³+5³+3³=153)"),
            ("Excel Sheet Column Number", "Convert an Excel column title to its corresponding column number. A=1, B=2, ..., Z=26, AA=27.", "A string `columnTitle`.", "An integer.", "1 <= len(columnTitle) <= 7", "columnTitle = 'AB'", "28"),
        ],
        "solutions": [
            ("GCD and LCM", "Use Euclid's algorithm for GCD. LCM = (a * b) / GCD(a, b).", ["Compute GCD using Euclid's algorithm: gcd(a, b) = gcd(b, a%b).", "Compute LCM = a * b // gcd."], "O(log(min(a,b)))", "O(1)",
             """import math

def gcd_lcm(a, b):
    g = math.gcd(a, b)
    l = a * b // g
    return (g, l)"""),
            ("Sieve of Eratosthenes", "Create a boolean array of size n+1. Mark multiples of each prime as composite.", ["Initialize all as prime.", "For each number from 2 to √n, mark its multiples.", "Collect remaining primes."], "O(N log log N)", "O(N)",
             """def sieve(n):
    is_prime = [True] * (n + 1)
    is_prime[0] = is_prime[1] = False
    for i in range(2, int(n**0.5) + 1):
        if is_prime[i]:
            for j in range(i*i, n + 1, i):
                is_prime[j] = False
    return [i for i in range(2, n + 1) if is_prime[i]]"""),
            ("Check Prime Number", "Check divisibility up to √n. If no divisor found, the number is prime.", ["Handle edge cases: n < 2 is not prime.", "Check divisibility from 2 to √n.", "If no divisor found, return True."], "O(√N)", "O(1)",
             """def is_prime(n):
    if n < 2:
        return False
    if n < 4:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True"""),
            ("Fibonacci Number", "Use iterative approach with two variables to avoid exponential recursion.", ["Initialize a=0, b=1.", "Iterate n times, updating a and b.", "Return a."], "O(N)", "O(1)",
             """def fibonacci(n):
    if n <= 1:
        return n
    a, b = 0, 1
    for _ in range(2, n + 1):
        a, b = b, a + b
    return b"""),
            ("Power Modular Exponentiation", "Use binary exponentiation: square the base and halve the exponent at each step.", ["If exp is odd, multiply result by base.", "Square base, halve exponent.", "Apply mod at each step."], "O(log N)", "O(1)",
             """def power_mod(base, exp, mod):
    result = 1
    base %= mod
    while exp > 0:
        if exp % 2 == 1:
            result = (result * base) % mod
        exp //= 2
        base = (base * base) % mod
    return result"""),
            ("Factorial Trailing Zeros", "Count factors of 5 in n!. Every pair of 2 and 5 contributes a trailing zero, and 2s are always more plentiful.", ["Count = n//5 + n//25 + n//125 + ...", "Keep dividing n by 5 and adding."], "O(log N)", "O(1)",
             """def trailing_zeros(n):
    count = 0
    while n >= 5:
        n //= 5
        count += n
    return count"""),
            ("Count Digits in Factorial", "Use Kamenetsky's formula: digits ≈ log10(n!) = Σlog10(i) for i=1..n, or use Stirling's approx.", ["Sum log10(i) for i from 1 to n.", "Return floor(sum) + 1."], "O(N)", "O(1)",
             """import math

def count_digits_factorial(n):
    if n <= 1:
        return 1
    digits = 0
    for i in range(2, n + 1):
        digits += math.log10(i)
    return int(digits) + 1"""),
            ("Catalan Number", "Use DP: C(n) = Σ C(i)*C(n-1-i) for i=0..n-1.", ["Initialize dp[0] = dp[1] = 1.", "For each n, compute sum of dp[i]*dp[n-1-i].", "Return dp[n]."], "O(N²)", "O(N)",
             """def catalan(n):
    dp = [0] * (n + 1)
    dp[0] = dp[1] = 1
    for i in range(2, n + 1):
        for j in range(i):
            dp[i] += dp[j] * dp[i - 1 - j]
    return dp[n]"""),
            ("Pascal's Triangle", "Each element is the sum of the two elements above it. Edge elements are 1.", ["Create rows iteratively.", "Each row starts and ends with 1.", "Inner elements = sum of two above."], "O(N²)", "O(N²)",
             """def generate_pascal(n):
    triangle = []
    for i in range(n):
        row = [1] * (i + 1)
        for j in range(1, i):
            row[j] = triangle[i-1][j-1] + triangle[i-1][j]
        triangle.append(row)
    return triangle"""),
            ("nCr (Binomial Coefficient)", "Use DP table or the multiplicative formula: C(n,r) = n!/(r!*(n-r)!).", ["Use iterative multiplication to avoid overflow.", "C(n,r) = C(n,n-r) for optimization."], "O(R)", "O(1)",
             """def ncr(n, r):
    if r > n - r:
        r = n - r
    result = 1
    for i in range(r):
        result = result * (n - i) // (i + 1)
    return result"""),
            ("Check Perfect Number", "Find all divisors up to √n and check if their sum equals n.", ["Iterate from 1 to √n.", "Add both divisor and n/divisor.", "Check if sum equals n."], "O(√N)", "O(1)",
             """def is_perfect(n):
    if n <= 1:
        return False
    div_sum = 1
    i = 2
    while i * i <= n:
        if n % i == 0:
            div_sum += i
            if i != n // i:
                div_sum += n // i
        i += 1
    return div_sum == n"""),
            ("Sum of Divisors", "Iterate to √n, adding both divisor and its complement.", ["For each i from 1 to √n, if n%i==0, add i and n//i.", "Handle perfect square case."], "O(√N)", "O(1)",
             """def sum_of_divisors(n):
    total = 0
    i = 1
    while i * i <= n:
        if n % i == 0:
            total += i
            if i != n // i:
                total += n // i
        i += 1
    return total"""),
            ("Euler's Totient Function", "Use the formula: φ(n) = n * Π(1 - 1/p) for each prime factor p of n.", ["Start with result = n.", "For each prime factor p, multiply result by (1 - 1/p).", "Handle repeated factors."], "O(√N)", "O(1)",
             """def euler_totient(n):
    result = n
    p = 2
    while p * p <= n:
        if n % p == 0:
            while n % p == 0:
                n //= p
            result -= result // p
        p += 1
    if n > 1:
        result -= result // n
    return result"""),
            ("Integer to Roman", "Map values to symbols. Greedily subtract the largest value and append its symbol.", ["Define value-symbol pairs in descending order.", "For each pair, repeatedly subtract and append."], "O(1)", "O(1)",
             """def int_to_roman(num):
    val_sym = [(1000,'M'),(900,'CM'),(500,'D'),(400,'CD'),
               (100,'C'),(90,'XC'),(50,'L'),(40,'XL'),
               (10,'X'),(9,'IX'),(5,'V'),(4,'IV'),(1,'I')]
    result = ''
    for val, sym in val_sym:
        while num >= val:
            result += sym
            num -= val
    return result"""),
            ("Roman to Integer", "Process right to left. If current value < next value, subtract it; otherwise add it.", ["Map symbols to values.", "Iterate right to left, comparing with previous."], "O(N)", "O(1)",
             """def roman_to_int(s):
    roman = {'I':1,'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000}
    result = 0
    prev = 0
    for ch in reversed(s):
        curr = roman[ch]
        if curr < prev:
            result -= curr
        else:
            result += curr
        prev = curr
    return result"""),
            ("Happy Number", "Use Floyd's cycle detection (fast/slow pointers) on the digit-square-sum sequence.", ["Compute digit square sum repeatedly.", "If it reaches 1, return True.", "If cycle detected without reaching 1, return False."], "O(log N)", "O(1)",
             """def is_happy(n):
    def digit_sum(num):
        total = 0
        while num:
            total += (num % 10) ** 2
            num //= 10
        return total
    
    slow = n
    fast = digit_sum(n)
    while fast != 1 and slow != fast:
        slow = digit_sum(slow)
        fast = digit_sum(digit_sum(fast))
    return fast == 1"""),
            ("Ugly Number", "Repeatedly divide by 2, 3, 5. If result is 1, it's ugly.", ["If n <= 0, return False.", "Divide by 2, 3, 5 while divisible.", "Check if result is 1."], "O(log N)", "O(1)",
             """def is_ugly(n):
    if n <= 0:
        return False
    for factor in [2, 3, 5]:
        while n % factor == 0:
            n //= factor
    return n == 1"""),
            ("Nth Ugly Number", "Use three pointers for multiples of 2, 3, and 5. Always pick the minimum.", ["Maintain dp array and three pointers i2, i3, i5.", "Next ugly = min(dp[i2]*2, dp[i3]*3, dp[i5]*5).", "Advance the corresponding pointer(s)."], "O(N)", "O(N)",
             """def nth_ugly(n):
    dp = [0] * n
    dp[0] = 1
    i2 = i3 = i5 = 0
    for i in range(1, n):
        next2, next3, next5 = dp[i2]*2, dp[i3]*3, dp[i5]*5
        dp[i] = min(next2, next3, next5)
        if dp[i] == next2: i2 += 1
        if dp[i] == next3: i3 += 1
        if dp[i] == next5: i5 += 1
    return dp[n-1]"""),
            ("Armstrong Number", "Sum the kth power of each digit (k = number of digits). Compare with original.", ["Count digits k.", "Sum each digit raised to power k.", "Compare with original."], "O(k) where k is number of digits", "O(1)",
             """def is_armstrong(n):
    digits = str(n)
    k = len(digits)
    return sum(int(d)**k for d in digits) == n"""),
            ("Excel Sheet Column Number", "Treat as base-26 number where A=1, B=2, ..., Z=26.", ["Initialize result = 0.", "For each character: result = result * 26 + (ord(ch) - ord('A') + 1).", "Return result."], "O(N)", "O(1)",
             """def title_to_number(columnTitle):
    result = 0
    for ch in columnTitle:
        result = result * 26 + (ord(ch) - ord('A') + 1)
    return result"""),
        ]
    },
    "GeomatricalProblem": {
        "problems": [
            ("Point in Triangle", "Given three vertices of a triangle and a point P, check if P lies inside the triangle.", "Four points (x,y).", "A boolean.", "Coordinates are integers, -10^4 <= x,y <= 10^4", "Triangle: (0,0),(10,30),(20,0), P=(10,15)", "True"),
            ("Area of Triangle", "Given three vertices, compute the area of the triangle.", "Three points (x,y).", "A float — area.", "-10^4 <= x,y <= 10^4", "Points: (0,0),(4,0),(0,3)", "6.0"),
            ("Convex Hull (Graham Scan)", "Given a set of points, find the convex hull using Graham Scan algorithm.", "A list of points (x,y).", "A list of points forming the convex hull.", "3 <= n <= 10^5", "points = [(0,3),(1,1),(2,2),(4,4),(0,0),(1,2),(3,1),(3,3)]", "[(0,0),(3,1),(4,4),(0,3)]"),
            ("Check Collinear Points", "Given three points, check if they are collinear.", "Three points (x,y).", "A boolean.", "-10^4 <= x,y <= 10^4", "Points: (1,1),(2,2),(3,3)", "True"),
            ("Distance Between Two Points", "Compute the Euclidean distance between two points in 2D space.", "Two points (x1,y1) and (x2,y2).", "A float.", "-10^6 <= x,y <= 10^6", "P1=(1,2), P2=(4,6)", "5.0"),
            ("Line Intersection", "Given two line segments, determine if they intersect and find the intersection point.", "Four points defining two line segments.", "Intersection point or None.", "-10^4 <= x,y <= 10^4", "Lines: (1,1)-(4,4) and (1,8)-(2,4)", "Intersection point"),
            ("Circle-Line Intersection", "Find the intersection points of a line and a circle.", "Circle center (cx,cy), radius r, line defined by two points.", "List of intersection points.", "-10^4 <= coordinates <= 10^4", "Circle:(0,0,5), Line:(0,0)-(5,0)", "[(5,0),(-5,0)]"),
            ("Polygon Area (Shoelace Formula)", "Compute the area of a polygon given its vertices using the Shoelace formula.", "A list of vertices in order.", "A float — area.", "3 <= n <= 10^4", "vertices = [(0,0),(4,0),(4,3),(0,3)]", "12.0"),
            ("Point in Polygon (Ray Casting)", "Determine if a point lies inside a polygon using the ray casting algorithm.", "A polygon (list of vertices) and a point.", "A boolean.", "3 <= vertices <= 10^4", "Polygon: [(0,0),(10,0),(10,10),(0,10)], P=(5,5)", "True"),
            ("Closest Pair of Points (Brute)", "Find the closest pair of points in O(n²) time.", "A list of points.", "A float — minimum distance.", "2 <= n <= 10^4", "points = [(1,1),(2,2),(3,3),(1,2)]", "1.0"),
            ("Check if Point is on Line Segment", "Given a line segment AB and point P, check if P lies on segment AB.", "Three points A, B, P.", "A boolean.", "-10^4 <= coordinates <= 10^4", "A=(0,0), B=(4,4), P=(2,2)", "True"),
            ("Angle Between Two Vectors", "Compute the angle (in degrees) between two 2D vectors.", "Two vectors (x1,y1) and (x2,y2).", "A float — angle in degrees.", "-10^6 <= components <= 10^6", "v1=(1,0), v2=(0,1)", "90.0"),
            ("Rotate Point Around Origin", "Rotate a point by a given angle θ (in degrees) around the origin.", "A point (x,y) and angle θ.", "Rotated point (x',y').", "-10^4 <= x,y <= 10^4", "Point=(1,0), θ=90°", "(0,1)"),
            ("Check Rectangle Overlap", "Given two axis-aligned rectangles, check if they overlap.", "Two rectangles as [x1,y1,x2,y2].", "A boolean.", "-10^9 <= coordinates <= 10^9", "R1=[0,0,2,2], R2=[1,1,3,3]", "True"),
            ("Perimeter of Polygon", "Compute the perimeter of a polygon given its vertices.", "A list of vertices.", "A float — perimeter.", "3 <= n <= 10^4", "vertices = [(0,0),(3,0),(3,4)]", "12.0"),
            ("Minimum Enclosing Circle", "Find the smallest circle that encloses all given points.", "A list of points.", "Center and radius of the circle.", "1 <= n <= 10^5", "points = [(0,0),(1,0),(0,1)]", "Center≈(0.5,0.5), r≈0.707"),
            ("Reflect Point Over Line", "Reflect a point over a given line (ax + by + c = 0).", "Point (x,y) and line coefficients a, b, c.", "Reflected point.", "-10^4 <= values <= 10^4", "Point=(1,1), Line: x-y=0", "(1,1) (on the line)"),
            ("Check if Points Form Square", "Given four points, check if they form a perfect square.", "Four points.", "A boolean.", "-10^4 <= coordinates <= 10^4", "Points: (0,0),(1,0),(1,1),(0,1)", "True"),
            ("Lattice Points on Line Segment", "Count the number of lattice (integer) points on a line segment between two points.", "Two points (x1,y1) and (x2,y2).", "An integer.", "-10^6 <= coordinates <= 10^6", "P1=(1,1), P2=(5,5)", "5"),
            ("Maximum Points on a Line", "Given a set of points, find the maximum number of points that lie on the same line.", "A list of points.", "An integer.", "1 <= n <= 300", "points = [(1,1),(2,2),(3,3),(1,2)]", "3"),
        ],
        "solutions": [
            ("Point in Triangle", "Use area method: if Area(PAB) + Area(PBC) + Area(PCA) == Area(ABC), point is inside.", ["Compute area of triangle ABC.", "Compute areas of PAB, PBC, PCA.", "Check if sum equals ABC area."], "O(1)", "O(1)",
             """def point_in_triangle(p, a, b, c):
    def area(p1, p2, p3):
        return abs((p1[0]*(p2[1]-p3[1]) + p2[0]*(p3[1]-p1[1]) + p3[0]*(p1[1]-p2[1])) / 2.0)
    
    A = area(a, b, c)
    A1 = area(p, b, c)
    A2 = area(a, p, c)
    A3 = area(a, b, p)
    
    return abs(A - (A1 + A2 + A3)) < 1e-9"""),
            ("Area of Triangle", "Use the Shoelace formula: Area = |x1(y2-y3) + x2(y3-y1) + x3(y1-y2)| / 2.", ["Plug coordinates into the formula.", "Take absolute value and divide by 2."], "O(1)", "O(1)",
             """def triangle_area(p1, p2, p3):
    return abs(p1[0]*(p2[1]-p3[1]) + p2[0]*(p3[1]-p1[1]) + p3[0]*(p1[1]-p2[1])) / 2.0"""),
            ("Convex Hull (Graham Scan)", "Find the bottom-most point, sort by polar angle, and process points maintaining a left-turn stack.", ["Find anchor point.", "Sort remaining by polar angle.", "Process with stack, maintaining convexity."], "O(N log N)", "O(N)",
             """def convex_hull(points):
    def cross(o, a, b):
        return (a[0]-o[0])*(b[1]-o[1]) - (a[1]-o[1])*(b[0]-o[0])
    
    points = sorted(set(points))
    if len(points) <= 1:
        return points
    
    lower = []
    for p in points:
        while len(lower) >= 2 and cross(lower[-2], lower[-1], p) <= 0:
            lower.pop()
        lower.append(p)
    
    upper = []
    for p in reversed(points):
        while len(upper) >= 2 and cross(upper[-2], upper[-1], p) <= 0:
            upper.pop()
        upper.append(p)
    
    return lower[:-1] + upper[:-1]"""),
            ("Check Collinear Points", "Three points are collinear if the area of triangle they form is 0.", ["Compute cross product (or area).", "If zero, points are collinear."], "O(1)", "O(1)",
             """def are_collinear(p1, p2, p3):
    return (p2[0]-p1[0])*(p3[1]-p1[1]) - (p3[0]-p1[0])*(p2[1]-p1[1]) == 0"""),
            ("Distance Between Two Points", "Use the Euclidean distance formula: √((x2-x1)² + (y2-y1)²).", ["Compute differences.", "Square, sum, take square root."], "O(1)", "O(1)",
             """import math
def distance(p1, p2):
    return math.sqrt((p2[0]-p1[0])**2 + (p2[1]-p1[1])**2)"""),
            ("Line Intersection", "Use parametric form and solve the system of equations. Check if parameters are within [0,1] for segments.", ["Express lines parametrically.", "Solve for parameters using cross products.", "Check bounds."], "O(1)", "O(1)",
             """def line_intersection(p1, p2, p3, p4):
    d = (p1[0]-p2[0])*(p3[1]-p4[1]) - (p1[1]-p2[1])*(p3[0]-p4[0])
    if d == 0:
        return None  # Parallel
    t = ((p1[0]-p3[0])*(p3[1]-p4[1]) - (p1[1]-p3[1])*(p3[0]-p4[0])) / d
    x = p1[0] + t*(p2[0]-p1[0])
    y = p1[1] + t*(p2[1]-p1[1])
    return (x, y)"""),
            ("Circle-Line Intersection", "Substitute line equation into circle equation and solve the resulting quadratic.", ["Set up quadratic equation.", "Compute discriminant.", "Find intersection points if discriminant >= 0."], "O(1)", "O(1)",
             """import math
def circle_line_intersect(cx, cy, r, p1, p2):
    dx, dy = p2[0]-p1[0], p2[1]-p1[1]
    fx, fy = p1[0]-cx, p1[1]-cy
    a = dx*dx + dy*dy
    b = 2*(fx*dx + fy*dy)
    c = fx*fx + fy*fy - r*r
    disc = b*b - 4*a*c
    if disc < 0: return []
    disc = math.sqrt(disc)
    t1 = (-b - disc) / (2*a)
    t2 = (-b + disc) / (2*a)
    pts = []
    for t in [t1, t2]:
        pts.append((p1[0]+t*dx, p1[1]+t*dy))
    return pts"""),
            ("Polygon Area (Shoelace Formula)", "Sum cross products of consecutive vertices and take half the absolute value.", ["Apply Shoelace formula.", "Sum x_i*y_{i+1} - x_{i+1}*y_i.", "Return absolute value / 2."], "O(N)", "O(1)",
             """def polygon_area(vertices):
    n = len(vertices)
    area = 0
    for i in range(n):
        j = (i + 1) % n
        area += vertices[i][0] * vertices[j][1]
        area -= vertices[j][0] * vertices[i][1]
    return abs(area) / 2.0"""),
            ("Point in Polygon (Ray Casting)", "Cast a ray from the point and count intersections with polygon edges. Odd count means inside.", ["Cast horizontal ray to the right.", "Count edge crossings.", "Odd = inside, even = outside."], "O(N)", "O(1)",
             """def point_in_polygon(polygon, point):
    n = len(polygon)
    inside = False
    x, y = point
    j = n - 1
    for i in range(n):
        xi, yi = polygon[i]
        xj, yj = polygon[j]
        if ((yi > y) != (yj > y)) and (x < (xj-xi)*(y-yi)/(yj-yi)+xi):
            inside = not inside
        j = i
    return inside"""),
            ("Closest Pair of Points (Brute)", "Check all pairs and track the minimum distance.", ["Double loop over all pairs.", "Compute distance for each pair.", "Track minimum."], "O(N²)", "O(1)",
             """import math
def closest_pair_brute(points):
    min_dist = float('inf')
    for i in range(len(points)):
        for j in range(i+1, len(points)):
            d = math.sqrt((points[i][0]-points[j][0])**2 + (points[i][1]-points[j][1])**2)
            min_dist = min(min_dist, d)
    return min_dist"""),
            ("Check if Point is on Line Segment", "Check if point is collinear with endpoints and lies within the bounding box.", ["Check collinearity using cross product.", "Check bounding box constraints."], "O(1)", "O(1)",
             """def on_segment(a, b, p):
    cross = (b[0]-a[0])*(p[1]-a[1]) - (b[1]-a[1])*(p[0]-a[0])
    if abs(cross) > 1e-9:
        return False
    return min(a[0],b[0]) <= p[0] <= max(a[0],b[0]) and min(a[1],b[1]) <= p[1] <= max(a[1],b[1])"""),
            ("Angle Between Two Vectors", "Use dot product formula: cos(θ) = (v1·v2) / (|v1|*|v2|).", ["Compute dot product.", "Compute magnitudes.", "Apply arccos."], "O(1)", "O(1)",
             """import math
def angle_between(v1, v2):
    dot = v1[0]*v2[0] + v1[1]*v2[1]
    mag1 = math.sqrt(v1[0]**2 + v1[1]**2)
    mag2 = math.sqrt(v2[0]**2 + v2[1]**2)
    cos_angle = dot / (mag1 * mag2)
    cos_angle = max(-1, min(1, cos_angle))
    return math.degrees(math.acos(cos_angle))"""),
            ("Rotate Point Around Origin", "Apply rotation matrix: x'=x*cos(θ)-y*sin(θ), y'=x*sin(θ)+y*cos(θ).", ["Convert angle to radians.", "Apply rotation formulas.", "Return new coordinates."], "O(1)", "O(1)",
             """import math
def rotate_point(x, y, angle_deg):
    angle = math.radians(angle_deg)
    x_new = x * math.cos(angle) - y * math.sin(angle)
    y_new = x * math.sin(angle) + y * math.cos(angle)
    return (round(x_new, 10), round(y_new, 10))"""),
            ("Check Rectangle Overlap", "Two rectangles don't overlap if one is above, below, left, or right of the other.", ["Check non-overlap conditions.", "Return negation."], "O(1)", "O(1)",
             """def is_overlap(r1, r2):
    # r = [x1, y1, x2, y2]
    if r1[0] >= r2[2] or r2[0] >= r1[2]:
        return False
    if r1[1] >= r2[3] or r2[1] >= r1[3]:
        return False
    return True"""),
            ("Perimeter of Polygon", "Sum distances between consecutive vertices (including last to first).", ["Iterate through vertices.", "Add distance between consecutive pairs.", "Include closing edge."], "O(N)", "O(1)",
             """import math
def polygon_perimeter(vertices):
    n = len(vertices)
    perimeter = 0
    for i in range(n):
        j = (i + 1) % n
        perimeter += math.sqrt((vertices[j][0]-vertices[i][0])**2 + (vertices[j][1]-vertices[i][1])**2)
    return perimeter"""),
            ("Minimum Enclosing Circle", "Use Welzl's randomized algorithm. Process points recursively, maintaining up to 3 boundary points.", ["Shuffle points randomly.", "Recursively add points.", "If point outside current circle, include it on boundary."], "O(N) expected", "O(N)",
             """import math, random
def min_enclosing_circle(points):
    def circle_from_1(p):
        return (p[0], p[1], 0)
    def circle_from_2(p1, p2):
        cx = (p1[0]+p2[0])/2
        cy = (p1[1]+p2[1])/2
        r = math.sqrt((p1[0]-p2[0])**2+(p1[1]-p2[1])**2)/2
        return (cx, cy, r)
    def is_inside(c, p):
        return math.sqrt((c[0]-p[0])**2+(c[1]-p[1])**2) <= c[2]+1e-7
    # Simplified for small inputs
    random.shuffle(points)
    c = circle_from_1(points[0])
    for i in range(1, len(points)):
        if not is_inside(c, points[i]):
            c = circle_from_2(points[0], points[i])
            for j in range(1, i):
                if not is_inside(c, points[j]):
                    c = circle_from_2(points[j], points[i])
    return c"""),
            ("Reflect Point Over Line", "Use the reflection formula for point over line ax+by+c=0.", ["Compute d = (ax+by+c)/(a²+b²).", "x' = x - 2ad, y' = y - 2bd."], "O(1)", "O(1)",
             """def reflect_point(x, y, a, b, c):
    d = (a*x + b*y + c) / (a*a + b*b)
    x_ref = x - 2*a*d
    y_ref = y - 2*b*d
    return (x_ref, y_ref)"""),
            ("Check if Points Form Square", "Compute all 6 pairwise distances. A square has 4 equal sides and 2 equal (longer) diagonals.", ["Compute all 6 distances.", "Sort them.", "First 4 should be equal (sides), last 2 equal (diagonals)."], "O(1)", "O(1)",
             """import math
def is_square(p1, p2, p3, p4):
    def dist_sq(a, b):
        return (a[0]-b[0])**2 + (a[1]-b[1])**2
    points = [p1, p2, p3, p4]
    dists = sorted([dist_sq(points[i], points[j]) for i in range(4) for j in range(i+1, 4)])
    return dists[0] > 0 and dists[0]==dists[1]==dists[2]==dists[3] and dists[4]==dists[5]"""),
            ("Lattice Points on Line Segment", "Count = GCD(|x2-x1|, |y2-y1|) + 1.", ["Compute absolute differences.", "Find GCD.", "Return GCD + 1."], "O(log(max(dx,dy)))", "O(1)",
             """import math
def lattice_points(x1, y1, x2, y2):
    return math.gcd(abs(x2-x1), abs(y2-y1)) + 1"""),
            ("Maximum Points on a Line", "For each point, compute slopes to all other points using a hash map. Track the maximum.", ["For each point, compute slope (as fraction) to all others.", "Use a dictionary to count collinear points.", "Track global maximum."], "O(N²)", "O(N)",
             """from collections import defaultdict
import math

def max_points(points):
    if len(points) <= 2:
        return len(points)
    
    max_count = 2
    for i in range(len(points)):
        slopes = defaultdict(int)
        for j in range(len(points)):
            if i == j:
                continue
            dx = points[j][0] - points[i][0]
            dy = points[j][1] - points[i][1]
            g = math.gcd(abs(dx), abs(dy))
            if g:
                dx, dy = dx//g, dy//g
            if dx < 0:
                dx, dy = -dx, -dy
            elif dx == 0:
                dy = abs(dy)
            slopes[(dx, dy)] += 1
        if slopes:
            max_count = max(max_count, max(slopes.values()) + 1)
    return max_count"""),
        ]
    },
}

def write_file(filepath, content):
    os.makedirs(os.path.dirname(filepath), exist_ok=True)
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)

def generate_problem(idx, title, statement, input_fmt, output_fmt, constraints, example_input, example_output):
    return f"""# Problem {idx}: {title}

## Problem Statement
{statement}

## Input Format
- {input_fmt}

## Output Format
- {output_fmt}

## Constraints
- {constraints}

## Example
**Input:** {example_input}  
**Output:** {example_output}
"""

def generate_solution(idx, title, approach, steps, time_c, space_c, code):
    steps_text = "\n".join(f"{i+1}. {s}" for i, s in enumerate(steps))
    return f"""# Solution {idx}: {title}

## Approach Explanation
{approach}

## Step-by-Step Logic
{steps_text}

## Complexity
- **Time Complexity:** {time_c}
- **Space Complexity:** {space_c}

## Code
```python
{code}
```
"""

def main():
    for topic_name, data in TOPICS.items():
        print(f"Generating {topic_name}...")
        for i, prob in enumerate(data["problems"], 1):
            title, statement, input_fmt, output_fmt, constraints, ex_in, ex_out = prob
            content = generate_problem(i, title, statement, input_fmt, output_fmt, constraints, ex_in, ex_out)
            filepath = os.path.join(BASE_DIR, topic_name, "Problems", f"problem{i}.md")
            write_file(filepath, content)
        
        for i, sol in enumerate(data["solutions"], 1):
            title, approach, steps, time_c, space_c, code = sol
            content = generate_solution(i, title, approach, steps, time_c, space_c, code)
            filepath = os.path.join(BASE_DIR, topic_name, "Solutions", f"solution{i}.md")
            write_file(filepath, content)
        
        print(f"  DONE {topic_name}: {len(data['problems'])} problems + {len(data['solutions'])} solutions")

if __name__ == "__main__":
    main()
