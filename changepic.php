<?php
header("Cache-Control: no-store, no-cache, must-revalidate, max-age=0");
header("Cache-Control: post-check=0, pre-check=0", false);
header("Pragma: no-cache");
ini_set('max_execution_time', 0);
ini_set('memory_limit', '128M');
require './vendor/autoload.php';
\InstagramAPI\Instagram::$allowDangerousWebUsageAtMyOwnRisk = true;
$ig = new \InstagramAPI\Instagram();
$username = '';   #buraya instagram adinizi yazin, tirnaklari silmeyin!
$password = ''; #buraya sifrenizi girin, tirnaklari silmeyin!

try {
   echo  $ig->login($username, $password);
} catch (\Exception $e) {
	header("Refresh:5");
	die('Bir hata oluştu: ' . $e->getMessage());
}

$time='0';

while (true) {
	$newtime=date("h:i:sa");
	$timesec=substr($newtime,-4,-2);
	if ($timesec==58){
		try {
		   $ig->account->changeProfilePicture($imgpath.'image.png');
		} catch (\Exception $e) {
			header("Refresh:5");
			die('Bir hata oluştu: ' . $e->getMessage());		
	}}


}


?>
