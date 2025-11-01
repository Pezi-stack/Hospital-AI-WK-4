"""
AI-Suggested Implementation: Sorting Hospital Patient Records
This version represents what modern AI code completion tools (like GitHub Copilot, Tabnine) 
would typically suggest - using Pythonic, efficient, and modern approaches.
"""

from typing import List, Dict, Any, Optional
from operator import itemgetter


def sort_patients_ai(patients_list: List[Dict[str, Any]], sort_key: str, reverse: bool = False) -> List[Dict[str, Any]]:
    """
    AI-optimized function to sort a list of patient dictionaries by a specific key.
    
    Uses:
    - Type hints for better code clarity
    - sorted() built-in for efficiency (TimSort algorithm)
    - operator.itemgetter for faster key extraction
    - Optional reverse parameter for descending order
    
    Args:
        patients_list: List of dictionaries containing patient information
        sort_key: The key to sort by (e.g., 'patient_id', 'name', 'age', 'admission_date')
        reverse: If True, sort in descending order (default: False)
    
    Returns:
        New sorted list of patient dictionaries (original unchanged)
    
    Raises:
        ValueError: If sort_key is not provided or empty
    """
    if not sort_key:
        raise ValueError("sort_key cannot be empty")
    
    # Use sorted() which is more efficient than list.sort() when you want a new list
    # operator.itemgetter is faster than lambda for simple key access
    return sorted(
        patients_list,
        key=lambda x: x.get(sort_key, '') if x.get(sort_key) is not None else '',
        reverse=reverse
    )


def sort_patients_multi_key(patients_list: List[Dict[str, Any]], 
                           sort_keys: List[str], 
                           reverse: bool = False) -> List[Dict[str, Any]]:
    """
    AI-enhanced: Sort by multiple keys (e.g., department first, then age).
    This is a more advanced feature AI tools often suggest.
    
    Args:
        patients_list: List of patient dictionaries
        sort_keys: List of keys to sort by (priority order)
        reverse: If True, sort in descending order
    
    Returns:
        Sorted list of patient dictionaries
    """
    if not sort_keys:
        raise ValueError("sort_keys cannot be empty")
    
    def get_sort_value(patient: Dict[str, Any]) -> tuple:
        """Extract sort values as a tuple for multi-key sorting."""
        return tuple(patient.get(key, '') for key in sort_keys)
    
    return sorted(patients_list, key=get_sort_value, reverse=reverse)


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
    
    print("\n--- AI-Suggested Sort by Patient ID ---")
    sorted_by_id = sort_patients_ai(patients, "patient_id")
    for patient in sorted_by_id:
        print(f"  {patient}")
    
    print("\n--- AI-Suggested Sort by Age (Descending) ---")
    sorted_by_age = sort_patients_ai(patients, "age", reverse=True)
    for patient in sorted_by_age:
        print(f"  {patient}")
    
    print("\n--- AI Multi-Key Sort (Department, then Age) ---")
    sorted_multi = sort_patients_multi_key(patients, ["department", "age"])
    for patient in sorted_multi:
        print(f"  {patient}")

