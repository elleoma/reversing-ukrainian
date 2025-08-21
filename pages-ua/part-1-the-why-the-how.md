## part 1 - чому, як ...

Це 2021 рік, і тут ми знову висвітлюємо новий курс інженера -зворотного інженера. Цей курс буде зосереджено на мові програмування C, на яку ми будемо статично змінювати складений бінарний ARM 32 elf, використовуючи налагоджувач Radare2 на мікроконтролері Raspberry Pio Pico.

Що таке мікроконтролери? Серед інших пристроїв ми можемо знайти їх у транспортних засобах, роботах, офісних машинах, медичних пристроях, мобільних радіоприймачах, торгових автоматах та домашніх приладах. Вони є цілеспрямованими машинами, розробленими для управління невеликими ознаками більшого компонента, без складної передової операційної системи.

Ми будемо писати дуже основні програми C, а потім повернути їх по одному в складі ARM 32.

Я припускаю, що ви працюєте з дистрибуцією Ubuntu Linux ...

Спочатку вам знадобиться Raspberry Pi Pico.

Вам знадобиться Radare2 repo.

<pre spellcheck="false">git clone https://github.com/radareorg/radare2.git
cd radare2
cd radare2&nbsp;sys/install.sh
</pre>

Вам потрібно побудувати з джерела! Версії, які упаковуються в Ubuntu та Kali Linux, є старшими і не мають необхідних функцій для нашого рівня реверсування.

Вам знадобиться Вім.

<pre spellcheck="false">sudo apt install vim
</pre>

Вам потрібно буде оновити .VIMRC file.

<pre spellcheck="false">vim ~/.vimrc
</pre>

Тоді ...

<pre spellcheck="false">set number
set tabstop=2 &nbsp; &nbsp;
set shiftwidth=2
set expandtab&nbsp;
syntax on
set syntax=c&nbsp;
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

Вітаємо, що ви отримали миготливу програму C!

На нашому наступному уроці ми створимо просту програму "Привіт, Світ".