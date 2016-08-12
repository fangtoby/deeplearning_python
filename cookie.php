<?php
/**
 * author       : dot.f <fangyanliang@yiban.cn>
 * createTime   : 2016/8/10 11:41
 * description  :
 */

//模拟登录
function login_post($url, $cookie, $post) {
    $curl = curl_init();//初始化curl模块
    curl_setopt($curl, CURLOPT_URL, $url);//登录提交的地址
    curl_setopt($curl, CURLOPT_HEADER, 0);//是否显示头信息
    curl_setopt($curl, CURLOPT_RETURNTRANSFER, 0);//是否自动显示返回的信息
    curl_setopt($curl, CURLOPT_COOKIEJAR, $cookie); //设置Cookie信息保存在指定的文件中
    curl_setopt($curl, CURLOPT_POST, 1);//post方式提交
    curl_setopt($curl, CURLOPT_POSTFIELDS, http_build_query($post));//要提交的信息
    curl_exec($curl);//执行cURL
    curl_close($curl);//关闭cURL资源，并且释放系统资源
}
//登录成功后获取数据
function get_content($url, $cookie,$post) {
    $ch = curl_init();
    curl_setopt($ch, CURLOPT_URL, $url);
    curl_setopt($ch, CURLOPT_HEADER, 0);
    curl_setopt($ch, CURLOPT_RETURNTRANSFER, 1);
    curl_setopt($ch, CURLOPT_COOKIEFILE, $cookie); //读取cookie
    curl_setopt($ch, CURLOPT_POSTFIELDS, http_build_query($post));//要提交的信息
    $rs = curl_exec($ch); //执行cURL抓取页面内容
    curl_close($ch);
    return $rs;
}

$cookie_file = dirname(__FILE__) . '/cookie.txt';
$login_url  = 'http://service.js.10086.cn/actionDispatcher.do';
$get_url = 'http://service.js.10086.cn/my/actionDispatcher.do';

$post = array(
    "userLoginTransferProtocol"=>"https",
    "redirectUrl"=>"index.html",
    "reqUrl"=>"login",
    "busiNum"=>"LOGIN",
    "operType"=>"0",
    "passwordType"=>"1",
    "isSavePasswordVal"=>"0",
    "isSavePasswordVal_N"=>"1",
    "currentD"=>"1",
    "loginFormTab"=>"http",
    "loginType"=>"1",
    "phone-login"=>"on",
    "mobile"=>"18860975543",
    "city"=>"NJDQ",
    "password"=>"880920",
    "verifyCode"=>"",
);

login_post($login_url, $cookie_file, $post);

$sFile = file_get_contents($cookie_file);

echo $sFile;

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

echo get_content($get_url,$cookie_file,$data);



