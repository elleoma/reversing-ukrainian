---
{}
---

__Placeholder_10__ Частина 18 - "Протягом 800 років я навчав джедаїв!" З поставки води у великому столичному місті U__PLAYSHOLDER_34__. "

"Джерела розвідки розташували штаб -квартиру" Темні очі ", що стоять за нападами зловмисного програмного забезпечення __placeholder_45__, використовуйте мікроконтролер PICO як контролер всередині безпілотника, який готується, щоб вдарити цей об'єкт __placeholder_46__, щоб уникнути нападу на нашу водопостачання".

"Координати нападу - '61 .013693050912785, 99.19670587477269 ', до якого входить оператор безпілотника, '61 .013693050912785, 9e.19670587477269' детонації в, 61.

"Паніка виникає, однак, DHS змогла забезпечити мережу водопостачання, перш ніж програма-вимагач змогла шифрувати свою мережу __placeholder_48__ протягом дванадцяти годин мережа була повністю захищена."

Гаразд ... Я хотів витратити час, щоб по -справжньому показати абсолютну критичність проектування програмного забезпечення з належною обробкою введення. Використання '__placeholder_35__' __placeholder_28__ Інші методи, які виконують __placeholder_56__ належним чином обробляють кожен клавішу, може призвести до такої ситуації, як описана вище. Давайте розглянемо нашу функцію введення ... __placeholder_0 __#включає & lt; stdio__placeholder_40 __ & gt;
__Placeholder_11__ включає & lt; string__placeholder_41 __ & gt;
__Placeholder_12__ включити "pico/stdlib__placeholder_42__"

__Placeholder_13__ Визначте нуль 0x30
__Placeholder_14__ Визначте дев'ять 0x39
__Placeholder_15__ Визначте період 0x2e
__Placeholder_16__ Визначте Capital_A 0x41
__Placeholder_17__ Визначте нижній_case_z 0x7a
__Placeholder_18__ Визначте BackSpace 0x08
__Placeholder_19__ Визначте del 0x7f

void input_proc (тип char, char* p_usb_char, char* p_usb_string, const __placeholder_37 __* p_usb_string_size)
{
  *p_usb_char = '\ 0';
  *p_usb_char = getchar_timeout_us (0);
  if ( *p_usb_char == backspace || *p_usb_char == del)
  {
    if (p_usb_string [0]! = '\ 0')
    {
      __Placeholder_49 __ ("\ b");
      __Placeholder_50 __ ("");
      __Placeholder_51 __ ("\ b");
      P_USB_STRING [__ Ploadholder_20 __ (P_USB_STRING) -1] = '\ 0';
    }
  }
  if (type == 'f')
  { 
    Чар* період;
    while (( *p_usb_char & gt; = Zero & amp; & amp; *p_usb_char & lt; = дев'ять) || *p_usb_char == період)
    {
      if (*p_usb_char == період)
        період = strchr (p_usb_string, '.');
      якщо (період == null) 
      {
        if (__ Ploadholder_21 __ (P_USB_STRING) & lt; *P_USB_STRING_SIZE)
        {
          putchar (*p_usb_char);
          strncat (P_USB_STRING, P_USB_CHAR, 1);
        }
        *p_usb_char = '\ 0';
      }
      інакше
        перерва;
    }
  }
  інакше, якщо (тип == 'd')
  { 
    while ( *p_usb_char & gt; = Zero & amp; & amp; *p_usb_char & lt; = дев'ять)
    {
      if (__ Ploadholder_22 __ (P_USB_STRING) & lt; *P_USB_STRING_SIZE)
      {
        putchar (*p_usb_char);
        strncat (P_USB_STRING, P_USB_CHAR, 1);
      }
      *p_usb_char = '\ 0';
    }
  }
  інакше, якщо (тип == 's')
  { 
    while ( *p_usb_char & gt; = capital_a & amp; & amp; *p_usb_char & lt; = lite_case_z)
    {
      if (__ Ploadholder_23 __ (P_USB_STRING) & lt; *P_USB_STRING_SIZE)
      {
        putchar (*p_usb_char);
        strncat (P_USB_STRING, P_USB_CHAR, 1);
      }
      *p_usb_char = '\ 0';
    }
  }
}
__Placeholder_1__

Сьогодні ми будемо переглянути саме те, що насправді робить ця функція. __Placeholder_2__void input_proc (тип char, char* p_usb_char, char* p_usb_string, const __placeholder_38 __* p_usb_string_size)
__Placeholder_3__

Починаємо з заголовка функції. Спочатку ми приймаємо _Char_ _type_, де в нашому прикладі ми будемо використовувати _'f'_ для обробки номерів з плаваючою комою. Потім у нас є _char \*_ (вказівник) _p \ _USB \ _Char_, який буде init to _ '\\ 0'_ в __main.c__. Потім у нас є char \* p \ _usb \ _string, який ми будемо init to _ '\\ 0'_ in __main.c__. Тоді у нас є _const __placeholder_39 __ \*_ _p \ _USB \ _String \ _Size_, який буде init to _100_ в __main.c__. Потім ми створюємо логіку, щоб правильно обробляти видалення __placeholder_29__ Backspace. __Placeholder_4__ if ( *p_usb_char == backspace || *p_usb_char == del)
  {
    if (p_usb_string [0]! = '\ 0')
    {
      __Placeholder_52 __ ("\ b");
      __Placeholder_53 __ ("");
      __Placeholder_54 __ ("\ b");
      P_USB_STRING [__ Ploadholder_24 __ (P_USB_STRING) -1] = '\ 0';
    }
  }
__Placeholder_5__

Потім ми створюємо логіку для обробки, якщо програма Main__Placeholder_55__ очікує лише номерів з плаваючою комою, як у нашій історії вище, якби це було реалізовано, безпілотник би __placeholder_57__ пропустив свою ціль. __Placeholder_6__ if (type == 'f')
  { 
    Чар* період;
    while (( *p_usb_char & gt; = Zero & amp; & amp; *p_usb_char & lt; = дев'ять) || *p_usb_char == період)
    {
      if (*p_usb_char == період)
        період = strchr (p_usb_string, '.');
      якщо (період == null) 
      {
        if (__ Ploadholder_25 __ (P_USB_STRING) & lt; *P_USB_STRING_SIZE)
        {
          putchar (*p_usb_char);
          strncat (P_USB_STRING, P_USB_CHAR, 1);
        }
        *p_usb_char = '\ 0';
      }
      інакше
        перерва;
    }
  }
__Placeholder_7__

Ми бачимо, що якщо хтось вводить щось інше, ніж _zero_ через _nine_ __placeholder_30__ a _period, _ вхід буде просто відхилений! Ви також бачите, що якщо є _period_ введений другий, може бути введений __placeholder_58__ або зловмисно __placeholder_31__ випадково. Ми також обробляємо кількість введення менше, ніж _100_ належним чином. Потім ми правильно будуємо свою струну з кожного належним чином очищеного клавіші. Подібні логічні ручки, якщо ви маєте справу з десятками __placeholder_32__ __placeholder_36__. __Placeholder_8__ else if (type == 'd')
  { 
    while ( *p_usb_char & gt; = Zero & amp; & amp; *p_usb_char & lt; = дев'ять)
    {
      if (__ Ploadholder_26 __ (P_USB_STRING) & lt; *P_USB_STRING_SIZE)
      {
        putchar (*p_usb_char);
        strncat (P_USB_STRING, P_USB_CHAR, 1);
      }
      *p_usb_char = '\ 0';
    }
  }
  інакше, якщо (тип == 's')
  { 
    while ( *p_usb_char & gt; = capital_a & amp; & amp; *p_usb_char & lt; = lite_case_z)
    {
      if (__ Ploadholder_27 __ (P_USB_STRING) & lt; *P_USB_STRING_SIZE)
      {
        putchar (*p_usb_char);
        strncat (P_USB_STRING, P_USB_CHAR, 1);
      }
      *p_usb_char = '\ 0';
    }
  }
__Placeholder_9__

На нашому наступному уроці ми реалізуємо це в нашому мікроконтролері PICO.