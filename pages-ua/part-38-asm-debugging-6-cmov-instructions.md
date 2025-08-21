## part 38 - налагодження ASM 6 \ [cmov інструкції \]

Для повного змісту всіх уроків, будь ласка, натисніть нижче, оскільки він дасть короткий короткий урок на додаток до тем, які він висвітлює.&nbsp;https://github.com/mytechnotalent/Reverse-Engineering-Tutorial

Давайте переглянемо деякий вихідний код.

<div class="slate-resizable-image-embed slate-image-embed__resize-full-width"><img src="/imgs/1520234974923.jpg"/></div>

Давайте розірвемося на 0x08048092, що є рядком 31. Давайте зробимо r для запуску, а потім введіть __print $ ebx__. Ми можемо побачити значення 7.

<div class="slate-resizable-image-embed slate-image-embed__resize-full-width"><img src="/imgs/1520240729383.jpg"/></div>

Гаразд, давайте розірветься на 0x080480b1, який є рядком 46. Пам'ятайте, коли ми вивчаємо значення __answer__, він був перетворений на його еквівалент для друку ASCII, щоб побачити значення "7", ви введете __X/1C &amp;ANANSWER__.

<div class="slate-resizable-image-embed slate-image-embed__resize-full-width"><img src="/imgs/1520498895208.jpg"/></div>

Я з нетерпінням чекаю побачити вас на весь наступний тиждень, коли ми занурюємось у зламу нашої шостої програми Асамблеї!