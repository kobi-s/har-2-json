# HAR to JSON Converter
This Python script converts an HTTP Archive (HAR) file into a JSON file containing an array of request objects. Each object represents a single HTTP request with relevant details like the request method, URL, headers, and data.

## Data Structure
The JSON output will consist of an array of objects, each with the following keys:
```
{
  "method": "HTTP_METHOD",
  "url": "REQUEST_URL",
  "headers": {
    "Header1": "Value1",
    "Header2": "Value2",
    ...
  },
  "data": "POST_DATA_OR_EMPTY_STRING"
}
```
