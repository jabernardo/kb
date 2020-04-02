# Common Questions for argparse library

`argparse` is a library included in Python installation package that enables us to parse command-line arguments like
what the old `argp` C  library did.

## Parsing Command-line Arguments

<details>
  <summary>View Code</summary>
  
```python
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("-n", "--name", help="Username")
args = parser.parse_args()

print(args)

```

</details>
