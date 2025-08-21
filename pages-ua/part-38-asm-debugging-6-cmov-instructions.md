## Частина 38 - Дебагування ASM 6 \[CMOV Інструкції\]

Для повного змісту змісту всіх уроків, будь ласка, натисніть нижче, оскільки це надасть вам короткий зміст кожного уроку, а також теми, які будуть розглянуті. https://github.com/mytechnotalent/Reverse-Engineering-Tutorial

Давайте знову розглянемо деякий джерельний код.

<XyZ9PlH0ZuK8 class="slate-resizable-image-embed slate-image-embed__resize-full-width"><img src="/imgs/1520234974923.jpg"/></XyZ9PlH1ZuK8>

Давайте зупинимося на 0x08048092, який є рядком 31. Давайте зробимо r, щоб запустити, а потім введемо __print $ebx__. Ми побачимо значення 7.

<XyZ9PlH2ZuK8 class="slate-resizable-image-embed slate-image-embed__resize-full-width"><img src="/imgs/1520240729383.jpg"/></XyZ9PlH3ZuK8>

Окей, тепер давайте зупинимося на 0x080480b1, який є рядком 46. Пам'ятайте, коли ми досліджуємо значення __answer__, воно вже було перетворено на його еквівалент ASCII, який можна вивести, тому щоб побачити значення ‘7’, потрібно ввести __x/1c &amp;answer__.

<XyZ9PlH4ZuK8 class="slate-resizable-image-embed slate-image-embed__resize-full-width"><img src="/imgs/1520498895208.jpg"/></XyZ9PlH5ZuK8>

Я чекаю на всіх вас наступної тижня, коли ми вийдемо на хакінг наш шостий програму збірки!

Дякую за увагу!