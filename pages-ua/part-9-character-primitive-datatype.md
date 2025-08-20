## part 9 - Первісний тип даних символів

Для повного змісту всіх уроків, натисніть нижче, оскільки він дасть короткий короткий урок на додаток до тем, які він висвітлює. https://github.com/mytechnotalent/hacking\_c-\_arm64

Сьогодні ми поговоримо про перший із примітивного C ++. _Char_ dataype використовується для зберігання одного символу and, повинен бути оточений одиночними цитатами.

Давайте подивимось на наш основний приклад.

<pre spellcheck="false">#include &lt;iostream&gt;

int main()
{
    char my_char = 'c';

    std::cout &lt;&lt; my_char &lt;&lt; std::endl;

    return 0;
}
</pre>

Надзвичайно простий. Ми просто створюємо змінну char під назвою _my \ _char _ і присвоюючи їй символ _c_.

Потім ми друкуємо його на stdout and більше нічого.

Давайте складемо and посилання.

<pre spellcheck="false">g++ -o 0x03_asm64_char_primitive_datatype 0x03_asm64_char_primitive_datatype.cpp
</pre>

Давайте біжимо.

<pre spellcheck="false">./0x03_asm64_char_primitive_datatype
</pre>

Дуже просто ми бачимо наступне.

<pre spellcheck="false">c
</pre>

Він успішно перегукувався _c_ до терміналу stdout. Дуже просто.

Наступного тижня ми налагоджуємо цей дуже простий приклад.