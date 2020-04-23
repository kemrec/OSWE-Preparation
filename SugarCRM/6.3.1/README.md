# SugarCRM 6.3.1 Php unserialize() PHP code execution

There is a php class file to use in exploit python code.

Exploit Exp:

The dangerous unserialize() exists in the 'include/MVC/View/views/view.list.php' script, which is called with user controlled data from the 'current_query_by_page'
parameter. The exploit abuses the __destruct() method from the SugarTheme class to write arbitrary PHP code to a 'pathCache.php' on the web root.
