# Time Allocation Optimizer (Linear Programming)

[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/zedda110088/time-allocation-optimizer/blob/main/notebooks/demo.ipynb)

Optimize weekly time allocation (Study/Sleep/Exercise/Research/Social/Classes) with Linear Programming (PuLP), visualize Baseline vs Optimized, and export the plan as an iCalendar (.ics).

---

## Project Structure
- data/
  - my_diary_30days.csv
- src/
  - optimize.py
  - export_calendar.py
  - plot.py
- notebooks/
  - demo.ipynb
- outputs/
  - baseline_vs_optimized.png
  - optimal_schedule.ics


---

## ▶️ Run in Colab
Click the Colab badge above → Runtime → Run all.

---

## Local Quick Start
```bash
git clone https://github.com/zedda110088/time-allocation-optimizer.git
cd time-allocation-optimizer

pip install -r requirements.txt
jupyter lab   # or: jupyter notebook
```

## Example Output
**Baseline vs Optimized (weekly hours):**  
![Baseline vs Optimized](outputs/baseline_vs_optimized.png)
**Exported Calendar (.ics):**  
Import `outputs/optimal_schedule.ics` into Google Calendar / Apple Calendar.

## How It Works
1. Read your weekly diary data (`my_diary_30days.csv`)
2. Build a linear programming model with PuLP
3. Optimize your time allocation under constraints
4. Visualize baseline vs optimized allocation
5. Export the optimized plan to `.ics` for calendar import



