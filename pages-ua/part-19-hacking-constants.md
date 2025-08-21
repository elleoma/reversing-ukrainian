## Частина 19 – Хакінг констант

Для повного змісту всіх уроків натисніть нижче, оскільки це надасть вам короткий зміст кожного уроку, а також теми, які будуть розглянуті. https://github.com/mytechnotalent/Reverse-Engineering-Tutorial

Давайте переглянемо нашу початкову програму.

<XyZ9PlH0ZuK8 class="slate-resizable-image-embed slate-image-embed__resize-full-width"><img src="/imgs/1520195148562.jpg"/></XyZ9PlH1ZuK8>

Давайте хакнемо!

<XyZ9PlH2ZuK8 class="slate-resizable-image-embed slate-image-embed__resize-full-width"><img src="/imgs/1520144504108.jpg"/></XyZ9PlH3ZuK8>

Як ми бачимо, значення в адресі пам'яті __0x10730__ дорівнює __2017__. Давайте змінимо це значення в пам'яті на __1981__. Давайте продовжимо і побачимо, як значення зміниться на __1981__! Хакінг успішний!

Давайте спробуємо хакнути іншим шляхом! Відновіть програму і встановіть зупинку на main+28 і продовжуйте до зупинки.

<div class="slate-resizable-image-embed slate-image-embed__resize-full-width"><img src="/imgs/1520146785758.jpg"/></div>

Давайте продовжимо і побачимо, що значення в __r1__ дорівнює __2017__. Давайте змінимо значення в __r1__ на __1981__. Давайте продовжимо і побачимо, як програма успішно була хакнута на __1981__!

<div class="slate-resizable-image-embed slate-image-embed__resize-full-width"><img src="/imgs/1520148769675.jpg"/></div>

Наступна неділя ми вийдемо на тему Перемичок.

Харківський національний університет радіоелектроніки.