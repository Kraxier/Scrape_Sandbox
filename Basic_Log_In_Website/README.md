
# Concept of Log In Website and Basic To Handling Sessions

Inspired by: *Web Scraping with Python* by Ryan Mitchel

---

## Introductions

Logging into websites and handling sessions is one of the most important web scraping skills that web scrapers need to learn. It requires a good understanding of how websites work. These are some of the things I needed to learn in order to scrape a website that has a login feature.

We need to understand the **POST** method where **you push information to a web server**, in contrast to the **GET** method which **requests information** from the web server.

One of the most common tools to do this is the **Python Requests Library** where the implementation begins with:

```python
import requests
```

---

## Submitting Basic Forms

In terms of HTML, a basic form looks like this:

```html
<form method="post" action="processing.php">
  First name: <input type="text" name="firstname"><br>
  Last name: <input type="text" name="lastname"><br>
  <input type="submit" value="Submit">
</form>
```

Notice `name="firstname"` and `name="lastname"`. You need to use those as parameters in your code:

```python
params = {'firstname': 'Kraxier', 'lastname': 'No_Lastname'}
r = requests.post("http://example.com/pages/processing.php", data=params)
```

### Breakdown of the `requests.post`:

```python
r = requests.post(url, data={key: value}, json={key: value}, headers={key: value})
```

- `url`: The endpoint you're sending the request to (required)
- `data`: For sending form-encoded data (optional)
- `json`: For sending JSON data (optional)
- `headers`: For sending HTTP headers (optional)

> ⚠️ The `url` should be the **endpoint**, not the login page itself.

---

### Key Things to Know:

1. The name of the fields you want to submit with the data.
2. The `action` attribute of the form (where the data is posted to).

---

### HTML Notes:

When you submit a form:

- `method="post"` specifies using the POST method.
- `action="processing.php"` is the endpoint URL.

> If the form is at `https://pythonscraping.com/pages/files/form.html`, then `processing.php` is relative to that.

**What Happens If You Send Data to the Wrong URL?**

If you send your POST request to the form page (`form.html`), you're not hitting the server-side script that processes the form.

---

### Other Inputs in HTML

- Radio buttons
- Checkboxes
- JavaScript-based fields

Still, you only need to worry about the **name** attribute and locate it using browser inspection tools (like Chrome Developer Tools).

---

### Submitting Files/Images

Rare and not commonly needed, so not covered deeply.

---

## How to Handle Logins and Cookies

After learning how to submit forms, we also need to **maintain login state**. Most modern websites use **cookies** to track login sessions.

### Cookies Contain:

- Server-generated token
- Timeout settings
- Tracking info

### Handling Cookies with Sessions

```python
import requests
session = requests.Session()
r = session.post("http://example.com/pages/processing.php", data=params)
```

Sessions help persist:

- Cookies
- Headers
- Protocol info

---

### Important Cookie Notes:

1. Inspect cookies (e.g., `session_id=abc123`)
2. Look at expiration times
3. Know `HTTPOnly`, `Secure`, `SameSite` flags
4. Understand session tracking
5. Handle CSRF protection (`csrftoken`)
6. Be mindful of rate-limiting

> Mimic real users to avoid blocks!

---

### Other Authentication

- Selenium library can help with complex cases
- HTTP Basic Auth is also used on high-security or corporate sites

---

## log_in_1.py

Demonstrates fundamentals learned from the book using:

- Website: https://quotes.toscrape.com/login

Implemented Concepts:

1. POST method
2. Request library
3. Chrome Inspect Developer Tools

---

## Traditional Forms vs. JavaScript Forms

Modern sites (e.g., Upwork, Instagram) use **APIs and JavaScript** instead of standard `<form>` elements.

You must inspect **Network Activity** for:

- Hidden API URLs
- X-CSRF token
- JavaScript verification
- CAPTCHA handling
- Selenium usage

---

### Why Learn Traditional Form Submission?

Even modern websites follow the same data flow:

1. Collect input from HTML
2. Process via backend
3. Validate and authenticate
4. Redirect user

**Understanding forms teaches you:**

- ✅ How HTTP works
- ✅ How authentication works
- ✅ How data is structured
- ✅ How to simulate a browser in Python

---

### Cookies: Explained

```text
1. What is a Cookie?
    - A small piece of data stored in your browser by a website.
    - Used for sessions, authentication, preferences.
    - Stored as key-value pairs.
    - Temporary (session) or persistent.
```

#### Example:

- You log in → Server sends `Set-Cookie: session_id=abc123`
- Browser stores and sends it back in future requests
- Server uses it to identify you

---

### Sessions: Explained

```text
1. What is a Session?
    - Temporary connection between client and server
    - Tracked via session IDs in cookies or headers
```

#### Workflow:

- You log in
- Server validates and creates session
- Session ID stored in browser
- Sent with every request
- Deleted upon logout

---

### Tokens: Explained

```text
1. What is a Token?
    - Used to verify identity and enhance security
    - CSRF Tokens and Auth Tokens like JWT, OAuth
```

#### CSRF Example:

```html
<input type="hidden" name="csrf_token" value="123xyz">
```

---

## Summary: Submitting Forms and Logging In

### Understanding HTML Forms

- Structure contains fields like username/password
- Submit sends data to `action` endpoint via `method`

### Key Differences:

- `form.html`: front-end UI
- `processing.php`: back-end processor

### Traditional vs Modern:

- Traditional: teaches HTTP, server processing
- Modern: uses JS and APIs (but same principle applies)

---

### HTTP Methods

- **GET**: Fetch data
- **POST**: Send data (e.g., login)
- Server-side processes the request and sends a response

---

## Understanding Chrome DevTools

### Network Panel:

- Monitor all requests (method, status, response)
- View form data sent in real-time

---

