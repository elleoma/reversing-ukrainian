---
{}
---

__Placeholder_33__ Частина 20 - Налагодження введення

Сьогодні ми будемо налагодити нашу функцію введення. Давайте розглянемо наш код. Огляд & nbsp; __ input.c __ & nbsp; наступним чином. __Placeholder_0 __#включити & lt; stdio__placeholder_62 __ & gt;
__Placeholder_34__ включає & lt; string__placeholder_63 __ & gt;
__Placeholder_35__ включити "pico/stdlib__placeholder_64__"

__Placeholder_36__ Визначте нуль 0x30
__Placeholder_37__ Визначте дев'ять 0x39
__Placeholder_38__ Визначте період 0x2e
__Placeholder_39__ Визначити Capital_A 0x41
__Placeholder_40__ Визначте нижній_case_z 0x7a
__Placeholder_41__ Визначте Backspace 0x08
__Placeholder_42__ Визначте del 0x7f

void input_proc (тип char, char* p_usb_char, char* p_usb_string, const __placeholder_59 __* p_usb_string_size)
{
& nbsp; *p_usb_char = '\ 0';
& nbsp; *p_usb_char = getchar_timeout_us (0);
& nbsp; if ( *p_usb_char == backspace || *p_usb_char == del)
& nbsp; {
& nbsp; & nbsp; if (p_usb_string [0]! = '\ 0')
& nbsp; & nbsp; {
& nbsp; & nbsp; & nbsp; __Placeholder_86 __ ("\ b");
& nbsp; & nbsp; & nbsp; __Placeholder_87 __ ("");
& nbsp; & nbsp; & nbsp; __Placeholder_88 __ ("\ b");
& nbsp; & nbsp; & nbsp; P_USB_STRING [__ Ploadholder_50 __ (P_USB_STRING) -1] = '\ 0';
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
& nbsp; & nbsp; & nbsp; & nbsp; if (__ Ploadholder_51 __ (P_USB_STRING) & lt; *P_USB_STRING_SIZE)
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
& nbsp; & nbsp; & nbsp; if (__ placholder_52 __ (p_usb_string) & lt; *p_usb_string_size)
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
& nbsp; & nbsp; & nbsp; if (__ Ploadholder_53 __ (P_USB_STRING) & lt; *P_USB_STRING_SIZE)
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
__Placeholder_1__

Перегляньте наші & nbsp; __ print.c __ & nbsp; наступним чином. __Placeholder_2 __#включити & lt; stdio__placeholder_65 __ & gt;
__Placeholder_43__ включити "pico/stdlib__placeholder_66__"
__Placeholder_44__ включити "input__placeholder_67__"

__Placeholder_45__ Визначте повернення 0x0d

void print_proc (char* p_usb_char, char* p_usb_string)
{
& nbsp; if (*p_usb_char == return)
& nbsp; {
& nbsp; & nbsp; if (p_usb_string [0] == '\ 0')
& nbsp; & nbsp; & nbsp; __Placeholder_89 __ ("\ n");
& nbsp; & nbsp; інакше
& nbsp; & nbsp; & nbsp; __Placeholder_90 __ ("\ n%s \ n", p_usb_string);
& nbsp; & nbsp; flush_input (p_usb_string);
& nbsp; }
}
__Placeholder_3__

Перегляньте наші & nbsp; __ main.c __ & nbsp; наступним чином. __Placeholder_4 __#включити & lt; stdio__placeholder_68 __ & gt;
__Placeholder_46__ включити "pico/stdlib__placeholder_69__"
__Placeholder_47__ включити "print__placeholder_70__"
__Placeholder_48__ Включення "Input__placeholder_71__"

__Placeholder_60__ main ()
{
& nbsp; stdio_init_all ();

& nbsp; const __placeholder_61__ usb_string_size = 100;
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
__Placeholder_5__

Давайте розберемося в нашому налагоджувачі. __Placeholder_6__radare2 -w __placeholder_93__ -b 16 main .__ ploadholder_49__
__Placeholder_7__

Давайте автоматично проаналізуємо. __Placeholder_8__aaaa
__Placeholder_9__

Давайте прагнемо до головного. __Placeholder_10__s main
__Placeholder_11__

Перейдемо у візуальний режим, ввівши & nbsp; __ v __ & nbsp; __ ploadholder_72__ тоді & nbsp; __ p __ & nbsp; двічі, щоб дістатися до хорошого подання налагоджувача. Спочатку ми оглядаємо _main_. __Placeholder_12____Placeholder_13____placeholder_14__

Ми бачимо наш _stdio \ _init \ _all_ __placeholder_56__, який налаштовує io __placeholder_73__ ми бачимо _0x64_ на _r3_, що є нашим переміщенням 100 десятків для встановлення _usb \ _string \ _size _ і ми створимо _usb \ _ chart _0_ __placeholder_75__ Нарешті _USB \ _string_ __placeholder_76__ init to _0_. Давайте подивимось на нашу функцію _print \ _proc_. __Placeholder_15____Placeholder_16____Placeholder_17__

Спочатку ми перевіряємо, чи наш вказівник на USB \ _char __placeholder_54__ _p \ _USB \ _Char_ дорівнює _RETURN_ КЛЮЧ __PLAPYHOLDER_55__ _0xd_ __placeholder_77__, якщо це гілка. Потім ми повторюємо _p \ _USB \ _string_, поки не натиснемо Null Terminator __placeholder_78__, тоді __placeholder_57__ Наша _printf _function, яка, як ми бачимо тут, є обгорткою для функції c __placeholder_91__. Нарешті _flush \ _input_. Наша функція _input \ _proc_ трохи складніша. __Placeholder_18____Placeholder_19____Placeholder_20__

Тут ми використовуємо функцію g_etchar \ _timeout \ _us_ __placeholder_79__ обробляти _backspace_ __placeholder_80__ _delete_ клавіш. __Placeholder_21____Placeholder_22____Placeholder_23__

Тоді ми __placeholder_58__ Наш _putchar _wrapper проти_ 0_ __placeholder_81__ _9_ __placeholder_82__ Перевірте _strlen_ __placeholder_83__ належним чином побудуємо нашу рядок за допомогою _strncat_. __Placeholder_24____Placeholder_25____Placeholder_26__

Потім ми правильно обробляємо нашу логіку _period_, щоб переконатися, що лише один _period _IS, введений як номер плаваючої точки, може __placeholder_92__ обробляти 2 періоди. __Placeholder_27____Placeholder_28____Placeholder_29__

Потім ми правильно обробляємо свою петлю. Нарешті, у нас є функція _flush \ _input_. __Placeholder_30____Placeholder_31____Placeholder_32__

Тут ми просто промиваємо вхідний буфер, встановивши _p \ _USB \ _string_ на нульовий char. Це була більша сесія налагодження, тому, будь ласка, знайдіть свій час __placeholder_84__ Порівняйте Асамблею з джерелом, щоб ви могли дійсно зрозуміти кожен абзац, коли я його тут висвітлюю. Це підводить нас до кінця нашої початкової навчальної подорожі. У цій подорожі ми зробили 197 кроків разом через кілька різних архітектур. Настав ваша черга, щоб перенести цю підготовку на практиці __placeholder_85__ робити великі справи! Ця книга буде вашим довідником, коли ви стикаєтесь з викликами, проте немає нічого, що ви не можете досягти!