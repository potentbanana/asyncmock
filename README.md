# asyncmock
A dead simple mock for unit tests with async coroutines.

## Usage
About the simplest you can deal with

```python
import asyncio
import unittest
from asyncmock import AsyncMock

from sample import Sample

class SampleTest(unittest.TestCase):

    def test_sample_method(self):
        sample_ = Sample()
        async_mock = AsyncMock(sample_.asyncdependency)
        async_mock.set_response("get_url", {"new": "results"})

        loop = asyncio.get_event_loop()
        response = loop.run_until_complete(sample_.some_method_that_calls_get_url_from_dependency)
        self.assertEqual(response, {"new": "results"})
```

This can be helpful when you're pulling down third party data in your class and need to mock it out, but it's asynchronous and MagicMock won't handle async coroutines.

