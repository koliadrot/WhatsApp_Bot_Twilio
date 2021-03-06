EN:

WhatsApp Bot with Twilio

The main task of this bot, to respond to user requests, which can be easily added.
See repository - https://github.com/koliadrot/Telegram_Bot_Webhook

Due to a number of limitations of the WhatsApp messenger, providing api interface for ordinary enthusiast developers
is a difficult process. Therefore, various services are used, which are intermediaries
between users and messenger. One of them is Twilio.

When registering for this service, you get a trial account that will be spent in the process of working with this platform.
When reaching a zero balance on the account, the account will be blocked, until the account is replenished with real money.

Read in detail about all tools and tariffs of the Twilio platform at the link - https://www.twilio.com/docs/

To use your own brand name, phone number, and custom message templates, your account must first be approved by WhatsApp. Their approval process is currently limited.
The necessary section, to create your bot is on the link - https://www.twilio.com/console/sms/whatsapp
You will need to successfully configure the items: Learn, Sandbox.

1. Learn- this process consists of 5 steps, where you will need to send a message from the WhatsApp messenger to the specified number,
   make a few confirmations and complete the verification process of your number with the Twilio bot.
2. Sandbox - here you will need to insert ("WHEN A MESSAGE COMES IN") your *url address where the Twilio server will make POST requests.
   Also here you can add other participants to test your service.

*The bot itself was placed on the site of the service - https://www.pythonanywhere.com
The cost of the service is free, you only need to renew it every 3 months, it is also free!

RU: 

WhatsApp Бот с Twilio 

Главная задача этого бота, отвечать на запросы пользователей,которые могут быть легко добавлены.
Смотри хранилище(репозиторий) - https://github.com/koliadrot/Telegram_Bot_Webhook 

Из-за ряда ограничений мессенджера WhatsApp,предоставление api интерфейса для рядовых энтузиастов-разработчиков,
является затруднительным процессом. Поэтому используются различные сервисы "мурзилки", которые являются посредниками
между пользователями и мессенджером. Один из них это - Twilio.

При регистрации на этом сервисе, вы получаете пробный счет, который будет расходываться в процессе работы с этой платформой.
При достижении нулевого баланса на счете,аккаунт будет заблокирован, до пополнения счета реальными средствами.

Подробно читать про все инструменты и тарифы платформы Twilio по ссылке - https://www.twilio.com/docs/

Чтобы использовать собственную торговую марку, номер телефона и пользовательские шаблоны сообщений, ваша учетная запись должна быть сначала одобрена WhatsApp. Их процесс одобрения в настоящее время ограничен.

Нужный раздел, для создания вашего бота находится по ссылке - https://www.twilio.com/console/sms/whatsapp
Вам нужно будет успешно настроить пункты:Learn,Sandbox.

1. Learn- этот процесс состоит из 5 шагов,где нужно будет отправить сообщение с мессенджера WhatsApp на указанный номер,
   сделать несколько подтверждений и завершить процесс верификации вашего номера с ботом Twilio.
2. Sandbox - тут нужно будет вставить("WHEN A MESSAGE COMES IN") вашу url* адрес, куда будет сервер Twilio совершать POST запросы.
   Так же тут можно добавить других участников для тестирования вашего сервиса.

*Сам бот размещался на сайте сервиса - https://www.pythonanywhere.com
Стоимость услуги бесплатная, нужно только каждые 3 месяца продливать, это тоже бесплатно!
