Частина 22 – Хакінг змінних характеру

Для повного змісту змісту всіх уроків натисніть нижче, оскільки це надасть вам короткий зміст кожного уроку, а також теми, які будуть обговорені. https://github.com/mytechnotalent/Reverse-Engineering-Tutorial

Давайте переглянемо свій код.

<div class="slate-resizable-image-embed slate-image-embed__resize-full-width"><img src="/imgs/1520232430320.jpg"/></div>

Давайте хакнемо!

<div class="slate-resizable-image-embed slate-image-embed__resize-full-width"><img src="/imgs/1520194771044.jpg"/></div>

Ми знову бачимо прямий вміст __0x6e__ переміщений у __r3__ в __main+12__ який є нашим ‘__n__’.

<div class="slate-resizable-image-embed slate-image-embed__resize-full-width"><img src="/imgs/1520195499705.jpg"/></div>

Після кроку в 4 рази і перевірки значення в __r3__ яке ми чітко бачимо як ‘__n__’.

<div class="slate-resizable-image-embed slate-image-embed__resize-full-width"><img src="/imgs/1520233196032.jpg"/></div>

Давайте хакнемо значення в __r3__ на ‘__y__’ і потім знову переглянемо значення в __r3__.  Тепер ми чітко бачимо, що воно змінилося на ‘__y__’.

<div class="slate-resizable-image-embed slate-image-embed__resize-full-width"><img src="/imgs/1520232999022.jpg"/></div>

Поки продовжується, ми успішно бачимо, що наш хак працював!  Ми бачимо значення ‘__y__’ друкується в стандартний вивід.

Наступна неділя ми вийдемо в Булеві змінні.