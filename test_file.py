import shutil
import os
for i in range(1, 101):
    # shutil.copytree("Day 2", f"Day {i} strinf_dsio")
    # shutil.copy("Day 2/day 2.py", f"Day {i}/day {i}.py")
    # os.remove(f"Day {i}/day 2.py")
    # shutil.copytree("Day 2", "Day" + i + "strin")
    # os.remove(f"Day {i} strinf_dsio/day 2.py")
    # os.rmdir(f"Day {i} strinf_dsio")
    os.renames(f"Day {i}", f"Day {i} - code_with_ahmad")
