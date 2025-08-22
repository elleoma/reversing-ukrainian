## Частина 18 - Двійна примітивна тип даних

Для повного змісту всіх уроків натисніть нижче, оскільки це надасть вам короткий зміст кожного уроку, а також теми, які будуть розглянуті. https://github.com/mytechnotalent/hacking\_c-\_arm64

Сьогодні ми розберемося з C++ _double_ типом даних, який зберігає подвійні значення з плаваючою комою.

<pre spellcheck="false">#include &lt;iostream&gt;

int main()
{
&nbsp; &nbsp; double my_double = 10.1;

&nbsp; &nbsp; std::cout &lt;&lt; my_double &lt;&lt; std::endl;

&nbsp; &nbsp; return 0;
}
</pre>

Дуже просто ми створюємо змінну типу float і присвоюємо їй просте значення, а потім друкуємо її.

Хай ми скомпілюємо і зв'яземо.

<pre spellcheck="false">g++ -o 0x06_double_primitive_datatype 0x05_double_primitive_datatype.cpp
</pre>

Хай ми запустимо.

<pre spellcheck="false">./0x06_double_primitive_datatype
</pre>

Ми просто побачили наступне.

<pre spellcheck="false">10.1
</pre>

Вище вказаний приклад успішно вивів _10.1_ у термінальний вивід stdout. Дуже просто.

Наступного тижня ми відлагодимо цей дуже простий приклад.