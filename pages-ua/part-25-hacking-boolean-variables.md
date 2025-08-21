## Частина 25 – Хакінг булевих змінних

Для повного змісту всіх уроків натисніть нижче, оскільки це надасть вам короткий зміст кожного уроку, а також теми, які будуть розглянуті. https://github.com/mytechnotalent/Reverse-Engineering-Tutorial

Давайте знову переглянемо наш код.

<XyZ9PlH0ZuK8 class="slate-resizable-image-embed slate-image-embed__resize-full-width"><img src="/imgs/1520191957701.jpg"/></XyZ9PlH1ZuK8>

Давайте хакнемо!

<XyZ9PlH2ZuK8 class="slate-resizable-image-embed slate-image-embed__resize-full-width"><img src="/imgs/1520210981189.jpg"/></XyZ9PlH3ZuK8>

Давайте зупинимося на головній, запустимо і розіб'ємо, а також крок за кроком увійдіть чотири рази.

<div class="slate-resizable-image-embed slate-image-embed__resize-full-width"><img src="/imgs/1520146846926.jpg"/></div>

Ми бачимо, що __0__ або __FALSE__ переміщені в __r3__ на main+12.

<div class="slate-resizable-image-embed slate-image-embed__resize-full-width"><img src="/imgs/1520218746699.jpg"/></div>

Дуже просто ми встановлюємо __r3__ на __1__ або __TRUE__ і продовжимо виконання, під час якого ми помітили, що булеве змінне __isHacked__ тепер __TRUE__.

Так просто, люди! Ці прості приклади допоможуть збудувати вашу бібліотеку прикладів, як підійти до всього в коді і розуміти, як взяти під свій контроль виконання коду, незалежно від того!

Наступна неділя ми вийдемо в глибину з цілих змінних.