## part 17 - інструкція ROR

Для повного змісту всіх уроків, будь ласка, натисніть нижче, оскільки він дасть короткий короткий урок на додаток до тем, які він висвітлює.&nbsp;https://github.com/mytechnotalent/Reverse-Engineering-Tutorial

Команда ROR означає праворуч.

<div class="slate-resizable-image-embed slate-image-embed__resize-full-width"><img src="/imgs/1544181149655.jpg"/></div>

У нашому простому прикладі x64 на машині Ubuntu Linux вище ми бачимо We&nbsp;mov 1&nbsp;into&nbsp;al&nbsp; та обертатись 1.

Бінарне представлення - __00000001b __. &nbsp;if ми __ror__ 1 біт. Значення просто стає __10000000b__, як показано нижче.

Спочатку ми складаємо та пов'язуємо:

__NASM -f elf64 -o тест.o тест.asm__

__ld -o тест.O__

<div class="slate-resizable-image-embed slate-image-embed__resize-full-width"><img src="/imgs/1544181229818.jpg"/></div>

Тут ми можемо побачити в налагоджувачі thate&nbsp;al&nbsp;starts with&nbsp;1&nbsp;and, коли ми обертаємося праворуч, він йде to&nbsp;__10000000b__.

Наступного тижня ми зануримося в основи завантажувального сектору! Залишайтеся в курсі!