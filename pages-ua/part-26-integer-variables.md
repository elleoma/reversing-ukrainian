## part 26 - цілі змінні

Для повного змісту всіх уроків, будь ласка, натисніть нижче, оскільки він дасть короткий короткий урок на додаток до тем, які він висвітлює.&nbsp;https://github.com/mytechnotalent/Reverse-Engineering-Tutorial

Наступний етап нашої подорожі - це цілі змінні.&nbsp;

32-бітний реєстр може зберігати 2^32 різні значення. Діапазон цілих значень, які можна зберігати в 32 бітах, залежить від використання цілого представлення. З двома найпоширенішими уявленнями, діапазон становить від 0 до 4,294,967,295 (2^32 - 1) для представлення як (неподписаного) бінарного числа та −2,147,483,648 (−2^31) через 2,147,483,647 (2^31 - 1) для представлення як два доповнення.

Майте на увазі 32-бітні адреси пам'яті, ви можете безпосередньо отримати доступ до максимуму 4 ГБ пам'яті, що відповідає байтом.

Давайте розглянемо наш код.

<pre spellcheck="false">#include &lt;iostream&gt;

&nbsp;

int main(void) {

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; int myNumber = 777;

&nbsp;

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; std::cout &lt;&lt; myNumber &lt;&lt; std::endl;

&nbsp;

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; return 0;

}
</pre>

<div class="slate-resizable-image-embed slate-image-embed__resize-full-width"><img src="/imgs/1520215369999.jpg"/></div>

Щоб скласти це, ми просто вводимо:

g ++ example5.cpp -o example5

./example5

<div class="slate-resizable-image-embed slate-image-embed__resize-full-width"><img src="/imgs/1520195285687.jpg"/></div>

Успіх! &nbsp;we дивись __777__ надруковано до стандартного виходу або терміналу!

Давайте розберемо його:

Ми присвоюємо ціле число __777 __ безпосередньо у змінну __mynumber __ і потім роздрукуємо його до терміналу за допомогою функції C ++ __cout__.

Наступного тижня ми зануримося в налагодження цілих змінних.