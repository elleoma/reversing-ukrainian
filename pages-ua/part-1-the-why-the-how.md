---
{}
---

__Placeholder_15__ Частина 1 - чому, як ...

Це 2021 р. __Placeholder_27__ Тут ми знову висвітлюємо новий курс інженера -зворотного інженера. Цей курс буде зосереджено на мові програмування C, на яку ми будемо статично змінювати складений __placeholder_33__ 32 __placeholder_18__ Бінарне використання налагодження __placeholder_23__ на мікроконтролері Raspberry Pi Pico.

Що таке мікроконтролери? Ми можемо знайти їх у транспортних засобах, роботах, офісних машинах, медичних пристроях, мобільних радіоприймачах, торгових автоматах __placeholder_28__, серед інших пристроїв. Вони є цілеспрямованими машинами, розробленими для управління невеликими ознаками більшого компонента, без складної передової операційної системи.

Ми будемо писати дуже основні програми C __placeholder_29__, а потім повернути їх по черзі в __placeholder_34__ 32 Асамблеї.

Я припускаю, що ви працюєте з Ubuntu __placeholder_16__ Distro ...

Спочатку вам знадобиться Raspberry Pi Pico.

Вам знадобиться __placeholder_24__ repo.

__Placeholder_0__git клон __placeholder_12__
CD __placeholder_25__
cd __placeholder_26 __ & nbsp; __ ploadholder_19 __/встановити .__ ploadholder_21__
__Placeholder_1__

Вам потрібно побудувати з джерела! Версії, які упаковуються в Ubuntu __placeholder_30__ Kali __placeholder_17__ старші __placeholder_31__ do __placeholder_32__ мають необхідні функції для нашого рівня реверсування.

Вам знадобиться Вім.

__Placeholder_2__sudo apt Установіть vim
__Placeholder_3__

Вам потрібно буде оновити .vimrc __placeholder_22__.

__Placeholder_4__vim ~/.vimrc
__Placeholder_5__

Тоді ...

__Placeholder_6__set Номер
Встановити tabstop = 2 & nbsp; & nbsp;
Встановити ширину Shift = 2
Встановити розширення & nbsp;
синтаксис
встановити синтаксис = c & nbsp;
__Placeholder_7__

Вам знадобиться Raspberry Pi Pico Repo.

__Placeholder_8__mkdir pico
CD Pico
git clone -b master __placeholder_13__
CD PICO-SDK
Оновлення підмодуль Git - -init
CD ..
git clone -b master __placeholder_14__
Оновлення Sudo Apt
sudo apt встановити cmake gcc -__ ploadholder_35 __- none-eabi libnewlib -__ ploadholder_36 __- none-eabi build-ensential & nbsp;
__Placeholder_9__

Давайте побудуємо програму Blink.

__Placeholder_10__cd pico-examples
Mkdir Build
Комплект компакт -дисків
Експорт PICO_SDK_PATH = ../../PICO-SDK
cmake ..
CD моргнути
робити
__Placeholder_11__

Скопіюйте __blink.uf2 __file у свій піко.

Вітаємо вас __placeholder_20__ миготлива програма C!

На нашому наступному уроці ми створимо просту програму "Привіт, Світ".