## Частина 20 – Перемінні Характерів

Для повного змісту всіх уроків натисніть нижче, оскільки це надасть вам короткий зміст кожного уроку, а також теми, які будуть розглянуті. https://github.com/mytechnotalent/Reverse-Engineering-Tutorial

Наступний етап нашої подорожі – це змінні характерів. strings, яких ми вже розглядали раніше, змінна характеру займає лише один байт даних.

Увага! Коли ми працюємо з будь-якою інформацією характерів, ми працюємо з буквально двома шістнадцятковими цифрами, які є шістнадцятковим кодом ASCII, який представляє справжній символ, який ми бачимо на своїх термінальних пристроях.

Пам'ятайте, кожна шістнадцяткова цифра має довжину 4 біта. <pre spellcheck="false">#include &lt;iostream&gt;

&nbsp;

int main(void) {

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; char yes_no = ‘n’;

&nbsp;

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; std::cout &lt;&lt; yes_no &lt;&lt; std::endl;

&nbsp;

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; return 0;

}
</pre>, тому дві шістнадцяткові цифри мають довжину 8 біта або 1 байт. <div class="slate-resizable-image-embed slate-image-embed__resize-full-width"><img src="/imgs/1520190636660.jpg"/></div>

У підсумку кожен символ перекладається в шістнадцятковий код ASCII, який розуміє процесор. call значення __n__ становить __0x6e__ шістнадцятковий або __110__ десятковий. <div class="slate-resizable-image-embed slate-image-embed__resize-full-width"><img src="/imgs/1520211586776.jpg"/></div> ви можете переглянути будь-яку таблицю ASCII, щоб побачити, звідки ми отримали цей значення. /example3 це буде дуже корисно на наступному уроку.

Ми починаємо з нашою третьою програмою на C++, яка називається програмою змінної характеру. <pre spellcheck="false">#include &lt;iostream&gt;

&nbsp;

int main(void) {

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; char yes_no = ‘n’;

&nbsp;

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; std::cout &lt;&lt; yes_no &lt;&lt; std::endl;

&nbsp;

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; return 0;

}
</pre> Давайте увійдемо в неї і розіб'ємо кожну рядок крок за кроком, щоб побачити, як ця мова працює. <div class="slate-resizable-image-embed slate-image-embed__resize-full-width"><img src="/imgs/1520190636660.jpg"/></div> ми використовуватимемо приклад example3.cpp і збережемо його на нашому пристрої.

Для компіляції цього ми просто набираємо:

g++ example3.cpp -o example3

Далі ми просто набираємо:./example3

<div class="slate-resizable-image-embed slate-image-embed__resize-full-width"><img src="/imgs/1520211586776.jpg"/></div>

Успіх! <pre spellcheck="false">#include &lt;iostream&gt;

&nbsp;

int main(void) {

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; char yes_no = ‘n’;

&nbsp;

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; std::cout &lt;&lt; yes_no &lt;&lt; std::endl;

&nbsp;

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; return 0;

}
</pre> ми бачимо «__n__» надруковано в стандартному виході або терміналі!

Давайте розберемо це:

Ми використовуємо ключове слово __char __, щоб вказати змінну характеру, якій ми присвоюємо значення __n__.

Далі ми використовуємо функцію __cout __, щоб надрукувати його в стандартний вивід або термінал, і додати нову строку з допомогою функції __endl__.

Так! <pre spellcheck="false">#include &lt;iostream&gt;

&nbsp;

int main(void) {

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; char yes_no = ‘n’;

&nbsp;

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; std::cout &lt;&lt; yes_no &lt;&lt; std::endl;

&nbsp;

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; return 0;

}
</pre> дуже просто.

Наступного тижня ми увійдемо в Розробку Змінних Характерів.