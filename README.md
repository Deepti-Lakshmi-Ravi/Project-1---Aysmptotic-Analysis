# Project 1 - Asymptotic Analysis

## Overview
This project analyses the time complexity of a triple nested loop algorithm:

```c
for (int i = 1 to n) { 
    for (int j = i to n) { 
        for (int k = j*j to n) { 
            Sum += a[i]*b[j]*c[k];
        } 
    } 
}
````

The goal is to compare **theoretical operation counts** with **experimental runtime** and visualize their relationship.

---

--

## Requirements

* Python 3.x
* `matplotlib` library for plotting

Install matplotlib if needed:

```bash
pip install matplotlib
```

---

## Running the Code

1. Open a terminal and navigate to the project folder:

```bash
cd AsymptoticAnalysis
```

2. Run the Python script:

```bash
python analysis.py
```

3. The script will:

   * Compute **experimental runtime** for a set of `n` values.
   * Compute **theoretical operation counts** based on loop constraints.
   * Scale theoretical values to comparable time units.
   * Print a **table** comparing experimental runtime, theoretical ops, and scaled theoretical runtime.
   * Display a **graph** comparing experimental runtime vs scaled theoretical runtime.

---

## Input Sizes Tested

The following `n` values are used in the experiment:

```python
n_values = [4000, 5000, 6000, 7000, 8000, 9000, 10000,
            20000, 30000, 40000, 50000, 80000, 100000]
```


