## part 20 - налагодження введення

Сьогодні ми будемо налагодити нашу функцію введення. Давайте розглянемо наш код.

Review&nbsp;__input.c__&nbsp;as наступає.

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

void input_proc(char type, char* p_usb_char, char* p_usb_string, const int* p_USB_STRING_SIZE)
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

Перегляньте ur&nbsp;__print.c__&nbsp;as.

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

Перегляньте ur&nbsp;__main.c__&nbsp;as.

<pre spellcheck="false">#include &lt;stdio.h&gt;
#include "pico/stdlib.h"
#include "print.h"
#include "input.h"

int main()
{
&nbsp; stdio_init_all();

&nbsp; const int USB_STRING_SIZE = 100;
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

Давайте розберемося в нашому налагоджувач.

<pre spellcheck="false">radare2 -w arm -b 16 main.elf
</pre>

Давайте автоматично проаналізуємо.

<pre spellcheck="false">aaaa
</pre>

Давайте прагнемо main.

<pre spellcheck="false">s main
</pre>

Перейдемо у візуальний режим, typing&nbsp;__v__&nbsp;and then&nbsp;__p__&nbsp;twice, щоб дістатися до хорошого налагоджувач.

Спочатку ми оглядаємо _main_.

<div class="slate-resizable-image-embed slate-image-embed__resize-full-width"><img src="/imgs/1622836839312.jpg"/></div>

Ми бачимо наш _stdio \ _init \ _all_ call, який налаштовує io and, ми бачимо a _0x64_ в _r3_, що є нашим кроком 100 десятків, щоб встановити _usb \ _string \ _ -_siz and init to _0_ and нарешті _usb \ _string_ and init to _0_.

Давайте подивимось на нашу функцію _print \ _proc_.

<div class="slate-resizable-image-embed slate-image-embed__resize-full-width"><img src="/imgs/1622837104639.jpg"/></div>

Спочатку перевіряємо, чи наш вказівник на USB \ _Char or _P \ _USB \ _Char_ дорівнює _Return_ Key or _0XD_ and, якщо це гілка.

Потім ми повторюємо _p \ _USB \ _string_, поки не натиснемо Null Terminator and, тоді call Наш _Printf _Function, який, як ми бачимо тут, є обгорткою для функції C printf.

Нарешті _flush \ _input_.

Наша функція _input \ _proc_ трохи складніша.

<div class="slate-resizable-image-embed slate-image-embed__resize-full-width"><img src="/imgs/1622837449377.jpg"/></div>

Тут ми використовуємо G_ETCHAR \ _TimeOut \ _US_ Функція and Ручка _BackSpace_ and _delete_ клавіш.

<div class="slate-resizable-image-embed slate-image-embed__resize-full-width"><img src="/imgs/1622837675957.jpg"/></div>

Тоді ми call наш _putchar _wrapper проти_ 0_ and _9_ and перевіряйте _strlen_ and належним чином побудуємо нашу рядок з _strncat_.

nbsp

Потім ми правильно обробляємо нашу логіку _period_, щоб забезпечити лише один _period _IS, введений як номер плаваючої точки, може NOT ручки 2 періоди.

<div class="slate-resizable-image-embed slate-image-embed__resize-full-width"><img src="/imgs/1622837842045.jpg"/></div>

Потім ми правильно обробляємо свою петлю.

Нарешті, у нас є функція _flush \ _input_.

<div class="slate-resizable-image-embed slate-image-embed__resize-full-width"><img src="/imgs/1622837919869.jpg"/></div>

Тут ми просто промиваємо вхідний буфер, встановивши _p \ _USB \ _string_ на нульовий char.

Це була більша сесія налагодження, тому, будь ласка, знайдіть свій час and Порівняйте збірку з джерелом, щоб ви могли дійсно зрозуміти кожен абзац, коли я його тут висвітлюю.

Це підводить нас до кінця нашої початкової навчальної подорожі. У цій подорожі ми зробили 197 кроків разом через кілька різних архітектур. Настав ваша черга, щоб перенести цю підготовку на практиці and робити великі речі!

Ця книга буде вашим довідником, коли ви стикаєтесь з викликами, проте немає нічого, що ви не можете досягти!