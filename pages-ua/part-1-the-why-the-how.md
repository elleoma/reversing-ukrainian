## Частина 1 - Чому, Як...

2021 рік і знову ми починаємо новий курс зворотнього інжинірингу. Цей курс буде присвячений програмуванню мовою C, яку ми статично зворотньо розшифруємо скомпільований ARM 32 elf бінарний файл за допомогою Radare2 дебагера на мікроконтролері Raspberry Pi Pico.

Що таке мікроконтролери? Їх можна знайти в транспортних засобах, роботах, офісних машинах, медичних приладах, мобільних радіотрансиверах, автоматидах і домашніх приладах тощо. Вони призначені для управління малими функціями більшого компонента, без складної передньої частини операційної системи.

Ми будемо писати дуже прості програми мовою C і потім зворотньо розшифрувати їх один за одним мовою ARM 32 збірки.

Я припущу, що ви працюєте з дистрибутивом Ubuntu Linux...

Вам спочатку потрібно мати Raspberry Pi Pico.

Вам потрібно мати репозиторій Radare2.

<pre spellcheck="false">git clone https://github.com/radareorg/radare2.git
cd radare2
cd radare2&nbsp;sys/install.sh
</pre>

Ви ЗАВЖДИ повинні будувати з джерела! Версії, що пакуються в Ubuntu і Kali Linux, старіші і не мають необхідних функцій для нашого рівня зворотнього інжинірингу.

Вам потрібно мати VIM.

<pre spellcheck="false">sudo apt install vim
</pre>

Вам потрібно оновити файл.vimrc file.

<pre spellcheck="false">vim ~/.vimrc
</pre>

А потім...

<pre spellcheck="false">set number
set tabstop=2 &nbsp; &nbsp;
set shiftwidth=2
set expandtab&nbsp;
syntax on
set syntax=c&nbsp;
</pre>

Вам потрібно мати репозиторій Raspberry Pi Pico.

<pre spellcheck="false">mkdir pico
cd pico
git clone -b master https://github.com/raspberrypi/pico-sdk.git
cd pico-sdk
git submodule update --init
cd..
git clone -b master https://github.com/raspberrypi/pico-examples.git
sudo apt update
sudo apt install cmake gcc-arm-none-eabi libnewlib-arm-none-eabi build-essential&nbsp;
</pre>

Давайте побудуємо програму "блискавка".

<pre spellcheck="false">cd pico-examples
mkdir build
cd build
export PICO_SDK_PATH=../../pico-sdk
cmake..
cd blink
make
</pre>

Копіюйте файл __blink.uf2 __в свій Pico.

Вітаємо, ви got написали блискучу програму мовою C!

У наступному урокі ми створимо просту програму "Привіт, Світ!".