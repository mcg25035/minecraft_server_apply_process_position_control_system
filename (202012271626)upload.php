<?php
# 檢查檔案是否上傳成功
if ($_FILES['my_file']['error'] === UPLOAD_ERR_OK)
{

  # 檢查檔案是否已經存在
  if (file_exists('/home/runner/CityofUniversefileserver/' . $_FILES['my_file']['name']))
  {
    echo '伺服端已有相同檔名的檔案，請換一個檔名在上傳。<br/><a href=index.php>點我</a>回到上傳頁面';
  }
  else
  {
    if(strpos($_FILES['my_file']['name'],' ') == true)
    {
    echo '檔案名稱內包含空格，請換一個檔名上傳';
    }
    else
    {
    $file = $_FILES['my_file']['tmp_name'];
    $dest = '/home/runner/CityofUniversefileserver/' . $_FILES['my_file']['name'];
    echo '檔案上傳成功,請回到discord群職位申請頻道輸入<br/>claimfile ' . $_FILES['my_file']['name'];
    # 將檔案移至指定位置
    move_uploaded_file($file , $dest);
    }
  }
} else {
  echo "你的檔案超過2MB或小於0MB,無法上傳<br/><a href=index.php>點我</a>回到上傳頁面:";
}
?>
