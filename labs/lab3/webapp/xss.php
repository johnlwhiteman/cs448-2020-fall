<?php
header("X-XSS-Protection: 0;");
//header("X-XSS-Protection: 1;");
//header("X-XSS-Protection: 1; mode=block");
?>
<html>
<head>
<title>XSS Test</title>
</head>
<body>
<h1>XSS Test</h1>
<pre>Try: &lt;script&gt; alert('hello');&lt;/script&gt;</pre>
<form method="get">
<table>
<tr>
<?php
if (isset($_REQUEST["txt"])) {
    print <<< EOL
<td>
<textarea name="txt" id="txt" rows="4" cols="60">$_REQUEST[txt]</textarea>
</td>
EOL;

} else {
    print <<< EOL
<td>
<textarea name="txt" id="txt" rows="4" cols="60"></textarea>
</td>
EOL;
}
?>
</tr><tr>
<td align="right">
<button type="submit">Submit</button>
</tr>
</table>
</form>
<!-- XSS happens here -->
<p><?php print($_REQUEST["txt"]); ?></p>
</pre>
</body>
</html>
