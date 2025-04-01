
'''Logging in Quote_to_Scrape'''


'''
HTML Website:
<body>
    <div class="container">
        <div class="row header-box">
            <div class="col-md-8">
                <h1>
                    <a href="/" style="text-decoration: none">Quotes to Scrape</a>
                </h1>
            </div>
            <div class="col-md-4">
                <p>
                
                    <a href="/login">Login</a>
                
                </p>
            </div>
        </div>
    

    <form action="/login" method="post" accept-charset="utf-8">
        <input type="hidden" name="csrf_token" value="hrisoNvEqlTWuafFcVOGAUmtXbLkPDKgYjQynISxCdBJpeHRZMzw">
        <div class="row">
            <div class="form-group col-xs-3">
                <label for="username">Username</label>
                <input type="text" class="form-control" id="username" name="username">
            </div>
        </div>
        <div class="row">
            <div class="form-group col-xs-3">
                <label for="username">Password</label>
                <input type="password" class="form-control" id="password" name="password">
            </div>
        </div>
        <input type="submit" value="Login" class="btn btn-primary">
        
    </form>


    </div>
    <footer class="footer">
        <div class="container">
            <p class="text-muted">
                Quotes by: <a href="https://www.goodreads.com/quotes">GoodReads.com</a>
            </p>
            <p class="copyright">
                Made with <span class="zyte">❤</span> by <a class="zyte" href="https://www.zyte.com">Zyte</a>
            </p>
        </div>
    </footer>

</body>

'''

# import requests

# Login_Website: https://quotes.toscrape.com/login
# Website to Scrape: https://quotes.toscrape.com/
# params = {'username': 'Kraxier', 'password': '12345'}
# r = requests.post("https://quotes.toscrape.com/", data=params)
# print(r.text)


# This imports the requests library, which is a popular HTTP library for making web requests in Python.
# import requests

# params = {'username': 'Kraxier', 'password': '12345'}
# Dictionary  in Python used for login credential 

# r = requests.post("https://quotes.toscrape.com/", data=params)
# Sends a POST request to the main page (not the login page) with the credentials
# data=params sends the username/password as form data

'''
<!doctype html>
<html lang=en>
<title>405 Method Not Allowed</title>
<h1>Method Not Allowed</h1>
<p>The method is not allowed for the requested URL.</p>
'''
# import sys
# import io
# sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

# import requests
# login_url = "https://quotes.toscrape.com/login"
# target_url = "https://quotes.toscrape.com/"
# credentials = {'username': 'Kraxier', 'password': '12345'}
# response = requests.post(login_url, data=credentials)
# print(response.text)
# print()
# protected_content = requests.get(target_url)
# print(protected_content.text)




