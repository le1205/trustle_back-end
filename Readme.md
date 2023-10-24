# Flask REST API

This is a simple Flask REST API that provides two routes: `/ping` and `/urls`. The API accepts a JSON payload with a username and returns a response based on the requested route.

## Endpoints

### `/ping`

- Method: GET
- Description: Returns a simple "pong" response to check if the API is running.

#### Request

- No request payload is required.

#### Response

- Status Code: 200 (OK)
- Body: "pong"

### `/urls`

- Method: POST
- Description: Returns a list of URLs indicating the presence or absence of the provided username.

#### Request

- Body: JSON payload containing the username.

```json
{
  "username": "joellui"
}
```

#### Response

- Status Code: 200 (OK)
- Body: JSON array of dictionaries, each containing a URL and a boolean value indicating the presence (true) or absence (false) of the username.

```json
[
  {
    "https://ask.fm/@username": false
  },
  {
    "https://pinterest.com/@username": true
  },
  {
    "https://tumblr.com/blog/@username": true
  },
  ...
]
```

### `/fetchlink`

- Method: POST
- Description: Returns a list of URLs indicating the presence or absence of the provided username.

#### Request

- Body: JSON payload containing the username.

```json
{
  "username": "michael bage",
  "separators": [".", "_"]
}
```

## Running the API

To run the API, follow these steps:

1. Install the required dependencies by running `pip install -r requirements.txt`.
2. Start the Flask server by running `python main.py`.
3. The API will be accessible at `http://localhost:5000`.
