# test-data-generator

This API is used to generated the test data based on schema.

url for test data generation- POST Request:

```http://localhost:5000/generate/test/data```

Example input Schema:

```
{
  "row_count": 120,
  "data_gen": [
    {
      "name": "field_name",
      "data_type": "data-type",
      "enums": [
        "values"
      ],
      "range": [0, 20]
    }
  ]
}
```

Steps to generate test data:

1. run ```app.py ```
2. post the valid schema from any rest client (Postman)
