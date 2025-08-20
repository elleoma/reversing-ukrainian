## PART 17 - "Абсолютна потужність корумує абсолютно!", Трагічна казка про введення ...

"Але я просто тут, щоб вивчити зворотну інженерію, я справді not, зацікавлений у несексичній частині кодування, я просто хочу, щоб зворотна інженерна виклик and бути суперзіркою!"

Ах, наївність не-джідів. Для багато чого вони повинні вивчити or, можливо, навчаючись дійсно вчитися!

Я беру not постріл у програмах програмування and курсів, які вчать, як захоплювати stdin у користувачів спрощено, як 'scanf', проте я скоріше кидаю виклик вам розглянути належний підхід.

Ми маємо справу з мікроконтролером. Це ціль авторів викупів, державних агентів and ВСІХ СТАРІВ. Спочатку ми повинні зайняти час, щоб зрозуміти, як правильно обробляти вхід щодо мікроконтролера.

Я взяв свободу, щоб побудувати належну функцію введення для вашого експертизи.

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
    if(p_usb_string[0] != '\0')
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

"Вау, я думав, що ми сприймаємо це повільно!" Настав час належним чином почати розуміти, як бути джедатом при розробці ефективного програмного забезпечення. Настав час, щоб зайняти час, щоб правильно перетравити реальну функцію перевірки введення.

Я хочу, щоб ви взяли час and, щоб дізнатись цю функцію, щоб ми могли переглянути її на наступному уроці.

На нашому наступному уроці ми належним чином розбиваємо цю роботу з генієм, щоб правильно зрозуміти and CRAFT and в кінцевому підсумку реверс -інженера в нашому майбутньому!