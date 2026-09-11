import time
from decay import simulate, simulate_loop

N = 200000
lam = 0.4

start = time.perf_counter()
simulate_loop(N, lam)
loop_time = time.perf_counter() - start

start = time.perf_counter()
simulate(N, lam)
numpy_time = time.perf_counter() - start

print(f"Pure-Python loop: {loop_time:.4f} s")
print(f"NumPy vectorized: {numpy_time:.4f} s")
print(f"NumPy is {loop_time / numpy_time:.1f}x faster")