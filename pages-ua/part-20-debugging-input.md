## Частина 20 - Дебагування Вхідних Даних

Сьогодні ми дебагуватимемо нашу функцію вхідних даних. Давайте переглянемо свій код.

Перегляньте файл __input.c__ наступним чином.

<pre spellcheck="false">#include &lt;stdio.h&gt;
#include &lt;string.h&gt;
#include "pico/stdlib.h"

#define ZERO 0x30
#define NINE 0x39
#define PERIOD 0x2e
#define CAPITAL_A 0x41
#define LOWER_CASE_Z 0x7a
#define BACKSPACE 0x08
#define DEL 0x7f

void input_proc(char type, char* p_usb_char, char* p_usb_string, const XyZ9PlH14ZuK8* p_USB_STRING_SIZE)
{
&nbsp; *p_usb_char = '\0';
&nbsp; *p_usb_char = getchar_timeout_us(0);
&nbsp; if(*p_usb_char == BACKSPACE || *p_usb_char == DEL)
&nbsp; {
&nbsp; &nbsp; if(p_usb_string[0] != '\0')
&nbsp; &nbsp; {
&nbsp; &nbsp; &nbsp; printf("\b");
&nbsp; &nbsp; &nbsp; printf(" ");
&nbsp; &nbsp; &nbsp; printf("\b");
&nbsp; &nbsp; &nbsp; p_usb_string[strlen(p_usb_string)-1] = '\0';
&nbsp; &nbsp; }
&nbsp; }
&nbsp; if(type == 'f')
&nbsp; {&nbsp;
&nbsp; &nbsp; char* period;
&nbsp; &nbsp; while((*p_usb_char &gt;= ZERO &amp;&amp; *p_usb_char &lt;= NINE) || *p_usb_char == PERIOD)
&nbsp; &nbsp; {
&nbsp; &nbsp; &nbsp; if(*p_usb_char == PERIOD)
&nbsp; &nbsp; &nbsp; &nbsp; period = strchr(p_usb_string, '.');
&nbsp; &nbsp; &nbsp; if(period == NULL)&nbsp;
&nbsp; &nbsp; &nbsp; {
&nbsp; &nbsp; &nbsp; &nbsp; if(strlen(p_usb_string) &lt; *p_USB_STRING_SIZE)
&nbsp; &nbsp; &nbsp; &nbsp; {
&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; putchar(*p_usb_char);
&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; strncat(p_usb_string, p_usb_char, 1);
&nbsp; &nbsp; &nbsp; &nbsp; }
&nbsp; &nbsp; &nbsp; &nbsp; *p_usb_char = '\0';
&nbsp; &nbsp; &nbsp; }
&nbsp; &nbsp; &nbsp; else
&nbsp; &nbsp; &nbsp; &nbsp; break;
&nbsp; &nbsp; }
&nbsp; }
&nbsp; else if(type == 'd')
&nbsp; {&nbsp;
&nbsp; &nbsp; while(*p_usb_char &gt;= ZERO &amp;&amp; *p_usb_char &lt;= NINE)
&nbsp; &nbsp; {
&nbsp; &nbsp; &nbsp; if(strlen(p_usb_string) &lt; *p_USB_STRING_SIZE)
&nbsp; &nbsp; &nbsp; {
&nbsp; &nbsp; &nbsp; &nbsp; putchar(*p_usb_char);
&nbsp; &nbsp; &nbsp; &nbsp; strncat(p_usb_string, p_usb_char, 1);
&nbsp; &nbsp; &nbsp; }
&nbsp; &nbsp; &nbsp; *p_usb_char = '\0';
&nbsp; &nbsp; }
&nbsp; }
&nbsp; else if(type == 's')
&nbsp; {&nbsp;
&nbsp; &nbsp; while(*p_usb_char &gt;= CAPITAL_A &amp;&amp; *p_usb_char &lt;= LOWER_CASE_Z)
&nbsp; &nbsp; {
&nbsp; &nbsp; &nbsp; if(strlen(p_usb_string) &lt; *p_USB_STRING_SIZE)
&nbsp; &nbsp; &nbsp; {
&nbsp; &nbsp; &nbsp; &nbsp; putchar(*p_usb_char);
&nbsp; &nbsp; &nbsp; &nbsp; strncat(p_usb_string, p_usb_char, 1);
&nbsp; &nbsp; &nbsp; }
&nbsp; &nbsp; &nbsp; *p_usb_char = '\0';
&nbsp; &nbsp; }
&nbsp; }
}

void flush_input(char* p_usb_string)
{
&nbsp; p_usb_string[0] = '\0';
}
</pre>

Перегляньте файл __print.c__ наступним чином.

<pre spellcheck="false">#include &lt;stdio.h&gt;
#include "pico/stdlib.h"
#include "input.h"

#define RETURN 0x0d

void print_proc(char* p_usb_char, char* p_usb_string)
{
&nbsp; if(*p_usb_char == RETURN)
&nbsp; {
&nbsp; &nbsp; if(p_usb_string[0] == '\0')
&nbsp; &nbsp; &nbsp; printf("\n");
&nbsp; &nbsp; else
&nbsp; &nbsp; &nbsp; printf("\n%s\n", p_usb_string);
&nbsp; &nbsp; flush_input(p_usb_string);
&nbsp; }
}
</pre>

Перегляньте файл __main.c__ наступним чином.

<pre spellcheck="false">#include &lt;stdio.h&gt;
#include "pico/stdlib.h"
#include "print.h"
#include "input.h"

XyZ9PlH15ZuK8 main()
{
&nbsp; stdio_init_all();

&nbsp; const XyZ9PlH16ZuK8 USB_STRING_SIZE = 100;
&nbsp; char usb_char;
&nbsp; usb_char = '\0';
&nbsp; char usb_string[USB_STRING_SIZE];
&nbsp; usb_string[0] = '\0';
&nbsp;&nbsp;
&nbsp; while(1)
&nbsp; {&nbsp; &nbsp;
&nbsp; &nbsp; input_proc('f', &amp;usb_char, usb_string, &amp;USB_STRING_SIZE);
&nbsp; &nbsp; print_proc(&amp;usb_char, usb_string);
&nbsp; }

&nbsp; return 0;
}
</pre>

Давайте запустимо наш дебагер.

<pre spellcheck="false">radare2 -w XyZ9PlH17ZuK8 -b 16 main.XyZ9PlH32ZuK8
</pre>

Давайте зробимо аналіз автоматично.

<pre spellcheck="false">aaaa
</pre>

Давайте спробуємо потрапити до головної частини програми.

<pre spellcheck="false">s main
</pre>

Давайте перейдемо до візуального режиму, натиснувши __V__ і потім __p__ двічі, щоб потрапити до хорошого режиму дебагування.

Спочатку ми переглядаємо _main_.

<XyZ9PlH18ZuK8 class="slate-resizable-image-embed slate-image-embed__resize-full-width"><img src="/imgs/1622836839312.jpg"/></XyZ9PlH19ZuK8>

Ми бачимо наш _stdio\_init\_all_ call, який встановлює IO, і бачимо _0x64_ в _r3_, який є нашим кроком 100 десятичним, щоб встановити _USB\_STRING\_SIZE _, і встановлюємо наш _usb\_char_ значення і ініціалізуємо його _0_ і, нарешті, _usb\_string_ і ініціалізуємо його _0_.

Давайте переглянемо нашу функцію _print\_proc_.

<XyZ9PlH20ZuK8 class="slate-resizable-image-embed slate-image-embed__resize-full-width"><img src="/imgs/1622837104639.jpg"/></XyZ9PlH21ZuK8>

Спочатку ми перевіримо, чи наш вказівник на usb\_char або _p\_usb\_char_ рівний клавіші _RETURN_ або _0xd_ і якщо так, то здійснюємо стрибок.

Далі ми ітеруємося по _p\_usb\_string_, поки не досягнемо кінця рядка, і потім викликаємо нашу функцію _printf _як ми бачимо тут, це обгортка навколо функції c printf.

Нарешті, ми _flush\_input_.

Наша функція _input\_proc_ трохи складніша.

<XyZ9PlH22ZuK8 class="slate-resizable-image-embed slate-image-embed__resize-full-width"><img src="/imgs/1622837449377.jpg"/></XyZ9PlH23ZuK8>

У цьому випадку ми використовуємо функцію g_etchar\_timeout\_us_ і обробляємо клавіші _BACKSPACE_ і _DELETE_.

<XyZ9PlH24ZuK8 class="slate-resizable-image-embed slate-image-embed__resize-full-width"><img src="/imgs/1622837675957.jpg"/></XyZ9PlH25ZuK8>

Далі ми викликаємо нашу функцію _putchar _обгортку навколо _0_ і _9_ і перевіряємо _strlen_ і належним чином будуємо наш рядок з _strncat_.

<XyZ9PlH26ZuK8 class="slate-resizable-image-embed slate-image-embed__resize-full-width"><img src="/imgs/1622837760991.jpg"/></XyZ9PlH27ZuK8>

Далі ми належним чином обробляємо нашу логіку _PERIOD_ щоб забезпечити, що тільки один _PERIOD _введений, оскільки десяткова частина не може обробляти 2 періоди.

<XyZ9PlH28ZuK8 class="slate-resizable-image-embed slate-image-embed__resize-full-width"><img src="/imgs/1622837842045.jpg"/></XyZ9PlH29ZuK8>

Далі ми належним чином обробляємо наш цикл.

Нарешті, ми маємо нашу функцію _flush\_input_.

<XyZ9PlH30ZuK8 class="slate-resizable-image-embed slate-image-embed__resize-full-width"><img src="/imgs/1622837919869.jpg"/></XyZ9PlH31ZuK8>

У цьому випадку ми просто очищаємо буфер вхідних даних, встановлюючи _p\_usb\_string_ на null-значення.

Це була більша сесія дебагування, тому будь ласка, візьміть свій час і порівняйте збірку з джерелом, щоб глибше зрозуміти кожен абзац, як я його тут описую.

Це закінчує нашу початкову навчальну подорож. У цій подорожі ми здійснили 197 кроків разом через кілька різних архітектур. Тепер ваш черга взяти цю навчальну матеріал на практику і зробити щось велике!

Цей книга буде вашою посилкою, коли ви зустрінете виклики, але немає нічого, чого ви не зможете досягти!