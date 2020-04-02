# Common Questions for Python JSON

## Convert Dictionary to JSON

<details>
  <summary>View Code</summary>
  
```python

import json

data = {
  "name": "John Doe",
  "age": "21"
}

print(json.dumps(data))
```

</details>

## Open JSON file

<details>
  <summary>View Code</summary>
  
```python

import json

def parse_json(filename):
  data = {}
  
  try:
    with open(filename) as json_file:
      data = json.load(json_file)
  except Exception as ex:
    raise ex
    
  return data
```

</details>
