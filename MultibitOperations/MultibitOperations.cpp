// MultibitOperations.cpp : This file contains the 'main' function. Program execution begins and ends there.
//

/*
Author: Marcin Ziajkowski
*/

#include "pch.h"
#include <iostream>

using namespace std;

const unsigned int UIntBinaryDigitalsToDecimalDigitalsAmount(unsigned int binary_bits_amount)
{
	return ((binary_bits_amount * 3) / 10) + 1;
}
const unsigned int BitsToDecDig(unsigned int binary_bits_amount)
{
	return UIntBinaryDigitalsToDecimalDigitalsAmount(binary_bits_amount);
}

const unsigned int UIntDecimalDigitalsToBinaryDigitalsAmount(unsigned int decimal_digits_amount)
{
	unsigned int tmp = (decimal_digits_amount % 3) ? (decimal_digits_amount / 3) + 1 : (decimal_digits_amount / 3);
	return (decimal_digits_amount * 3) + tmp;
}
const unsigned int DecDigToBits(unsigned int decimal_digits_amount)
{
	return UIntDecimalDigitalsToBinaryDigitalsAmount(decimal_digits_amount);
}

template <class DATA_IN, class DATA_OUT, class FUNC >
bool test_negative(DATA_IN tab_in, DATA_OUT tab_out, FUNC func, const unsigned int range = 1) // type (*func)()
{
	int faults = 0;
	for (int i = 0; i < range; i++) if (func(tab_in[i]) != tab_out[i]) { ++faults; break; }
	return !!faults;
}
template <class DATA_IN, class DATA_OUT, class FUNC >
bool test_positive(DATA_IN tab_in, DATA_OUT tab_out, FUNC func, const unsigned int range = 1) // type (*func)()
{
	return !test_negative(tab_in, tab_out, func, range);
}


int main()
{
	int tab_res1[10]    = { 4,7,10,14,17,20,24,27,30,34 };
	int tab_res2[10]    = { 1,1,1,2,2,2,3,3,3,4 };
	int initial_tab[10] = { 1,2,3,4,5,6,7,8,9,10};

	for (int i = 1; i <= 10; i += 1) {
		cout <<i<<" : "<< DecDigToBits(i)  <<" / "<<tab_res1[i-1]<< endl; }
	for (int i = 1; i <= 10; i += 1) {
		cout << i << " : " << BitsToDecDig(i) << " / " << tab_res2[i-1] << endl; }

	cout << std::boolalpha << test_positive(initial_tab, tab_res1, DecDigToBits, 10)<<"\n";
	cout << std::boolalpha << test_positive(initial_tab, tab_res2, BitsToDecDig, 10)<<"\n";
	cout<<std::noboolalpha;
	
}
