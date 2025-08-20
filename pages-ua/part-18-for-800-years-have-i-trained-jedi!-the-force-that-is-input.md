## part 18 - "Протягом 800 років я тренував джедаї!", Сила, яка вводить ... "Рік - 2021 and СЕМІНЯХ МІСЯЦІВ, Середня ціна галона газу в межах Сполучених Штатів становить 7,51 дол. Вода поставляється у великому столичному місті США ".

"Джерела розвідки розташували штаб -квартиру" Темні очі ", що стоять за нападами зловмисного програмного забезпечення and, використовують мікроконтролер Pico як контролер всередині безпілотника, який готується, щоб вдарити цей об'єкт and, вибиває їхні комунікації, щоб уникнути нападу на постачання води".

"Координати нападу - '61 .013693050912785, 99.19670587477269 ', до якого входить оператор безпілотника, '61 .013693050912785, 9e.19670587477269' детонації в, 61.

"Паніка виникає, однак, DHS зміг закріпити мережу водопостачання, перш ніж Ransomware змогла шифрувати свою мережу and протягом дванадцяти годин, мережа була повністю захищена."

Гаразд ... Я хотів витратити час, щоб по -справжньому показати абсолютну критичність проектування програмного забезпечення з належною обробкою введення. Використання 'scanf' or інших методик, які виконують not, належним чином обробляються кожною клавішею, може призвести до такої ситуації, як описана вище. Давайте розглянемо нашу функцію введення ... <pre spellcheck="false">#include &lt;stdio.h&gt;
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

Сьогодні ми будемо переглянути саме те, що насправді робить ця функція. <pre spellcheck="false">void input_proc(char type, char* p_usb_char, char* p_usb_string, const int* p_USB_STRING_SIZE)
</pre>

Починаємо з заголовка функції. Спочатку ми приймаємо _Char_ _type_, де в нашому прикладі ми будемо використовувати _'f'_ для обробки номерів з плаваючою комою. Потім у нас є _char \*_ (вказівник) _p \ _USB \ _Char_, який буде init to _ '\\ 0'_ в __main.c__. Потім у нас є char \* p \ _usb \ _string, який ми будемо init to _ '\\ 0'_ in __main.c__. Потім у нас є _const int \*_ _p \ _usb \ _string \ _size_, який буде init to _100_ в __main.c__. Потім ми створюємо логіку, щоб правильно обробляти кнопку Backspace or. <pre spellcheck="false">  if(*p_usb_char == BACKSPACE || *p_usb_char == DEL)
  {
    if(p_usb_string[0] != '\0')
    {
      printf("\b");
      printf(" ");
      printf("\b");
      p_usb_string[strlen(p_usb_string)-1] = '\0';
    }
  }
</pre>

Потім ми створюємо логіку для обробки, якщо програма main.C очікує лише номерів з плаваючою комою, як у нашій історії вище, якби було реалізовано, безпілотник би not пропустив свою ціль. <pre spellcheck="false">  if(type == 'f')
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

Ми бачимо, що якщо хтось вводить щось інше, ніж _zero_ через _nine_ or a _period, _ вхід просто буде відхилено! Ви також бачите, що якщо введено _period_, який може бути введений not або зловмисно or випадково. Ми також обробляємо кількість введення менше, ніж _100_ належним чином. Потім ми правильно будуємо свою струну з кожного належним чином очищеного клавіші. Подібні логічні ручки, якщо ви маєте справу з десятками or strings. <pre spellcheck="false">  else if(type == 'd')
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

На нашому наступному уроці ми реалізуємо це в нашому мікроконтролері PICO.