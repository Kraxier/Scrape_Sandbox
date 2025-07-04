r'''
Key Strengths in Your Approach:
    Height Comparison Logic - You correctly identified that comparing scroll heights is essential for detecting new content
    Network Awareness - Using wait_for_load_state("networkidle") shows good understanding of content loading patterns
    Progressive Debugging - Your print statements and observations demonstrate systematic problem-solving
    Quote Tracking - The set-based deduplication is efficient for tracking unique content

    
Figure Out WHen to Stop at Things 
'''

# Core Issues and Solutions: On the Previous Prototpe 2

# 1. Unreliable Break Condition
r'''
Problem: Scroll positions will rarely be exactly equal due to sub-pixel rendering
Fix: Use threshold-based comparison:
'''
# scroll_threshold = 5  # pixels tolerance

# if abs(new_height_page - prev_height_page) < scroll_threshold and \
#    abs(new_scroll_pos - prev_scroll_pos) < scroll_threshold:
#     break


# 2. Inefficient Quote Handling
r'''
Problem: Re-querying ALL quotes and rebuilding the set every iteration is O(n²)
Fix: Track new quotes incrementally:
'''
# Initialize before loop
# all_quotes = set()
# last_count = 0

# # Inside loop
# new_quotes = page.locator(".quote:not(:has-text(''))").all()  # Only new quotes
# for quote in new_quotes:
#     if (text := quote.text_content()) not in all_quotes:
#         all_quotes.add(text)

# if len(all_quotes) == last_count:
#     no_new_count += 1
# else:
#     no_new_count = 0
#     last_count = len(all_quotes)

# 3. Missing Scrolling Safeguards
r'''
Problem: Potential for infinite loops
Fix: Implement multi-factor termination:
'''
# Initialize before loop
# max_attempts = 10
# no_new_count = 0
# max_no_new = 3

# # Inside loop
# if no_new_count >= max_no_new or attempt >= max_attempts:
#     break

# 4. Viewport Relationship Ignored
r'''
Problem: Bottom detection requires viewport size
Fix: Calculate true page bottom:
'''
# viewport_height = page.evaluate("window.innerHeight")
# at_bottom = new_scroll_pos + viewport_height >= new_height_page - 10  # 10px threshold

r'''
Key Improvements:

1. Human-Like Scrolling
    Random scroll distances (700-1000px)
    Variable pauses (1.5-2.5s)
    Mimics natural reading patterns

2. Robust Termination
    Triple safeguard:
        Max scroll attempts (15)
        Consecutive fails (3)
        Bottom detection
Prevents infinite loops

3. Efficient Content Tracking
    Only processes new quotes
    Uses combined selector (.quote >> visible=true)
    Tracks additions incrementally

4. Accurate Bottom Detection
    Considers viewport height
    Uses 10px threshold for rendering variances

Recommendations:
Add Randomization
    Vary scroll direction occasionally (small upward scrolls)
    Include random mouse movements
    Simulate human hesitation patterns

Error Handling

    Add try/except for DOM mutations
    Handle stale element references

Implement retry logic for flaky content

'''
