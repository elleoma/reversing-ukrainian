## part 20 - змінні символи

Для повного змісту всіх уроків, будь ласка, натисніть нижче, оскільки він дасть короткий короткий урок на додаток до тем, які він висвітлює.&nbsp;https://github.com/mytechnotalent/Reverse-Engineering-підручник

Наступний етап нашої подорожі - це змінні символів.&nbsp;unly strings, з яким ми мали справу, персонаж займає лише один байт даних.

Майте на увазі, коли ми маємо справу з будь -якими даними персонажів, ми маємо справу з буквально двома шестигранними цифрами, які є кодом ASCII, який представляє фактичний персонаж, який ми бачимо у наших відповідних терміналах.

Пам'ятайте, що кожна шістнадцяткова цифра довжиною 4 біти.&nbsp;. Дві шестигранні цифри мають 8 біт довжиною or byte long.nbsp

Для резюме, кожен персонаж перекладається на код ASCII у HEX, який процесор розуміє.&nbsp; Вартість __n__ становить __0x6e__ hex or __110__ decimal.&nbsp;youous переглянути будь -яку таблицю ASCII, щоб побачити, коли ми отримали цю цінність.xyz9yum75 зручно на наступному уроці.

Ми починаємо з нашої третьої програми в C ++, яка є нашою програмою "Змінна символів ".&nbsp;let's Dive в and розірвати кожен рядок вниз поетапно and див., Як працює ця мова.nbspwe call to iteakpppppps53 пристрій.

<pre spellcheck="false">#include &lt;iostream&gt;

&nbsp;

int main(void) {

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; char yes_no = ‘n’;

&nbsp;

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; std::cout &lt;&lt; yes_no &lt;&lt; std::endl;

&nbsp;

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; return 0;

}
</pre>

<div class="slate-resizable-image-embed slate-image-embed__resize-full-width"><img src="/imgs/1520190636660.jpg"/></div>

Щоб скласти це, ми просто вводимо:

g ++ example3.cpp -o example3

Ми просто тоді вводимо:

./example3

<div class="slate-resizable-image-embed slate-image-embed__resize-full-width"><img src="/imgs/1520211586776.jpg"/></div>

Успіх! &nbsp;WE див. "__N__", надрукований до стандартного виводу or термінал!

Давайте розберемо його:

Ми використовуємо __CHAR __KeyWord, щоб вказати змінну символу, до якої ми присвоюємо це значення __N__.

Потім ми використовуємо __cout __function, щоб надрукувати її до стандартного виводу or термінал nbsp nbsp нова лінія з функцією __endl__.

Це все! &nbsp;very просто.

Наступного тижня ми зануримося у налагодження змінних символів.