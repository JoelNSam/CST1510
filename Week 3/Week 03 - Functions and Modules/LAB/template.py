"""
RECORD CHECK  -  my version
===========================

Name  :Joel Nathanael Sam
Lane  :  AI       (delete two)
Date  :

Run it:   python template.py

Work through the numbered sections in order. Each one tells you what it must do.
Delete these instructions as you replace them with your code.
"""
def status_of(percent):
    if percent > 100:
        return "OVER LIMIT"
    elif percent >= 90:
        return "WARNING"
    else:
        return "OK"

name = input("Server name: ")
used = int(input("Used: "))
total = int(input("Total: "))

difference = total - used
percent = used / total * 100
status = status_of(percent)

border = "=" * 34

print(border)
print(f"  RECORD CHECK  -  {name}")
print(border)
print(f"  {'Used':<12}: {used}")
print(f"  {'Total':<12}: {total}")
print(f"  {'Status':<12}: {status}")
print(border)
# ==================================================================== INPUT
# 2. Ask for your three values.
#
#    - the first is TEXT      (a name, a hostname, an IP)  -> no conversion needed
#    - the second is a NUMBER (use float(), not int())
#    - the third  is a NUMBER (use float(), not int())

label = ""      # replace with an input() call
value = 0.0     # replace with an input() call, converted
limit = 0.0     # replace with an input() call, converted


# ================================================================== PROCESS
# 3. Work out the difference, the percentage, and the status.
#
#    Threshold : call status_of() to get the status. Work out the
#                difference and percentage inline, not in a function.
#    Typical   : call check() to get the difference and percentage instead.

difference = 0.0   # replace with your code
percent = 0.0       # replace with your code
status = ""          # replace with your code


# =================================================================== OUTPUT
# 4. Print the report.
#
#    Threshold : the three values you were given, plus status, inside a border
#    Typical   : add difference and percent, 2 decimal places, right-aligned
#    Excellent : call print_report() instead of printing directly here, and
#                wrap sections 2-4 in a loop so you can check as many records
#                as you like in one run - type "quit" as the label to stop.
#                Keep count of how many came back OVER LIMIT and print that
#                once, after the loop ends.

print()
print("=" * 34)
print(f"  RECORD CHECK  -  {label}")
print("=" * 34)

# your report lines go here

print("=" * 34)


# ==========================================================================
# 5. Before you finish:
#
#    [ ] Run it three times with different numbers
#    [ ] Run it with a total of 0 and note the error (do not fix it yet)
#    [ ] Check every function does one job - if a function both calculates
#        and prints, split it
