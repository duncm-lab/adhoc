$login = New-Object System.Net.NetworkCredential("duncm53@gmail.com", "")

$smtp = New-Object System.Net.Mail.SmtpClient('smtp.gmail.com', 587)
$smtp.EnableSsl = 1
$smtp.UseDefaultCredentials = 0
$smtp.Credentials = $login



function sendMessage($to, $from, $subject, $body){
    $message = New-Object System.Net.Mail.MailMessage($from, $to, $subject, $body)
    $smtp.Send($message)
}




