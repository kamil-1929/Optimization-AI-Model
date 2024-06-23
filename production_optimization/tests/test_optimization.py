import unittest
import pulp as pl
from production_optimization import optimization_model

class TestOptimization(unittest.TestCase):
    def test_optimal_solution(self):
        # Solve the model
        optimization_model.model.solve()
        # Check if the solution is optimal
        self.assertEqual(pl.LpStatus[optimization_model.model.status], 'Optimal')
        # Check the value of the objective function
        self.assertAlmostEqual(pl.value(optimization_model.model.objective), 240)  # Example expected value, adjust accordingly

if __name__ == '__main__':
    unittest.main()
