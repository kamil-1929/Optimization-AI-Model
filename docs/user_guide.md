# User Guide for Production Scheduling Optimization

This user guide provides step-by-step instructions on how to use the Production Scheduling Optimization project.

## Installation

1. **Clone the repository**:
   ```bash
   git clone https://github.com/yourusername/production-optimization.git
   cd production-optimization
   ```

2. **Install dependencie**:
- Using requirements.txt:
    ```bash
    pip install -r requirements.txt
    ```
3. **Using environment.yml**:
    ```bash
    conda env create -f environment.yml
    conda activate production-optimization
    ```

## Running the Optimization
1. Run the main script:

```bash
python production_optimization.py
```

2. Check the output:
The script will print the status of the solution, optimal production quantities for each product, total profit, and resource utilization.

## Understanding the Output
- Status: Indicates if the solution is optimal.
- Optimal Production: The number of units to produce for each product to maximize profit.
T- otal Profit: The total profit achieved with the optimal production quantities.
- Resource Utilization: The total usage of labor, machine time, and raw materials.

## Running Tests
To run the unit tests, use the following command:
```bash
python -m unittest discover -s tests
With this folder structure, your project will be organized and professional, m
