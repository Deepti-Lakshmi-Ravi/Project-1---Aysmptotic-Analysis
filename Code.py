import time
import matplotlib.pyplot as plt

def theoretical_operations(n):
    total = 0
    sqrt_n = int(n**0.5)
    for i in range(1, sqrt_n+1):
        for j in range(i, sqrt_n+1):
            if j*j <= n:
                total += (n - j*j + 1) #Inner loop runs n - j^2 + 1 times
    return total

def experimental_runtime(n):
    start = time.perf_counter() #Starting the timer for experimental runtime
    count = 0
    for i in range(1, n+1):
        for j in range(i, n+1):
            if j*j > n:
                break
            for k in range(j*j, n+1):
                count += 1 #Counting the number of operations
    elapsed_ns = (time.perf_counter() - start) * 1e9 #Convert seconds to nanoseconds
    return elapsed_ns, count

def scale(exp_times, theo_values):
    C = sum(e*t for e,t in zip(exp_times,theo_values)) / sum(t*t for t in theo_values)
    return C, [C*t for t in theo_values] # Multiply theoretical values by scaling constant

def run_experiment(n_values):
    exp_times = []
    theo_values = [theoretical_operations(n) for n in n_values] # Calculate theoretical operations for all n values

    for n in n_values:
        exp_time, _ = experimental_runtime(n)
        exp_times.append(exp_time)  # Measure experimental runtime for all n values

    C, scaled_theory = scale(exp_times, theo_values) #Scaling the theoritical value to match experimental runtime in ns
    print(f"\nScaling constant C = {C:.4f}\n")
    print(f"{'n':>10} {'Experimental(ns)':>20} {'Theoretical Operations':>20} {'Scaled Values(ns)':>20}")
    print("="*90)
    for n,e,t,s in zip(n_values,exp_times,theo_values,scaled_theory):
        print(f"{n:>10} {e:>20.0f} {t:>20.0f} {s:>20.0f}")
    print("="*90)

    plt.figure(figsize=(10,6)) #Plotting the graph
    plt.plot(n_values, exp_times, 'ro-', label='Experimental Runtime')
    plt.plot(n_values, scaled_theory, 'b^-', label='Theoretical Runtime')
    plt.xlabel('n (Input size)')
    plt.ylabel('Runtime (ns)')
    plt.title('Experimental vs Theoretical Runtime')
    xticks = [4000] + [v for i,v in enumerate(n_values) if i%2==0 and v!=4000] #Starts with 4000 and rest is autopicked to show a clear x axis
    plt.xticks(xticks, rotation=45)
    plt.legend()
    plt.grid(True, alpha=0.4)
    plt.tight_layout()
    plt.show()

    return exp_times, theo_values, scaled_theory

if __name__ == "__main__":
    n_values = [4000,5000,6000,7000,8000,9000,10000,20000,30000,40000,50000,80000,100000]
    run_experiment(n_values)
