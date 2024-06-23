import unittest
from production_optimization.optimization_model import run_optimization
import pulp as pl

class TestOptimization(unittest.TestCase):
    def test_optimal_solution(self):
        # Solve the model and capture the returned model object
        model = run_optimization()
        # Check if the solution is optimal
        self.assertEqual(pl.LpStatus[model.status], 'Optimal')

if __name__ == '__main__':
    unittest.main()
