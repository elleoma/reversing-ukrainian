---
{}
---

__Placeholder_2__ Частина 17 - "Абсолютна сила пошкоджує абсолютно!", Трагічна казка про введення ...

"Але я просто тут, щоб вивчити зворотну інженерію, я дійсно __placeholder_31__ зацікавлений у несексичній частині кодування, я просто хочу, щоб зворотна інженерна виклик __placeholder_22__ бути суперзіркою!"

Ах, наївність не-джідів. Для багато чого вони повинні навчитися __placeholder_16__, можливо, навчанню, щоб дійсно вчитися!

Я беру __placeholder_32__ постріл у книгах програмування __placeholder_23__ курси, які вчать, як захоплювати stdin у користувачів спрощено, як '__placeholder_17__', однак я скоріше закликаю вас вважати належним підходом.

Ми маємо справу з мікроконтролером. Це ціль авторів викупу, державних агентів __placeholder_24__ всілякі недоброзичливі сторони. Спочатку ми повинні зайняти час, щоб зрозуміти, як правильно обробляти вхід щодо мікроконтролера.

Я взяв свободу, щоб побудувати належну функцію введення для вашого експертизи.

__Placeholder_0 __#включити & lt; stdio__placeholder_19 __ & gt;
__Placeholder_3__ включає & lt; string__placeholder_20 __ & gt;
__Placeholder_4__ включити "pico/stdlib__placeholder_21__"

__Placeholder_5__ Визначте нуль 0x30
__Placeholder_6__ Визначте дев'ять 0x39
__Placeholder_7__ Визначте період 0x2e
__Placeholder_8__ Визначте Capital_A 0x41
__Placeholder_9__ Визначте нижній_case_z 0x7a
__Placeholder_10__ Визначте Backspace 0x08
__Placeholder_11__ Визначте del 0x7f

void input_proc (тип char, char* p_usb_char, char* p_usb_string, const __placeholder_18 __* p_usb_string_size)
{
  *p_usb_char = '\ 0';
  *p_usb_char = getchar_timeout_us (0);
  if ( *p_usb_char == backspace || *p_usb_char == del)
  {
    if (p_usb_string [0]! = '\ 0')
    {
      __Placeholder_28 __ ("\ b");
      __Placeholder_29 __ ("");
      __Placeholder_30 __ ("\ b");
      P_USB_STRING [__ Ploadholder_12 __ (P_USB_STRING) -1] = '\ 0';
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
        if (__ Ploadholder_13 __ (P_USB_STRING) & lt; *P_USB_STRING_SIZE)
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
      if (__ placholder_14 __ (p_usb_string) & lt; *p_usb_string_size)
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
      if (__ Ploadholder_15 __ (P_USB_STRING) & lt; *P_USB_STRING_SIZE)
      {
        putchar (*p_usb_char);
        strncat (P_USB_STRING, P_USB_CHAR, 1);
      }
      *p_usb_char = '\ 0';
    }
  }
}
__Placeholder_1__

"Вау, я думав, що ми сприймаємо це повільно!" Настав час належним чином почати розуміти, як бути джедатом при розробці ефективного програмного забезпечення. Настав час, щоб зайняти час, щоб правильно перетравити реальну функцію перевірки введення.

Я хочу, щоб ви витратили час __placeholder_25__ перетравлюють цю функцію, щоб ми могли переглянути її на наступному уроці.

На нашому наступному уроці ми належним чином розбиваємо цю роботу з генієм, щоб правильно зрозуміти __placeholder_26__ craft __placeholder_27__ в кінцевому підсумку реверс -інженер у нашому майбутньому майбутньому!