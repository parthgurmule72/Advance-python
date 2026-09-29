import numpy as np
import pandas as pd

# 1. CREATE THE SERIES
def create_random_series(n=10, seed=25):
    """Returns a Series of 10 random integers between 10 and 200."""
    rng = np.random.default_rng(seed)
    values = rng.integers(low=10, high=201, size=n)
    return pd.Series(values)


# 2. CREATE LABELED SERIES
def create_labeled_series(series):
    """Attach custom labels to the Series."""
    labels = [f"value_{i + 101}" for i in range(len(series))]
    return pd.Series(series.values, index=labels)


# 3. DISPLAY SERIES INFORMATION
def describe_series(s, title="Series"):
    print(title)
    print(s)

    print("\nDtype :", s.dtype)
    print("Shape :", s.shape)
    print("Size  :", s.size)
    print("Index :", list(s.index))


# 4. MAIN PROGRAM
if __name__ == "__main__":

    # Step 1: Create Series
    series = create_random_series()

    print("STEP 1: Series with default index")
    describe_series(series)

    # Step 2: Add custom labels
    labeled = create_labeled_series(series)

    print("\nSTEP 2: Same values with custom labels")
    describe_series(labeled, "Labeled Series")

    # Step 3: Basic statistics
    print("\nSTEP 3: Basic Statistics")
    print("Minimum :", series.min())
    print("Maximum :", series.max())
    print("Mean    :", f"{series.mean():.2f}")
    print("Sum     :", series.sum())

    # Step 4: Sorting
    print("\nSTEP 4: Sorted Values")
    print(series.sort_values().to_string())

    # Step 5: Indexing and filtering
    print("\nSTEP 5: Indexing and Filtering")
    print("First value :", series.iloc[0])

    print("\nValues greater than 100:")
    print(series[series > 100].to_string())
