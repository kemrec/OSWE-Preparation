# Dangerous Functions and Situations in PHP.

<--------Acquire User supplied input------>

$_GET and $HTTP_GET_VARS //parameter submitted in query string Ex: $_GET['username']
$_POST and $HTTP_POST_VARS //parameter submitted in request body string Ex: $_POST['username']
$_COOKIE and $HTTP_COOKIE_VARS //cookies submitted in the request Ex: $_COOKIE['name']
$_REQUEST //contains all item the item in $_GET, $_POST and $_COOKIE
$_FILES and $HTTP_POST_FILES //contains file uploaded in the request
$_SERVER['PHP_SELF'] //contains current executing page
$_SESSION //store session value Ex: $_SESSION['username'] = $_POST['username']

<---------Command Exection----------->

exec - Returns last line of commands output
passthru - Passes commands output directly to the browser
system - Passes commands output directly to the browser and returns last line
shell_exec - Returns commands output
popen - Opens read or write pipe to process of a command
proc_open - Similar to popen() but greater degree of control
pcntl_exec - Executes a program

<----------Code Execution------------------>

eval()
assert() - identical to eval()
preg_replace('/.*/e',...) //e does an eval() on the match
create_function()
call_user_func()
call_user_func_array()
EX: eval("echo " . $_REQUEST["user_name"] . ";");

<-----------XSS------------->

echo "Welcome " . $_GET['user_input'];
<?= $_GET['user_input'] ?>

<-----------Directory Traversal & SSRF----->

fopen() //Opens file or URL
readfile() //Read a file
file() // Reads entire file into an array
fgets() //Read first line
fpassthru() //Read from the current position in file - until EOF, and then write the result to the output buffer
gzopen() //
unlink() //delete a file
file_get_contents() //Reads entire file into a string
parse_ini_file()
fwrite() //Write a open file
fread() // Read a open file
Ex 1: $path = $_GET["file"];
$file = fopen($path, "r");
$line = fgets($file);

<-------------File Upload------------->

The getimagesize() function will check if it is an image and will check “mime” to verify image type.

Insecure Configuration :

 <FilesMatch ".+\.ph(p([3457s]|\-s)?|t|tml)">  SetHandler application/x-httpd-php  </FileMatch>

Secure Configuration :

 <FilesMatch ".+\.ph(p([3457s]|\-s)?|t|tml)$">  SetHandler application/x-httpd-php  </FileMatch>

move_uploaded_file()

<-------------SQL Injection------------> 
Following function used to query database

mysql_query //use in MySQL
mssql_query //use in MsSQL
pg_query //use in Postgress
Ex:
$username = $_POST["username"];
$password = $_POST["password"];
$sql="SELECT * FROM users WHERE username = '$username' AND password = '$password'";
$result = mysql_query($sql, $link);
.
<-----------LFI & RFI---------------------->

include() //include remote/local PHP file into PHP file.
include_once()
require() //same as include but stop execution in case of error
require_once()
EX: $user_prof = $_GET['user_profile'];
$path = "./user/" . $user_prof;
$file = require($path);

<------------Serialize & Deserialize-------->

serialize()
unserialize()
Ex: $input = $_POST['data']; //a:3:{i:0;s:4:"Emre";i:1;s:8:"Security";i:2;s:6:"Expert";}
var c = unserialize($input);

<---------- Info function------------------->

phpinfo()
