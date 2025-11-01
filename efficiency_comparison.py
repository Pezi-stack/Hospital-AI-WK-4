"""
Efficiency Comparison: Manual vs AI-Suggested Implementation
This script benchmarks different sorting approaches for hospital patient records.
"""

import time
import random
from hospital_sort_manual import sort_patients_manual, sort_patients_manual_v2
from hospital_sort_ai import sort_patients_ai, sort_patients_multi_key


def generate_sample_patients(n: int) -> list:
    """Generate n random patient records for testing."""
    departments = ["Cardiology", "Pediatrics", "Orthopedics", "Maternity", "Neurology", "Emergency"]
    first_names = ["John", "Alice", "Bob", "Carol", "David", "Emma", "Frank", "Grace"]
    last_names = ["Smith", "Johnson", "Williams", "Davis", "Brown", "Miller", "Wilson", "Moore"]
    
    patients = []
    for i in range(n):
        patient_id = f"P{random.randint(1000, 9999)}"
        name = f"{random.choice(first_names)} {random.choice(last_names)}"
        age = random.randint(18, 90)
        admission_date = f"2024-01-{random.randint(1, 28):02d}"
        department = random.choice(departments)
        
        patients.append({
            "patient_id": patient_id,
            "name": name,
            "age": age,
            "admission_date": admission_date,
            "department": department
        })
    
    return patients


def benchmark_sort(func, patients, sort_key, iterations=100):
    """Benchmark a sorting function."""
    times = []
    for _ in range(iterations):
        test_patients = patients.copy()
        start = time.perf_counter()
        result = func(test_patients, sort_key)
        end = time.perf_counter()
        times.append(end - start)
    return sum(times) / len(times) * 1000  # Return average in milliseconds


if __name__ == "__main__":
    print("=" * 60)
    print("EFFICIENCY COMPARISON: Manual vs AI-Suggested Sorting")
    print("=" * 60)
    
    # Test with different dataset sizes
    sizes = [10, 100, 1000]
    
    for size in sizes:
        print(f"\n--- Testing with {size} patient records ---")
        patients = generate_sample_patients(size)
        
        # Benchmark each approach
        manual_bubble_time = benchmark_sort(sort_patients_manual, patients, "patient_id", 10)
        manual_lambda_time = benchmark_sort(sort_patients_manual_v2, patients, "patient_id", 10)
        ai_time = benchmark_sort(sort_patients_ai, patients, "patient_id", 10)
        
        print(f"Manual Bubble Sort:      {manual_bubble_time:.4f} ms")
        print(f"Manual Lambda Sort:      {manual_lambda_time:.4f} ms")
        print(f"AI-Suggested Sort:       {ai_time:.4f} ms")
        
        # Calculate speedup
        if manual_bubble_time > 0:
            speedup_bubble = manual_bubble_time / ai_time
            print(f"AI is {speedup_bubble:.2f}x faster than bubble sort")
        
        if manual_lambda_time > 0:
            speedup_lambda = manual_lambda_time / ai_time
            print(f"AI is {speedup_lambda:.2f}x faster than manual lambda")
    
    print("\n" + "=" * 60)
    print("Note: AI-suggested version uses Python's optimized TimSort algorithm")
    print("which is more efficient than manual implementations for most cases.")
    print("=" * 60)

