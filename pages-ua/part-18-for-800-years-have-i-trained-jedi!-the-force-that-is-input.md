Частина 18 - "Я ВИДУЧУ СЕДЬМИ РОКИ ДЖЕДАЇ!", СИЛА, ЯКА ВВІДУЄ...

"Рік 2021 і сім місяців, середня ціна галона бензину в Сполучених Штатах становить 7,51 долар за галон. Чотири інші трубопроводи США були компрометовані з використанням шантажної програми і п'ять очей відкрили компрометований мережу всередині однієї з водних джерел в одному з великих міст Сполучених Штатів."

"Джерела інформації розташували штаб-квартиру організації 'Темні очі' за підтримкою атак з використанням вірусу і використовують мікроконтролер Pico як керуючий механізм всередині дрон, який готується завдати удару цій установі і вивести їх зв'язок, щоб уникнути нападу на нашу водну систему."

"Координати нападу - '61.013693050912785, 99.19670587477269', яким Дрон-оператор вводить '61.013693050912785, 9e.19670587477269', яке є 'Мірські шахти, Росія'. Вони запускають дрон і він вибухає в '61.013693050912785, 9.19670587477269', яке є 'Муніципалітет Норд-Аурдал, Норвегія'."

"Паніка виникла, але Департамент внутрішньої безпеки зміг забезпечити мережу водної системи до того, як шантажна програма змогла зашифрувати їх мережу, і протягом дванадцяти годин мережа була повністю забезпечена."

Хочу взяти час, щоб показати абсолютну КРИТИЧНІСТЬ розробки програмного забезпечення з належним обробленням вхідних даних. Використання 'scanf' або інших технік, які не належним чином обробляють кожне натиснення клавіш, може привести до ситуації, подібної тієї, яку описано вище.

Давайте переглянемо нашу функцію вхідних даних...

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

void input_proc(char type, char* p_usb_char, char* p_usb_string, const XyZ9PlH16ZuK8* p_USB_STRING_SIZE)
{
  *p_usb_char = '\0';
  *p_usb_char = getchar_timeout_us(0);
  if(*p_usb_char == BACKSPACE || *p_usb_char == DEL)
  {
    if(p_usb_string[0] != '\0')
    {
      printf("\b");
      XyZ9PlH10ZuK8(" ");
      XyZ9PlH11ZuK8("\b");
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

Сьогодні ми навчимося точно вивчати цю функцію.

<pre spellcheck="false">void input_proc(char type, char* p_usb_char, char* p_usb_string, const XyZ9PlH17ZuK8* p_USB_STRING_SIZE)
</pre>

Ми починаємо з заголовка функції. Перше, ми приймаємо _char_ _типу_, де в нашому прикладі ми використовуємо _'f'_ для обробки чисел з плаваючою точкою. Потім ми маємо _char\*_ (покажчик)_ _p\_usb\_char_, який буде ініціалізований _'\\0'_ в __main.c__. Потім ми маємо _char\* p\_usb\_string, який буде ініціалізований _'\\0'_ в __main.c__. Потім ми маємо _const int\*_ _p\_USB\_STRING\_SIZE_, який буде ініціалізований _100_ в __main.c__.

Ми створюємо логіку для належного оброблення кнопки видалення або кнопки назад.

<pre spellcheck="false">  if(*p_usb_char == BACKSPACE || *p_usb_char == DEL)
  {
    if(p_usb_string[0] != '\0')
    {
      XyZ9PlH12ZuK8("\b");
      XyZ9PlH13ZuK8(" ");
      XyZ9PlH14ZuK8("\b");
      p_usb_string[strlen(p_usb_string)-1] = '\0';
    }
  }
</pre>

Ми створюємо логіку для оброблення, якщо програма main.c очікує тільки чисел з плаваючою точкою, як у нашій історії вище, якщо б було виконано, дрон не зміг би потрапити у свій мітку.

<pre spellcheck="false">  if(type == 'f')
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
</pre>

Ми бачимо, що якщо хто-небудь вводить щось інше, ніж _НУЛЬ_ до _ДЕВ'ЯТИ_ або _ПЕРЕДНІЙ КРІВКА,_ вхід буде просто відкинуто!

Також ми бачимо, що якщо була введена _ПЕРЕДНІЙ КРІВКА,_ друга не могла бути введена ні з метою шахрайства, ні випадково. Ми також обробляємо кількість вхідних даних менше _100_ належним чином. Потім ми належним чином будуємо нашу строку з кожного належним чином очищеного натиснення клавіш.

Аналогічна логіка обробляє випадки з дробами або іншими випадками.

<pre spellcheck="false">  else if(type == 'd')
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
</pre>

У наступному урокі ми імплементуватимемо цю функцію в нашому мікроконтролері Pico.