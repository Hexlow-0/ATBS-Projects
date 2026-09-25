import re

log_data = """Logs:
INFO  2026-06-20 14:03:11 Application startup complete
INFO  2026-06-20 14:03:12 Connected to database server
WARNING 2026-06-20 14:05:44 Query execution exceeded expected duration
INFO  2026-06-20 14:05:45 Cache refreshed successfully
ERROR 2026-06-20 14:07:02 Failed to retrieve user profile: timeout
INFO  2026-06-20 14:07:05 Retrying request
INFO  2026-06-20 14:07:06 User profile loaded successfully
WARNING 2026-06-20 14:12:33 Disk usage above 85%
ERROR 2026-06-20 14:15:21 Unable to write backup file
INFO  2026-06-20 14:15:25 Backup process terminated
"""

# A pattern that tries to match from the end of "successfully" on one INFO line
# across the newline into the start of the next line ("ERROR").
pattern_text = r"successfully.*ERROR"

# --- Step 2: without re.DOTALL ---
pattern_no_dotall = re.compile(pattern_text)
match_no_dotall = pattern_no_dotall.search(log_data)

print("=== Without re.DOTALL ===")
print(f"Pattern: {pattern_text!r}")
print(f"Match found: {match_no_dotall is not None}")
if match_no_dotall:
    print(f"Matched text: {match_no_dotall.group()!r}")
else:
    print("As expected, '.' does not match '\\n' by default, "
          "so the pattern can't cross the line break.")

print()

# --- Step 3: with re.DOTALL ---
pattern_with_dotall = re.compile(pattern_text, re.DOTALL)
match_with_dotall = pattern_with_dotall.search(log_data)

print("=== With re.DOTALL ===")
print(f"Pattern: {pattern_text!r}")
print(f"Match found: {match_with_dotall is not None}")
if match_with_dotall:
    print(f"Matched text: {match_with_dotall.group()!r}")

print()

# --- Step 4: counting newlines as a sanity check ---
newline_pattern = re.compile(r"\n")
newlines_found = newline_pattern.findall(log_data)
num_newlines = len(newlines_found)

lines = log_data.split("\n")
num_lines_via_split = len(lines)

print("=== Newline sanity check ===")
print(f"Number of '\\n' characters found by findall: {num_newlines}")
print(f"Number of lines (via split('\\n')): {num_lines_via_split}")
print(f"Check: lines - 1 == newlines -> {num_lines_via_split - 1} == {num_newlines} "
      f"-> {num_lines_via_split - 1 == num_newlines}")
