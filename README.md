# GenericOBJ

## Usage

```python
import generic_obj

a={
 "name": "Temp"   
}
aa = generic_obj.to_obj(a)

b = {
  "name": "B",
  "child": aa
}
bb = generic_obj.to_obj(b)

bb.get()

```

The output will be

```json
{
    "_uuid": "b4a876a5-c3e8-4168-9be0-c5211e930dc3",
    "name": "B",
    "child": {
        "_uuid": "3a25ce15-f7ab-484a-98ee-4bd96ccc70f8",
        "name": "Temp"
    }
}
```