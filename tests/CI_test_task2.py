import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

def test_task2_requirements():
    """Test that Task 2 requirements are met"""
    # Check if required files exist
    assert os.path.exists('notebooks/task2_AAPL_technical_analysis.ipynb'), "AAPL notebook missing"
    assert os.path.exists('notebooks/task2_AMZN_technical_analysis.ipynb'), "AMZN notebook missing"
    assert os.path.exists('requirements_task2.txt'), "Task 2 requirements missing"
    print(" Task 2 files verified")

def test_task2_dependencies():
    """Test that Task 2 dependencies can be imported"""
    try:
        import talib
        import pynance
        import yfinance
        print(" Task 2 dependencies imported successfully")
        assert True
    except ImportError as e:
        print(f" Task 2 dependency error: {e}")
        assert False

if __name__ == "__main__":
    test_task2_requirements()
    test_task2_dependencies()
    print(" Task 2 tests completed!")