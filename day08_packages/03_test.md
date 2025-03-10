# Test code using unittest

```python
def upper_case(text):
    return text.upper()
```

```python
import unittest

import change_text


class TestChangeText(unittest.TestCase):
    def test_upper_case(self):
        word = "good day"
        result = change_text.upper_case(word)
        self.assertEqual(result, "GOOD DAY")


if __name__ == "__main__":
    unittest.main()
```
