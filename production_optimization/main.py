from production_optimization import optimization_model

def main():
    # Run the optimization
    optimization_model.model.solve()
    # Output the results
    print(f"Status: {optimization_model.pl.LpStatus[optimization_model.model.status]}")
    print(f"Objective: {optimization_model.pl.value(optimization_model.model.objective)}")
    for v in optimization_model.model.variables():
        print(f"{v.name} = {v.varValue}")

if __name__ == "__main__":
    main()
