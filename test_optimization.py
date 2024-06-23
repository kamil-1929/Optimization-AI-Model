import unittest
import pulp as pl
from production_optimization import model, x1, x2, x3, x4, x5

class TestOptimization(unittest.TestCase):
    def test_optimal_solution(self):
        # Solve the model
        model.solve()
        # Check if the solution is optimal
        self.assertEqual(pl.LpStatus[model.status], 'Optimal')
        # Check the value of the objective function
        self.assertAlmostEqual(pl.value(model.objective), 240)  # Example expected value, adjust accordingly

if __name__ == '__main__':
    unittest.main()
