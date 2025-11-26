import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

def test_task3_requirements():
    """Test that Task 3 requirements are met"""
    # Check if required files exist
    assert os.path.exists('notebooks/task3_correlation_analysis.ipynb'), "Correlation notebook missing"
    assert os.path.exists('requirements_task3.txt'), "Task 3 requirements missing"
    print(" Task 3 files verified")

def test_task3_dependencies():
    """Test that Task 3 dependencies can be imported"""
    try:
        from textblob import TextBlob
        from scipy.stats import pearsonr
        print("Task 3 dependencies imported successfully")
        assert True
    except ImportError as e:
        print(f" Task 3 dependency error: {e}")
        assert False

if __name__ == "__main__":
    test_task3_requirements()
    test_task3_dependencies()
    print(" Task 3 tests completed!")