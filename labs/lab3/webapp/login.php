<?php

function showForm() {
    print <<< EOL
<form method="post">
<table>
<tr>
<td>Name:</td>
<td><input type="text" name="name" autofocus autocomplete="on"></input></td>
</tr><tr>
<td>Password:</td>
<td><input type="password" name="password" autocomplete="on"></input></td>
</tr><tr>
<td colspan="2" align="right">
<input type="submit" value="Login"/>
</td>
</tr>
</table>
</form>
EOL;
}
showForm();

if (isset($_POST["name"]) && isset($_POST["password"])) {
    if ($_POST["name"] == "admin") {
        if ($_POST["password"] == "changeme") {
            $token = sha1(rand(1,99999));
            print("Nice Job! You are authenticated<br/>");
            print("Here's your secret token: $token");
        }
    }
}
