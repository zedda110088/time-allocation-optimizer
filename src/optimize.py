import pandas as pd
import pulp as pl

def solve_lp_basic(activities: pd.DataFrame, verbose: bool=False) -> pd.Series:

  """
  Build and solve the model in your original style:
    - One variable h_x for each activity, bounded by [min_hours, max_hours]
    - Objective: sum(utility_per_hour * h)
    - Constraint: total hours = 168
  """
    # 1) Create a maximization problem
    model = pl.LpProblem("Time_Allocation", pl.LpMaximize)

    # 2) Define variables (one variable per activity)
    h = {}
    for _, row in activities.iterrows():
        name = row["activity"]
        h[name] = pl.LpVariable(
            f"h_{name}",
            lowBound=float(row["min_hours"]),
            upBound=float(row["max_hours"]),
            cat="Continuous"
        )

    # 3) Define the objective function = sum(utility * hours)
    objective_terms = []
    for _, row in activities.iterrows():
        utility = float(row["utility_per_hour"])
        var     = h[row["activity"]]
        objective_terms.append(utility * var)
    model += pl.lpSum(objective_terms)

    # 4) Add weekly time budget constraint (total = 168 hours)
    model += pl.lpSum(h.values()) == 168

    # 5) Solve the model
    status = model.solve(pl.PULP_CBC_CMD(msg=verbose))
    print("Solver status:", pl.LpStatus[status])

    # 6) Extract results
    opt_hours = {name: pl.value(var) for name, var in h.items()}
    opt = pd.Series(opt_hours, name="opt_hours").sort_index()
    print(opt)
    print("Total hours =", float(opt.sum()))
    return opt
