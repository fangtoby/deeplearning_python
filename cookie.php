<?php
/**
 * author       : dot.f <fangyanliang@yiban.cn>
 * createTime   : 2016/8/10 11:41
 * description  :
 */

$data = array(
    'reqUrl' => "MY_QDCXQueryNew",
    'busiNum' => "QDCX",
    'queryMonth' => "201607",
    'queryItem' => "1",
    'qryPages'=> "1:1002:-1",
    'qryNo' =>"1",
    'operType' =>"3",
    'queryBeginTime' =>"2016-08-01",
    'queryEndTime' => "2016-08-10",
);

$data = http_build_query($data);

$opts = array(
    'http'=>array(
        'method'=>"POST",
        'header'=>"Content-type: application/x-www-form-urlencoded\r\n".
            "Content-length:".strlen($data)."\r\n" .
            "Host:service.js.10086.cn"."\r\n" .
            "Origin:http://service.js.10086.cn"."\r\n" .
            "Referer:http://service.js.10086.cn/my/MY_QDCX.html"."\r\n" .
            "User-Agent:Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.106 Safari/537.36"."\r\n" .
            "X-Requested-With:XMLHttpRequest"."\r\n" .
            "Cookie: AlteonP=AnndQmddqMBdi/VjIFoZbQ$$; so_dl234=\"\"; yjcxFlag=1; WTCX_MY_ZHYEJYXQ=MY_ZHYEJYXQ+1470798252502; wt_dl123=Mtco2rIvRUMHk+Mp53ovbRJzT5UY7jJK; CmLocation=250|250; nulluserQuitCountDayALL10=1; nulluserQuitCountMonthALL7=1; nulluserQuitFlag10=1; forwardActSmqllNew=1; login_error_number_https=18860975543; login_error_loginType_https=1; login_error_passwordType_https=1; autoLogin=NN/R7QvTMpBjkX/ZgDF6nGwA3ZJfIX2c; last_success_login_mobile=18860975543; onedayonetime=1; AlteonP=AsPcU2ddqMBEFHMciGK5Gw$$; cmjsSSOCookie=0CCBEFD6A3264A18A156CED3830B9716@js.ac.10086.cn; cmtokenid=0CCBEFD6A3264A18A156CED3830B9716@js.ac.10086.cn; WTCX_MY_INDEX=MY_INDEX+1470823491725; needShow=1; WTCX_MY_WDTC=MY_WDTC+1470824456082; JSESSIONID=wnNPXrCPV7QdQGCq6xVMmST957jvpfZQKrwGhKm71JCdhGvmpzZs!1980800848; CmWebtokenid=18860975543,js; CmProvid=js; WT_FPC=id=2d7388b25365f5f5dcf1470797470989:lv=1470825204584:ss=1470823491906; topUserMobile=18860975543; city=NTDQ; WTCX_MY_QDCX=MY_QDCX+1470825204776",
        'content' => $data,
    )
);

$cxContext = stream_context_create($opts);

$sFile = file_get_contents("http://221.178.251.154/my/actionDispatcher.do", false, $cxContext);

echo $sFile;





$cookie_file = tempnam('./temp','cookie');
$login_url  = 'http://service.js.10086.cn/login.html?url=index.html';
$post_fields = 'userLoginTransferProtocol=https&redirectUrl=index.html&reqUrl=login&busiNum=LOGIN&operType=0&passwordType=1&isSavePasswordVal=0&isSavePasswordVal_N=1&currentD=1&loginFormTab=http&loginType=1&phone-login=on&mobile=18860975543&city=NJDQ&password=880920&verifyCode=';
$ch = curl_init($login_url);
curl_setopt($ch, CURLOPT_HEADER, 0);
curl_setopt($ch, CURLOPT_RETURNTRANSFER, 1);
curl_setopt($ch, CURLOPT_POST, 1);
curl_setopt($ch, CURLOPT_POSTFIELDS, $post_fields);
curl_setopt($ch, CURLOPT_COOKIEJAR, $cookie_file);
curl_exec($ch);
curl_close($ch);

/*
$data = array(
    'reqUrl' => "MY_QDCXQueryNew",
    'busiNum' => "QDCX",
    'queryMonth' => "201607",
    'queryItem' => "1",
    'qryPages'=> "1:1002:-1",
    'qryNo' =>"1",
    'operType' =>"3",
    'queryBeginTime' =>"2016-08-01",
    'queryEndTime' => "2016-08-10",
);
$data = http_build_query($data);
$opts = array(
    'http'=>array(
        'method'=>"POST",
        'header'=>"Content-type: application/x-www-form-urlencoded\r\n".
            "Content-length:".strlen($data)."\r\n" .
            "Host:service.js.10086.cn"."\r\n" .
            "Origin:http://service.js.10086.cn"."\r\n" .
            "Referer:http://service.js.10086.cn/my/MY_QDCX.html"."\r\n" .
            "User-Agent:Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.106 Safari/537.36"."\r\n" .
            "X-Requested-With:XMLHttpRequest"."\r\n" .
            "Cookie: ".file_get_contents($cookie_file)."",
        'content' => $data,
    )
);
$cxContext = stream_context_create($opts);
$sFile = file_get_contents("http://service.js.10086.cn/my/actionDispatcher.do", false, $cxContext);
echo $sFile;
*/
