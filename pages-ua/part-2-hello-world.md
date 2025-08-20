---
{}
---

__Placeholder_27__ Частина 2 - Привіт світ

Сьогодні ми будемо висвітлювати основну установку для створення власних проектів на Raspberry Pi Pico. Всередині нашої папки __pico__ дозволяє створити __0x02 \ _pico \ _hello \ _world__ папка поряд із __pico-sdk__ __placeholder_42__ __pico-example__ папки. __Placeholder_0__mkdir 0x02_pico_hello_world
CD 0x02_PICO_HELLO_WORLD
__Placeholder_1__

Давайте створимо наш VIM __0x02 \ _Hello \ _world.c__ __placeholder_29__. __Placeholder_2__vim 0x02_hello_world__placeholder_55__
__Placeholder_3__

Давайте __placeholder_35__ наступне. __Placeholder_4 __#включити & lt; stdio__placeholder_38 __ & gt;
__Placeholder_28__ включити "pico/stdlib__placeholder_39__"

__Placeholder_36__ main () & nbsp;
{	
& nbsp; stdio_init_all ();

& nbsp; в той час як (1) & nbsp;
& nbsp; {
& nbsp;   __Placeholder_53 __ ("Привіт світ! \ N");

& nbsp; & nbsp; Sleep_ms (1000);
& nbsp; }
    
  повернення 0;
}
__Placeholder_5__

Ми спочатку обробляємо логіку, щоб ініціювати всі стандартні введення __placeholder_43__. __Placeholder_6 __ & nbsp; & nbsp; stdio_init_all ();
__Placeholder_7__

Нарешті ми друкуємо _ "Привіт світ!" _ Кожні секунди до стандартного виходу в нескінченній петлі. __Placeholder_8 __ & nbsp; & nbsp; в той час як (1) & nbsp;
& nbsp; & nbsp; {
& nbsp; & nbsp;   __Placeholder_54 __ ("привіт світ! \ N");

& nbsp; & nbsp; & nbsp; Sleep_ms (1000);
& nbsp; & nbsp; }
__Placeholder_9__

Тоді ми після успіху _Return 0_, щоб вказати на успіх, оскільки наша функція _Main_ - це __placeholder_37__. Це технічно необхідна __placeholder_57__, але хороша практика. __Placeholder_10__ повернення 0;
__Placeholder_11__

Робота з __cmake__ значно допомагає в процесі побудови для наших проектів. Спочатку нам потрібно зробити __cmakelists.txt__ __placeholder_30__. __Placeholder_12__cmake_minimum_required (версія 3.13)

включити (pico_sdk_import.cmake)

Проект (test_project c cxx asm)
SET (CMAKE_C_STANDARD 11)
set (cmake_cxx_standard 17)
pico_sdk_init ()

add_executable (0x02_hello_world
  0x02_hello_world__placeholder_56__________________
)

pico_enable_stdio_usb (0x02_hello_world 1)

pico_add_extra_outputs (0x02_hello_world)

Target_Link_Libraries (0x02_hello_world pico_stdlib)
__Placeholder_13__

Далі нам потрібно скопіювати __pico \ _sdk \ _import.cmake__ __placeholder_31__ із зовнішньої папки у встановленні __pico-sdk__ до __0x02 \ _hello \ _world__ проект. __Placeholder_14__cp ../pico-sdk/external/pico_sdk_import.cmake. __Placeholder_15__

Нарешті ми готові до будівництва. __Placeholder_16__mkdir
Комплект компакт -дисків
Експорт PICO_SDK_PATH = ../../PICO-SDK
cmake .. зробити
__Placeholder_17__

Це створить ряд файлів __placeholder_44__ ті, на яких ми будемо зосереджуватися, - це __. Elf__ __placeholder_32__, коли мова йде про налагодження __placeholder_45__ хакерство, що є повним результатом програми, можливо, включаючи інформацію про налагодження __placeholder_46__ __. Форма, яку ви можете перетягнути -__ ploadholder_48 __- потрапляйте на плату RP2040, коли вона встановлена як USB-накопичувач. Я знайшов час, щоб підключити кнопку скидання на PICO, щоб я робив __placeholder_58__, довелося продовжувати відключення в USB __placeholder_49__, натискаючи на завантаження кожного разу, коли мені потрібно повторно переробити, тому ось схема такого. __Placeholder_18____Placeholder_19____Placeholder_20__

Щоб спалахнути натисканням зовнішньої кнопки __placeholder_50__, поки вона ще натиснута, натисніть Bootsel на платі, а потім відпустіть Bootsel __placeholder_51__, нарешті, відпустіть зовнішню кнопку. Потім просто скопіюйте __. UF2__ __Placeholder_34__ на диск. __Placeholder_21__cp 0x02_hello_world.uf2 /volumes /rpi-rp2
__Placeholder_22__

Тоді нам потрібно знайти USB -накопичувач, щоб ви могли зробити наступне. __Placeholder_23__ls /__ ploadholder_40 __ /tty. __Placeholder_24__

Натисніть вкладку, щоб знайти накопичувач __placeholder_52__, тоді в моєму випадку я буду використовувати __screen__ для підключення. __Placeholder_25__screen /__placeholder_41__/tty.usbmodem00000000001
__Placeholder_26__

Ура! Ви повинні бачити: "Привіт світ!" до стандартного виходу щосекунди. На нашому наступному уроці ми будемо налагодити __. Elf__ бінарний у __radare2__.