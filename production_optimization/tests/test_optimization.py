import unittest
import pulp as pl
from production_optimization.optimization_model import run_optimization

class TestOptimization(unittest.TestCase):
    def test_optimal_solution(self):
        # Solve the model
        run_optimization()
        # Check if the solution is optimal
        self.assertEqual(pl.LpStatus[model.status], 'Optimal')
        # Check the value of the objective function
        self.assertAlmostEqual(pl.value(model.objective), 240)  # Example expected value, adjust accordingly

if __name__ == '__main__':
    unittest.main()
