"""
RECORD CHECK  -  my version
===========================

Name  :Joel Nathanel Sam
Lane  :  AI / Cyber / IT      (delete two)
Date  : 11 - 5 - 2026

Run it:   python template.py

Work through the numbered sections in order. Each one tells you what it must do.
Delete these instructions as you replace them with your code.
"""

import pandas as pd

# 1. Read the CSV file
df = pd.read_csv(r"C:\Users\joshm\Desktop\University - Joel Nathanael Sam\CST1510\Week 6\Week 06 - Pandas\Week 06 - Pandas\LAB\records_sample.csv")

# 2. Add percent column
df["percent"] = (df["value"] / df["limit"]) * 100

# 3. Print the DataFrame
print(df)


# ================================================================= PROCESS
# 2. Add a "percent" column: (value / limit) * 100.
#
#    Typical and above: also add a "status" column using .apply() with a
#    lambda - "OVER LIMIT" (100%+), "WARNING" (90%+), otherwise "OK".

# your column(s) go here


# ================================================================== OUTPUT
# 3. Print the DataFrame.
#
#    Threshold : print it as-is, with the percent column.
#    Typical   : also filter to show only the rows that are not "OK", using a
#                boolean condition in [] - not a loop.
#    Excellent : also group by "status" and print a count per group, save
#                the full DataFrame to a new CSV with .to_csv(), and save
#                one bar chart of the counts per status.

print(df)


# ==========================================================================
# 4. Before you finish:
#    [ ] Run it and check the percent/status columns by hand for one row
#    [ ] Check you used & (not "and") if you combined more than one condition
#    [ ] Check every column your code refers to actually exists - watch case
