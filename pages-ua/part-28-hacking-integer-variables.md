Частина 28 – Хакінг цілих змінних

Для повного змісту всіх уроків натисніть нижче, оскільки це надасть вам короткий зміст кожного уроку, а також теми, які будуть розглянуті. https://github.com/mytechnotalent/Reverse-Engineering-Tutorial

Давайте переглянемо свій код. <XyZ9PlH0ZuK8 class="slate-resizable-image-embed slate-image-embed__resize-full-width"><img src="/imgs/1519988583160.jpg"/></XyZ9PlH1ZuK8>

Давайте хакнемо! <XyZ9PlH2ZuK8 class="slate-resizable-image-embed slate-image-embed__resize-full-width"><img src="/imgs/1519988510636.jpg"/></XyZ9PlH3ZuK8>

Давайте ще раз подивимося всередині пам'яті місця __0x10730__. <div class="slate-resizable-image-embed slate-image-embed__resize-full-width"><img src="/imgs/1519988543593.jpg"/></div>

Як ми можемо побачити, ціле значення __777__ з'являється, а коли ми продовжимо, воно відображається в терміналі значення __777__, яке відповідає нашій функції C++ __cout__.

Давайте хакнемо значення всередині __0x10730__ і встановимо значення __666__ і потім знову переглянемо значення всередині __0x10730__ і продовжимо. <div class="slate-resizable-image-embed slate-image-embed__resize-full-width"><img src="/imgs/1519988571825.jpg"/></div>

Успіх! Як ми можемо побачити, ми змінили значення на __666__, а коли продовжимо, воно відображається в stdout.

Наступна неділя ми вийдемо на тему Float змінних.