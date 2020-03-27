import unittest
import solution

class TestSolution(unittest.TestCase):

    def test_find_ordering(self):
        # Testing given input set
        self.assertEqual(
            solution.find_ordering({
                "C1": [], 
                "C2": ["C1"],
                "C3": ["C2"],
                "LA": ["C2"],
                "DM": ["C2"],
                "DE": ["C3"],
                "AML": ["DE", "LA", "AA"],
                "P1": [],
                "P2": ["P1"],
                "AA": ["P2", "DM"]
                }), 
                ['C1', 'C2', 'C3', 'LA', 'DM', 'DE', 'P1', 'P2', 'AA', 'AML'])
        
        # Testing only one empty dependency
        self.assertEqual(
            solution.find_ordering({
                "C1": ["P1"], 
                "C2": ["C1"],
                "C3": ["C2"],
                "LA": ["C2"],
                "DM": ["C2"],
                "DE": ["C3"],
                "AML": ["DE", "LA", "AA"],
                "P1": [],
                "P2": ["P1"],
                "AA": ["P2", "DM"]
                }), 
                ['P1', 'P2', 'C1', 'C2', 'C3', 'LA', 'DM', 'DE', 'AA', 'AML'])
        
        # Testing lots of empty dependencies
        self.assertEqual(
            solution.find_ordering({
                "C1": [], 
                "C2": [],
                "C3": [],
                "LA": [],
                "DM": [],
                "DE": [],
                "AML": ["DE", "LA", "AA"],
                "P1": [],
                "P2": [],
                "AA": []
                }), 
                ['C1', 'C2', 'C3', 'LA', 'DM', 'DE', 'P1', 'P2', 'AA', 'AML'])
        
        # Testing no dependencies
        self.assertEqual(
            solution.find_ordering({
                "C1": [], 
                "C2": [],
                "C3": [],
                "LA": [],
                "DM": [],
                "DE": [],
                "AML": [],
                "P1": [],
                "P2": [],
                "AA": []
                }), 
                ['C1', 'C2', 'C3', 'LA', 'DM', 'DE', 'AML', 'P1', 'P2', 'AA'])

        # Test instance type of output
        self.assertIsInstance(solution.find_ordering({
            "C1": [], 
            "C2": ["C1"],
            "C3": ["C2"],
            "LA": ["C2"],
            "DM": ["C2"],
            "DE": ["C3"],
            "AML": ["DE", "LA", "AA"],
            "P1": [],
            "P2": ["P1"],
            "AA": ["P2", "DM"]
            }), list)
    
if __name__ == "__main__":
    unittest.main()