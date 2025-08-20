## part 1 - чому, як ...

Це 2021 and Тут ми знову висвітлюємо новий курс інженера -зворотного інженера. Цей курс буде зосереджено на мові програмування C, до якої ми будемо статично змінювати складений бінар ARM 32 elf, використовуючи microcontroller налагоджувач Radare2 налагоджувач.

Що таке мікроконтролери? Ми можемо знайти їх у транспортних засобах, роботах, офісних машинах, медичних пристроях, мобільних радіоприймачах, торгових автоматах and Домашня техніка, серед інших пристроїв. Вони є цілеспрямованими машинами, розробленими для управління невеликими ознаками більшого компонента, без складної передової операційної системи.

Ми будемо писати дуже основні програми C and, а потім змінити їх по одному в ARM 32 Асамблеї.

Я припускаю, що ви працюєте з дистрибуцією Ubuntu Linux ...

Спочатку вам знадобиться Raspberry Pi Pico.

Вам знадобиться Radare2 repo.

<pre spellcheck="false">git clone https://github.com/radareorg/radare2.git
cd radare2
cd radare2&nbsp;sys/install.sh
</pre>

Вам потрібно побудувати з джерела! Версії, які упаковуються в Ubuntu and KALI LINUX, є старішими and DO not, мають необхідні для нашого рівня реверсування.

Вам знадобиться Вім.

<pre spellcheck="false">sudo apt install vim
</pre>

Вам потрібно буде оновити .VIMRC file.

<pre spellcheck="false">vim ~/.vimrc
</pre>

Тоді ...

<pre spellcheck="false">встановити number
встановити tabstop=2 &nbsp; &nbsp;
встановити shiftwidth=2
встановити expandtab&nbsp;
syntax on
встановити syntax=c&nbsp;
</pre>

Вам знадобиться Raspberry Pi Pico Repo.

<pre spellcheck="false">mkdir pico
cd pico
git clone -b master https://github.com/raspberrypi/pico-sdk.git
cd pico-sdk
git submodule update --init
cd ..
git clone -b master https://github.com/raspberrypi/pico-examples.git
sudo apt update
sudo apt install cmake gcc-arm-none-eabi libnewlib-arm-none-eabi build-essential&nbsp;
</pre>

Давайте побудуємо програму Blink.

<pre spellcheck="false">cd pico-examples
mkdir build
cd build
export PICO_SDK_PATH=../../pico-sdk
cmake ..
cd blink
make
</pre>

Скопіюйте __blink.uf2 __file у свій піко.

Вітаю вас got, миготлива програма C!

На нашому наступному уроці ми створимо просту програму "Привіт, Світ".