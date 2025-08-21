## Частина 43 - Хакінг Пойнтерів!

Для повного змісту всіх уроків натисніть нижче, оскільки це надасть вам короткий зміст кожного уроку, а також теми, які будуть розглянуті. https://github.com/mytechnotalent/Reverse-Engineering-Tutorial

Ми дійшли кінця шляху. Це останній відео в серії x64. Остання тема стосується вказівників.

Що таке вказівники? Давайте почнемо з прикладу.

<div class="slate-resizable-image-embed slate-image-embed__resize-full-width"><img src="/imgs/1567286671465.jpg"/></div>

Вказівник нічого не більше ніж адреса пам'яті. Коли ми компілюємо, ми побачимо, де живе lottery\_number в мапованій пам'яті (це є діючим прикладом, як наше не маповане Radare приклади).

<div class="slate-resizable-image-embed slate-image-embed__resize-full-width"><img src="/imgs/1567286745307.jpg"/></div>

Давайте додамо справжній вказівник до прикладу:

<div class="slate-resizable-image-embed slate-image-embed__resize-full-width"><img src="/imgs/1567287725406.jpg"/></div>

Ми бачимо той же значення:

<XyZ9PlH10ZuK8 class="slate-resizable-image-embed slate-image-embed__resize-full-width"><img src="/imgs/1567287787090.jpg"/></XyZ9PlH11ZuK8>

Давайте експериментуватимемо більше:

<XyZ9PlH12ZuK8 class="slate-resizable-image-embed slate-image-embed__resize-full-width"><img src="/imgs/1567288396508.jpg"/></XyZ9PlH13ZuK8>

Ми бачимо, що адреса вказівника вказує на нову адресу:

<XyZ9PlH14ZuK8 class="slate-resizable-image-embed slate-image-embed__resize-full-width"><img src="/imgs/1567288456995.jpg"/></XyZ9PlH15ZuK8>

Пам'ятайте, вказівники є адресами пам'яті інших змінних. Давайте розглянемо це інакше:

<XyZ9PlH16ZuK8 class="slate-resizable-image-embed slate-image-embed__resize-full-width"><img src="/imgs/1567289354121.jpg"/></XyZ9PlH17ZuK8>

Давайте компілюємо:

<XyZ9PlH18ZuK8 class="slate-resizable-image-embed slate-image-embed__resize-full-width"><img src="/imgs/1567289368216.jpg"/></XyZ9PlH19ZuK8>

Ми віддераціюємо, роблячи наступне:

<XyZ9PlH20ZuK8 class="slate-resizable-image-embed slate-image-embed__resize-full-width"><img src="/imgs/1567289646596.jpg"/></XyZ9PlH21ZuK8>

Далі ми компілюємо:

<XyZ9PlH22ZuK8 class="slate-resizable-image-embed slate-image-embed__resize-full-width"><img src="/imgs/1567289657671.jpg"/></XyZ9PlH23ZuK8>

Ми бачимо, що віддераційований вказівник рівний 777.

<XyZ9PlH24ZuK8 class="slate-resizable-image-embed slate-image-embed__resize-full-width"><img src="/imgs/1567290644015.jpg"/></XyZ9PlH25ZuK8>

Ми бачимо приклад з масивом:

<XyZ9PlH26ZuK8 class="slate-resizable-image-embed slate-image-embed__resize-full-width"><img src="/imgs/1567290665083.jpg"/></XyZ9PlH27ZuK8>

Давайте відлагодимо:

<XyZ9PlH28ZuK8 class="slate-resizable-image-embed slate-image-embed__resize-full-width"><img src="/imgs/1567290786481.jpg"/></XyZ9PlH29ZuK8>

Далі ми розіб'ємо:

<XyZ9PlH30ZuK8 class="slate-resizable-image-embed slate-image-embed__resize-full-width"><img src="/imgs/1567290800965.jpg"/></XyZ9PlH31ZuK8>

Давайте хакнемо!

<XyZ9PlH32ZuK8 class="slate-resizable-image-embed slate-image-embed__resize-full-width"><img src="/imgs/1567292294462.jpg"/></XyZ9PlH33ZuK8>

Давайте знову розглянемо байновий файл:

<XyZ9PlH34ZuK8 class="slate-resizable-image-embed slate-image-embed__resize-full-width"><img src="/imgs/1567292311387.jpg"/></XyZ9PlH35ZuK8>

Ми бачимо, що ми хакнули значення 3 на 6.

<XyZ9PlH36ZuK8 class="slate-resizable-image-embed slate-image-embed__resize-full-width"><img src="/imgs/1567292376880.jpg"/></XyZ9PlH37ZuK8>

Ми бачимо, що ми здійснили успішний хак.

Я сподіваюся, що протягом багатьох років через кілька сотень x86, ARM і x64 уроків ви маєте базову знання, як зробити ХОРОШО, щоб захистити критичні інфраструктури від зловмисних рук, розуміючи, як працює ворог. Ідіть і робіть ХОРОШО роботу