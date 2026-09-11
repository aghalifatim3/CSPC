# CSPC

## PW1 — Lab A

Tests: 3/3 passed (test_starts_at_N0, test_rejects_negative_rate, test_matches_law)

Speed comparison (N = 200000 atoms):
- Pure-Python loop: 2.7542 s
- NumPy vectorized: 0.0003 s
- NumPy is ~9676x faster

Conclusion:
The pure-Python loop checks each atom one by one,which is slow when there are many atoms.NumPy instead handles all atoms at once using a single vectorized operation,so it avoids Python's slow loop overhead.This is why the NumPy version finishes almost instantly while the loop version takes a few seconds.