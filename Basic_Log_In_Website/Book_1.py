
'''
# This is the HTML of this URL: https://pythonscraping.com/pages/files/form.html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Form Example</title>
</head>
<body>
    <h2>Tell me your name!</h2>
    <form method="post" action="processing.php">
        <label for="firstname">First name:</label>
        <input type="text" id="firstname" name="firstname" required><br><br>

        <label for="lastname">Last name:</label>
        <input type="text" id="lastname" name="lastname" required><br><br>

        <input type="submit" value="Submit" id="submit">
    </form>
</body>
</html>
'''
import requests

params = {'firstname': 'Kraxier', 'lastname': 'Luthor'}
r = requests.post("https://pythonscraping.com/pages/files/processing.php", data=params)
print(r.text)
