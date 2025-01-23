FACTORY DESIGN PATTERN

Bir veritabanı yöneticisi uygulaması geliştirildiğini varsayalım. Uygulamanın temel
işlevi, farklı veri tabanlarına veri eklemek ve veri çekmek olacaktır. Ancak,uygulamayı
kullanan bazı müşteriler MySQL, bazıları ise Oracle veya MSSQL kullanmaktadır. Bu
uygulamada uygulamanın veritabanı türünden bağımsız bir şekilde çalışması
beklenmektedir.
Not: Uygulama, veritabanı türlerine göre farklı veritabanı yönetim sistemleri ile
bağlantı kurmalı ve veri okuma/yazma işlemleri yapmalıdır.
