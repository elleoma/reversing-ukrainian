## Частина 17 - "ПОВНОВЛАСТНІСТЬ ЗНИЩУЄ ПОВНІСТЬ!", Трагічна історія Введення...

"Але я тільки тут, щоб вивчити Обратну Інженерію. Я справді не цікавлюся не-сексуальною частиною програмування, я тільки хочу викликати Обратну Інженерію і стати суперзіркою!"

Ах, наївність тих, хто не є Джедаєм. Для них багато чого потрібно вивчити або, може бути, вивчити знову, щоб дійсно вивчити!

Я не роблю жодної спроби підмінити програмні книги і курси, які вчать, як захоплювати STDIN від користувачів у простому вигляді, наприклад, 'scanf', але я натомість викликаю вас, щоб розглянути належний підхід.

Ми маємо справу з мікроконтролером. Він є ВИБРАНОЮ мішенню авторів Рansomware, державних агентів і всіх інших неприємних осіб. НАМУ СПОРОМНО потрібно спочатку зрозуміти, як належним чином обробляти вхідні дані щодо мікроконтролера.

Я взяв на себе свободу побудувати належну функцію введення для вашої оцінки.

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
  *p_usb_char = '\0';
  *p_usb_char = getchar_timeout_us(0);
  if(*p_usb_char == BACKSPACE || *p_usb_char == DEL)
  {
    if(p_usb_string[0]!= '\0')
    {
      printf("\b");
      printf(" ");
      printf("\b");
      p_usb_string[strlen(p_usb_string)-1] = '\0';
    }
  }
  if(type == 'f')
  { 
    char* period;
    while((*p_usb_char &gt;= ZERO &amp;&amp; *p_usb_char &lt;= NINE) || *p_usb_char == PERIOD)
    {
      if(*p_usb_char == PERIOD)
        period = strchr(p_usb_string, '.');
      if(period == NULL) 
      {
        if(strlen(p_usb_string) &lt; *p_USB_STRING_SIZE)
        {
          putchar(*p_usb_char);
          strncat(p_usb_string, p_usb_char, 1);
        }
        *p_usb_char = '\0';
      }
      else
        break;
    }
  }
  else if(type == 'd')
  { 
    while(*p_usb_char &gt;= ZERO &amp;&amp; *p_usb_char &lt;= NINE)
    {
      if(strlen(p_usb_string) &lt; *p_USB_STRING_SIZE)
      {
        putchar(*p_usb_char);
        strncat(p_usb_string, p_usb_char, 1);
      }
      *p_usb_char = '\0';
    }
  }
  else if(type == 's')
  { 
    while(*p_usb_char &gt;= CAPITAL_A &amp;&amp; *p_usb_char &lt;= LOWER_CASE_Z)
    {
      if(strlen(p_usb_string) &lt; *p_USB_STRING_SIZE)
      {
        putchar(*p_usb_char);
        strncat(p_usb_string, p_usb_char, 1);
      }
      *p_usb_char = '\0';
    }
  }
}
</pre>

"Ох, я подумав, що ми йшли повільно!" Тепер настало час належним чином розпочати розуміти, як бути Джедаєм при розробці ефективного програмного забезпечення. Тепер настало час належним чином засвоювати справжню функцію перевірки входу.

Я хочу, щоб ви взяли час і засвоїли цю функцію, щоб ми могли її переглянути в наступному урокі.

У наступному урокі ми належним чином розберемо цю роботу генієві, щоб належним чином зрозуміти і створити, і, в кінцевому підсумку, здійснити Обратну Інженерію у нашій майбутній майбутності!