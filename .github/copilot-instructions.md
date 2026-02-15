# AI Coding Instructions

## Project Overview
Academic algorithm study project (N1 Activity) for a 7th semester Advanced Algorithms course. Contains optimized solutions for classic algorithmic problems using efficient data structures and techniques.

## Architecture & Key Patterns

### Algorithm Implementation Style
- **Optimal-First Approach**: Prioritize O(n) or O(n log n) solutions over brute force
- **Data Structure Usage**: Leverage hash maps (dictionaries) for O(1) lookups instead of nested loops
- **Comment in Portuguese**: Code comments use Portuguese (e.g., `# valor -> índice` for "value -> index")

### Example: TwoSum Pattern
File: `TwoSum`
- **Problem**: Find two numbers that sum to a target
- **Pattern Used**: Single-pass hash map to store visited values with their indices
- **Key Insight**: Trade space for time - use O(n) space to achieve O(n) time instead of O(n²)

```python
# Store value and index for constant-time complement lookup
mapa = {}
for i, num in enumerate(nums):
    complemento = target - num  # Check if complement exists
    if complemento in mapa:
        return [mapa[complemento], i]
    mapa[num] = i
return []
```

## Coding Conventions
1. **Variable Naming**: Use Portuguese descriptive names (`mapa`, `complemento`, `índice`)
2. **Return Early**: Return immediately when solution found rather than breaking loops
3. **Fallback Cases**: Always return empty list or appropriate sentinel for "no solution" cases

## Development Notes
- Solutions follow LeetCode-style interface patterns
- Focus on production-ready algorithms, not just correctness
- Document time/space complexity implications in comments when non-obvious
