# User Guide

This guide provides detailed instructions on how to use the production optimization project.

## Running the Optimization

To run the optimization model, use the following command:

```sh
python -m production_optimization.main
```

This will execute the main script and print the optimization results.

## Understanding the Results
The output of the optimization includes:

- The status of the solution (Optimal, Infeasible, etc.).
- The value of the objective function (total profit).
- The values of the decision variables (production quantities for each product).

## Customizing the Model
If you need to customize the optimization model, you can modify the optimization_model.py file. This file contains the definition of the decision variables, objective function, and constraints.

## Running Tests
To ensure the correctness of the model, run the unit tests using the following command:

```sh
pytest
```
The tests are located in the production_optimization/tests directory and cover the basic functionality of the optimization model.

## Further Assistance
For further assistance, refer to the README file or contact the project maintainers.
