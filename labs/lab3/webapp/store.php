<?php
header("X-XSS-Protection: 0;");
?>
<html>
<head>
<title>The Store</title>
</head>
<body>
<h1>The Store</h2>
<?php

function showForm() {
    print <<< EOL
<form method="post">
<table cellpadding="3" cellspacing="3">
<tr>
<td><b>Price:</b></td>
<td>$1.25</td>
</tr><tr>
<td><b>Select Quantity:</b></td>
<td>
<select name="qty">
<option value="1">1</option>
<option value="2">5</option>
<option value="3">10</option>
</select>
</td>
</tr><tr>
<td><b>Mailing Address:</b></td>
<td>
<textarea name="adx" id="adx" rows="4" cols="60"></textarea>
</td>
</tr><tr>
<td colspan="2" align="right">
<button type="submit">Purchase</button>
</td>
</tr>
</table>
<input type="hidden" name="price" value="1.25"/>
</form>
EOL;
}

function showPurchase() {
    $qty = $_POST["qty"];
    $price = $_POST["price"];
    $adx = $_POST["adx"];
    $total = $qty * $price;

    print <<< EOL
<h2>Thank you for your purchase!</h2>
<table cellpadding="3" cellspacing="3">
<tr>
<td><b>Qty:</b></td>
<td>$qty</td>
</tr><tr>
<td><b>Price:</b></td>
<td>\$$price</td>
</tr><tr>
<td><b>Total:</b></td>
<td>\$$total</td>
</tr><tr>
<td><b>Address</b></td>
<td><pre><h3>$adx</h3></pre></td>
</tr>
</table>
EOL;
}
?>

<?php
    if (! isset($_POST["qty"])) {
        showForm();
    } else {
        showPurchase();
    }
?>
</body>
</html>
