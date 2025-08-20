## part 17 - інструкція ROR

Для повного змісту всіх уроків, будь ласка, натисніть нижче, оскільки він дасть короткий короткий урок на додаток до тем, які він висвітлює.&nbsp;https://github.com/mytechnotalent/Reverse-Engineering-підручник

Команда ROR означає праворуч.

<div class="slate-resizable-image-embed slate-image-embed__resize-full-width"><img src="/imgs/1544181149655.jpg"/></div>

У нашому простому прикладі x64 на машині Ubuntu Linux вище ми бачимо we&nbsp;mov 1&nbsp;into&nbsp;al&nbsp;and rotate.

Бінарне представлення - __00000001b __. &nbsp;if ми __ror__ 1 біт. Значення просто стає __10000000b__, як показано нижче.

Спочатку ми складаємо and посилання:

__NASM -F ELF64 -O test.O test.ASM________________________________________________

__ld -o test test.o__

<div class="slate-resizable-image-embed slate-image-embed__resize-full-width"><img src="/imgs/1544181229818.jpg"/></div>

Тут ми можемо побачити в налагоджувач that&nbsp;al&nbsp;Starts with&nbsp;1&nbsp;and, коли ми маємо право, що йдеться To&nbsp;0000.

Наступного тижня ми зануримося в основи завантажувального сектору! Залишайтеся в курсі!