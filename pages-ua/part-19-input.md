---
{}
---

__Placeholder_222 Частина 19 - Введення

Останні два уроки, сподіваємось, демонстрували необхідність зрілого підходу до обробки введення будь -якого серйозного додатку. Сьогодні ми створимо належну вхідну архітектуру для PICO, пов’язаного зі stdin __placeholder_65__ stdio. Почнемо зі створення __input.h__ наступним чином. __Placeholder_0__void input_proc (тип char, char* p_usb_char, char* p_usb_string, const __placeholder_48 __* p_usb_string_size);
void flush_input (char* p_usb_string);
__Placeholder_1__

Тут ми налаштовуємо наш заголовок введення __placeholder_42__ для вирішення параметів, про які ми обговорювали на останньому уроці. Ми також встановлюємо нашу функцію _flush \ _input_ для обробки очищення вхідного буфера після того, як він буде використаний для того, щоб він був чистим до отримання нового входу для іншого __placeholder_45__ до _input \ _proc_. Далі ми створимо наш __print__placeholder_52__ __as. __Placeholder_2__void print_proc (char* p_usb_char, char* p_usb_string);
__Placeholder_3__

Дуже просто ми збираємося пройти в масиві Char від абонента, щоб обробляти кожен char __placeholder_66__ char Array від абонента, щоб обробляти створення рядка. Далі ми створимо наш __input.c__ наступним чином. __Placeholder_4 __#включає & lt; stdio__placeholder_53 __ & gt;
__Placeholder_23__ включає & lt; string__placeholder_54 __ & gt;
__Placeholder_24__ включити "pico/stdlib__placeholder_55__"

__Placeholder_25__ Визначте нуль 0x30
__Placeholder_26__ Визначте дев'ять 0x39
__Placeholder_27__ Визначте період 0x2e
__Placeholder_28__ Визначте Capital_A 0x41
__Placeholder_29__ Визначте нижній_case_z 0x7a
__Placeholder_30__ Визначте Backspace 0x08
__Placeholder_31__ Визначте del 0x7f

void input_proc (тип char, char* p_usb_char, char* p_usb_string, const __placeholder_49 __* p_usb_string_size)
{
& nbsp; *p_usb_char = '\ 0';
& nbsp; *p_usb_char = getchar_timeout_us (0);
& nbsp; if ( *p_usb_char == backspace || *p_usb_char == del)
& nbsp; {
& nbsp; & nbsp; if (p_usb_string [0]! = '\ 0')
& nbsp; & nbsp; {
& nbsp; & nbsp; & nbsp; __Placeholder_74 __ ("\ b");
& nbsp; & nbsp; & nbsp; __Placeholder_75 __ ("");
& nbsp; & nbsp; & nbsp; __Placeholder_76 __ ("\ b");
& nbsp; & nbsp; & nbsp; P_USB_STRING [__ Ploadholder_38 __ (P_USB_STRING) -1] = '\ 0';
& nbsp; & nbsp; }
& nbsp; }
& nbsp; if (type == 'f')
& nbsp; {& nbsp;
& nbsp; & nbsp; Чар* період;
& nbsp; & nbsp; while (( *p_usb_char & gt; = Zero & amp; & amp; *p_usb_char & lt; = дев'ять) || *p_usb_char == період)
& nbsp; & nbsp; {
& nbsp; & nbsp; & nbsp; if (*p_usb_char == період)
& nbsp; & nbsp; & nbsp; & nbsp; період = strchr (p_usb_string, '.');
& nbsp; & nbsp; & nbsp; якщо (період == null) & nbsp;
& nbsp; & nbsp; & nbsp; {
& nbsp; & nbsp; & nbsp; & nbsp; if (__ Ploadholder_39 __ (P_USB_STRING) & lt; *P_USB_STRING_SIZE)
& nbsp; & nbsp; & nbsp; & nbsp; {
& nbsp; & nbsp; & nbsp; & nbsp; & nbsp; putchar (*p_usb_char);
& nbsp; & nbsp; & nbsp; & nbsp; & nbsp; strncat (P_USB_STRING, P_USB_CHAR, 1);
& nbsp; & nbsp; & nbsp; & nbsp; }
& nbsp; & nbsp; & nbsp; & nbsp; *p_usb_char = '\ 0';
& nbsp; & nbsp; & nbsp; }
& nbsp; & nbsp; & nbsp; інакше
& nbsp; & nbsp; & nbsp; & nbsp; перерва;
& nbsp; & nbsp; }
& nbsp; }
& nbsp; інакше, якщо (тип == 'd')
& nbsp; {& nbsp;
& nbsp; & nbsp; while ( *p_usb_char & gt; = Zero & amp; & amp; *p_usb_char & lt; = дев'ять)
& nbsp; & nbsp; {
& nbsp; & nbsp; & nbsp; if (__ Ploadholder_40 __ (P_USB_STRING) & lt; *P_USB_STRING_SIZE)
& nbsp; & nbsp; & nbsp; {
& nbsp; & nbsp; & nbsp; & nbsp; putchar (*p_usb_char);
& nbsp; & nbsp; & nbsp; & nbsp; strncat (P_USB_STRING, P_USB_CHAR, 1);
& nbsp; & nbsp; & nbsp; }
& nbsp; & nbsp; & nbsp; *p_usb_char = '\ 0';
& nbsp; & nbsp; }
& nbsp; }
& nbsp; інакше, якщо (тип == 's')
& nbsp; {& nbsp;
& nbsp; & nbsp; while ( *p_usb_char & gt; = capital_a & amp; & amp; *p_usb_char & lt; = lite_case_z)
& nbsp; & nbsp; {
& nbsp; & nbsp; & nbsp; if (__ placholder_41 __ (p_usb_string) & lt; *p_usb_string_size)
& nbsp; & nbsp; & nbsp; {
& nbsp; & nbsp; & nbsp; & nbsp; putchar (*p_usb_char);
& nbsp; & nbsp; & nbsp; & nbsp; strncat (P_USB_STRING, P_USB_CHAR, 1);
& nbsp; & nbsp; & nbsp; }
& nbsp; & nbsp; & nbsp; *p_usb_char = '\ 0';
& nbsp; & nbsp; }
& nbsp; }
}

void flush_input (char* p_usb_string)
{
& nbsp; P_USB_STRING [0] = '\ 0';
}
__Placeholder_5__

У цей момент все слід повністю зрозуміти з вищезазначеним. Якщо це __placeholder_82__, перегляньте останні два уроки. Далі ми створимо наш __print.c__ наступним чином. __Placeholder_6 __#включає & lt; stdio__placeholder_56 __ & gt;
__Placeholder_32__ включити "pico/stdlib__placeholder_57__"
__Placeholder_33__ включити "Input__placeholder_58__"

__Placeholder_34__ Визначте повернення 0x0d

void print_proc (char* p_usb_char, char* p_usb_string)
{
& nbsp; if (*p_usb_char == return)
& nbsp; {
& nbsp; & nbsp; if (p_usb_string [0] == '\ 0')
& nbsp; & nbsp; & nbsp; __Placeholder_77 __ ("\ n");
& nbsp; & nbsp; інакше
& nbsp; & nbsp; & nbsp; __Placeholder_78 __ ("\ n%s \ n", p_usb_string);
& nbsp; & nbsp; flush_input (p_usb_string);
& nbsp; }
}
__Placeholder_7__

Тут ми приносимо наш Char __placeholder_67__. Нарешті ми створимо наш __main.c__ наступним чином. __Placeholder_8 __#включити & lt; stdio__placeholder_59 __ & gt;
__Placeholder_35__ включити "pico/stdlib__placeholder_60__"
__Placeholder_36__ включити "print__placeholder_61__"
__Placeholder_37__ Включення "Input__placeholder_62__"

__Placeholder_50__ main ()
{
& nbsp; stdio_init_all ();

& nbsp; const __placeholder_51__ usb_string_size = 100;
& nbsp; char usb_char;
& nbsp; usb_char = '\ 0';
& nbsp; char usb_string [usb_string_size];
& nbsp; usb_string [0] = '\ 0';
& nbsp; & nbsp;
& nbsp; в той час як (1)
& nbsp; {& nbsp; & nbsp;
& nbsp; & nbsp; input_proc ('f', & amp; usb_char, usb_string, & amp; usb_string_size);
& nbsp; & nbsp; print_proc (& amp; usb_char, usb_string);
& nbsp; }

& nbsp; повернення 0;
}
__Placeholder_9__

Тут ми просто встановлюємо нашу вхідну процедуру для обробки введення поплавця. Давайте зробимо новий DIR & nbsp; __ 0x07 \ _input __ & nbsp; __ ploadholder_70__ __placeholder_47__ Наші & nbsp; __ cmakelists.txt __ & nbsp; __ placholder_43__ в ньому. __Placeholder_10__cmake_minimum_required (версія 3.13)

включити (pico_sdk_import.cmake)

Проект (test_project c cxx asm)
set (cmake_c_standard 11) & nbsp;
set (cmake_cxx_standard 17) & nbsp;
set (cmake_c_flags_release "$ {cmake_c_flags_release}")
set (cmake_cxx_flags_release "$ {cmake_cxx_flags_release}")
pico_sdk_init ()

add_executable (головне
& nbsp; main__placeholder_79__
& nbsp; print__placeholder_80__
& nbsp; Input__placeholder_81__
)

pico_enable_stdio_usb (основний 1)
pico_enable_stdio_uart (головна 0)
pico_add_extra_outputs (main)

Target_Link_Libraries (основні PICO_STDLIB HARDWARE_I2C)

add_custom_target (Flash
& nbsp; & nbsp; Команда cp main.uf2/volumes/rpi-rp2/
& nbsp; & nbsp; Залежить від основного
)
__Placeholder_11__

Далі нам потрібно скопіювати & nbsp; __ pico \ _sdk \ _import.cmake __ & nbsp; __ ploadholder_44__ із зовнішньої папки в & nbsp; __ pico-sdk __ & nbsp; інсталяція до & nbsp; __ 0x07 \ _input __ & nbsp; __Placeholder_12__cp ../pico-sdk/external/pico_sdk_import.cmake. __Placeholder_13__

Нарешті ми готові до будівництва. __Placeholder_14__mkdir
Комплект компакт -дисків
Експорт PICO_SDK_PATH = ../../PICO-SDK
cmake .. зробити
зробити спалах
__Placeholder_15__

Я додав у MakeFile променевий режим, щоб заощадити нам час від копіювання до піко. Не забудьте спочатку поставити PICO в режим спалаху. Тоді нам потрібно знайти USB -накопичувач, щоб ви могли зробити наступне. __Placeholder_16__ls /__ ploadholder_63 __ /tty. __Placeholder_17__

Натисніть вкладку, щоб знайти накопичувач __placeholder_71__, тоді в моєму випадку я буду використовувати & nbsp; __ екран __ & nbsp; для підключення. __Placeholder_18__screen /__placeholder_64__/tty.usbmodem00000000001
__Placeholder_19__

Бум! Тепер ви побачите, що зможете ввести числа __placeholder_72__ лише один десятковий пункт. Ми належним чином обробляємо зворотну дію __placeholder_73__, коли ви досягнете максимуму 100 Chars, це буде __placeholder_83__ дозволить вам набрати далі. Нарешті він відручує те, що ви набрали. __Placeholder_20__32.3333
32.3333
32.111111111
32.111111111
7.99999003902930420384802384082304820384028342340284923840238948230482938429034823948293849023849223
7.99999003902930420384802384082304820384028342340284923840238948230482938429034823948293849023849223
__Placeholder_21__

На нашому наступному уроці ми будемо налагодити.