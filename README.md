![Лого](https://github.com/xxanqw/hudoliy-resourcepack/blob/3e22022f440fbe8a61ce429501d7602c1b17a333/src/logo.png)  
# Ресурс-пак для серверу "ХУДОЛІЙ"


### Як змінювати:
 - Зпочатку клонуємо репозиторій  
 `git clone --recurse-submodules https://github.com/xxanqw/hudoliy-resourcepack.git`
 - Вносимо зміни до папки `pack`
 - Коли бажані зміни зроблено, запускаємо файл `PackerGUI-*` залежить від вашої ОС.  
 - На виході отримуємо `pack.zip` та `sha1.txt`
 - Комітимо та пушимо зміни до репозиторію, і додаємо `pack.zip` та `sha1.txt` до нового релізу (опис змін не обов'язковий).

### Як білдити програму для пакування:
 **[Все описано тут](https://github.com/xxanqw/hudoliy-resourcepack/tree/main/build)**

## ToDo's
 - [ ] Пофіксити Ubuntu 22.04.3 і менше
 - [ ] Зробити більш юзерфрендлі інтерфейс та код
 - [ ] Зменшити розмір виконуваного файлу
 - [ ] Знайти метод білдити для всіх ос одночасно
 - [ ] Зробити пакер основаним на веб, задля економії місця  
       *Тобто зробити так аби скачувався лише екзешнік і сам підтягував потрібні папки та файли без повного клону репозиторію*
 - [ ] Зробити пакер не тільки для худолія (тривале оновлення)

Скоро худолій оживе.... https://skill-issues.xserv.pp.ua
