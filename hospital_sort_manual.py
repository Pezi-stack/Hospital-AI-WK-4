"""
Manual Implementation: Sorting Hospital Patient Records
This version uses traditional approach with explicit sorting logic.
"""

def sort_patients_manual(patients_list, sort_key):
    """
    Manually sorts a list of patient dictionaries by a specific key.
    
    Args:
        patients_list: List of dictionaries containing patient information
        sort_key: The key to sort by (e.g., 'patient_id', 'name', 'age', 'admission_date')
    
    Returns:
        Sorted list of patient dictionaries
    """
    # Create a copy to avoid modifying the original list
    sorted_list = patients_list.copy()
    
    # Manual bubble sort implementation (less efficient)
    n = len(sorted_list)
    for i in range(n):
        for j in range(0, n - i - 1):
            # Handle missing keys by treating them as None or empty string
            key1 = sorted_list[j].get(sort_key, None)
            key2 = sorted_list[j + 1].get(sort_key, None)
            
            # Compare values - handle None cases
            if key1 is None:
                key1 = ""
            if key2 is None:
                key2 = ""
            
            # Swap if needed
            if key1 > key2:
                sorted_list[j], sorted_list[j + 1] = sorted_list[j + 1], sorted_list[j]
    
    return sorted_list


def sort_patients_manual_v2(patients_list, sort_key):
    """
    Manual implementation using built-in sort with lambda (more efficient manual approach).
    This is what a developer might write manually without AI assistance.
    
    Args:
        patients_list: List of dictionaries containing patient information
        sort_key: The key to sort by
    
    Returns:
        Sorted list of patient dictionaries
    """
    sorted_list = patients_list.copy()
    sorted_list.sort(key=lambda x: x.get(sort_key, ''))
    return sorted_list


# Example usage with hospital patient data
if __name__ == "__main__":
    # Sample hospital patient records
    patients = [
        {"patient_id": "P003", "name": "John Smith", "age": 45, "admission_date": "2024-01-15", "department": "Cardiology"},
        {"patient_id": "P001", "name": "Alice Johnson", "age": 32, "admission_date": "2024-01-10", "department": "Pediatrics"},
        {"patient_id": "P005", "name": "Bob Williams", "age": 58, "admission_date": "2024-01-20", "department": "Orthopedics"},
        {"patient_id": "P002", "name": "Carol Davis", "age": 28, "admission_date": "2024-01-12", "department": "Maternity"},
        {"patient_id": "P004", "name": "David Brown", "age": 65, "admission_date": "2024-01-18", "department": "Neurology"}
    ]
    
    print("Original Patient List:")
    for patient in patients:
        print(f"  {patient}")
    
    print("\n--- Manual Bubble Sort (Inefficient) ---")
    sorted_by_id = sort_patients_manual(patients, "patient_id")
    for patient in sorted_by_id:
        print(f"  {patient}")
    
    print("\n--- Manual Lambda Sort (Efficient) ---")
    sorted_by_age = sort_patients_manual_v2(patients, "age")
    for patient in sorted_by_age:
        print(f"  {patient}")

