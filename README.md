# AI-Powered Code Completion: Hospital Patient Sorting Analysis

This project compares manual and AI-suggested implementations for sorting hospital patient records (dictionaries) by a specific key.

## Files

- `hospital_sort_manual.py` - Manual implementations (bubble sort and lambda sort)
- `hospital_sort_ai.py` - AI-suggested implementation with modern Python features
- `efficiency_comparison.py` - Benchmarking script to compare performance
- `ANALYSIS.md` - Detailed 200-word efficiency analysis

## Usage

### Run Manual Implementation
```bash
python hospital_sort_manual.py
```

### Run AI-Suggested Implementation
```bash
python hospital_sort_ai.py
```

### Run Performance Benchmarks
```bash
python efficiency_comparison.py
```

## Sample Output

The implementations demonstrate sorting hospital patient records by various keys:
- `patient_id` - Unique patient identifier
- `age` - Patient age
- `admission_date` - Date of hospital admission
- `department` - Medical department
- Multi-key sorting (department, then age)

## Key Findings

The AI-suggested implementation is more efficient because it:
1. Uses Python's optimized TimSort algorithm (O(n log n))
2. Includes type hints and error handling
3. Provides additional features like reverse sorting and multi-key sorting
4. Handles edge cases more gracefully

See `ANALYSIS.md` for the complete 200-word efficiency analysis.

