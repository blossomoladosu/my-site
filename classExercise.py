# recipe shape (from the chapter's coffee-shop example)
import numpy as np

rng = np.random.default_rng(seed=20)
draws = rng.binomial(5, 0.86, size=100_000)
print((draws == 5).mean())

