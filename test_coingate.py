# test_coingate.py
"""
Tests for CoinGate module.
"""

import unittest
from coingate import CoinGate

class TestCoinGate(unittest.TestCase):
    """Test cases for CoinGate class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = CoinGate()
        self.assertIsInstance(instance, CoinGate)
        
    def test_run_method(self):
        """Test the run method."""
        instance = CoinGate()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()
