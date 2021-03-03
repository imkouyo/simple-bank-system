num = float(input())
print("Analytic" if num < 2.0 else "Synthetic" if 2.0 <= num <= 3.0 else "Polysynthetic")