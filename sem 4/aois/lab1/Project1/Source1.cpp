#include <iostream>
#include <vector>

using namespace std;

struct binary_float {
	vector <bool> mantissa;
	vector <bool> index;
	bool sign;
};


const vector <bool> binary_zero = { 0, 0, 0, 0, 0, 0, 0, 0 };
const vector <bool> binary_one = { 0, 0, 0, 0, 0, 0, 0, 1 };
const vector <bool> minus_one_ñomplementary = { 1, 1, 1, 1, 1, 1, 1, 1 };
const int adicianal_zeros_to_eight = 8;
const int adicianal_zeros_to_twenty_three = 23;
const int perception = 127;

vector <bool> add(vector <bool> a, vector <bool> b)
{
	vector <bool> res;
	bool transfer = false;
	for (size_t i = a.size(); i > 0; i--)
	{

		if (a[i - 1] == 0 && b[i - 1] == 0 && !transfer)
		{
			res.emplace(res.begin(), 0);
			transfer = false;
		}
		else if (a[i - 1] == 0 && b[i - 1] == 0 && transfer)
		{
			res.emplace(res.begin(), 1);
			transfer = false;
		}
		else if (a[i - 1] == 1 && b[i - 1] == 0 && !transfer)
		{
			res.emplace(res.begin(), 1);
			transfer = false;
		}
		else if (a[i - 1] == 1 && b[i - 1] == 0 && transfer)
		{
			res.emplace(res.begin(), 0);
			transfer = true;
		}
		else if (a[i - 1] == 0 && b[i - 1] == 1 && !transfer)
		{
			res.emplace(res.begin(), 1);
			transfer = false;
		}
		else if (a[i - 1] == 0 && b[i - 1] == 1 && transfer)
		{
			res.emplace(res.begin(), 0);
			transfer = true;
		}
		else if (a[i - 1] == 1 && b[i - 1] == 1 && !transfer)
		{
			res.emplace(res.begin(), 0);
			transfer = true;
		}
		else if (a[i - 1] == 1 && b[i - 1] == 1 && transfer)
		{
			res.emplace(res.begin(), 1);
			transfer = true;
		}
	}
	return res;
}
void print(vector <bool> vec)
{
	for (size_t i = 0; i < vec.size(); i++)
	{
		cout << vec[i];
	}
}
vector <bool> to_binary(int num)
{
	vector <bool> res;
	int size;
	int num_;
	num_ = abs(num);
	while (num_)
	{
		res.emplace(res.begin(), num_ % 2);
		num_ /= 2;
	}
	size = res.size();
	for (size_t i = 0; i < adicianal_zeros_to_eight - size; i++)
	{
		res.emplace(res.begin(), 0);
	}
	if (num < 0)
	{
		res[0] = 1;
	}
	return res;
}
vector <bool> to_binary_inverse(int num)
{
	vector <bool> res = to_binary(num);
	if (num > 0)
	{
		res = to_binary(num);
	}
	else if (num < 0)
	{
		for (size_t i = 0; i < res.size(); i++)
		{
			res[i] = !res[i];
		}
		res[0] = 1;
	}
	return res;
}
vector <bool> to_binary_ñomplementary(int num)
{
	vector <bool> res = to_binary_inverse(num);
	if (num > 0)
	{
		res = to_binary(num);
	}
	else if (num < 0)
	{
		res = add(res, binary_one);
	}
	return res;
}
vector <bool> from_ñomplementary_to_inverse(vector <bool> bin)
{
	if (bin[0] == 1)
	{
		bin = add(bin, minus_one_ñomplementary);
		return bin;
	}
	else return bin;
}
vector <bool> from_inverse_to_straight(vector <bool> bin)
{
	if (bin[0] == 1)
	{
		for (int i = 0; i < 16; i++)
		{
			bin[i] = !bin[i];
		}
		bin[0] = 1;
		return bin;
	}
	else return bin;
}
vector <bool> from_straight_to_ñomplementary(vector <bool> bin)
{
	for (size_t i = 0; i < bin.size(); i++)
	{
		bin[i] = !bin[i];
	}
	bin[0] = 1;
	bin = add(bin, binary_one);
	return bin;
}

vector <bool> multiply(vector <bool> a, vector <bool> b)
{
	vector <bool> res = binary_zero;
	while (b != binary_zero)
	{
		res = add(a, res);
		b = add(b, minus_one_ñomplementary);
	}
	return res;
}
void division(vector <bool> a, vector <bool> b)
{
	vector <bool> res, remainder, temp_remainder;
	int times = 0;
	bool sign = false;
	if (a[0] == b[0])
	{
		sign = true;
	}
	a[0] = 0;
	b[0] = 1;
	b = from_straight_to_ñomplementary(b);
	while (1)
	{
		temp_remainder = add(a, b);
		if (temp_remainder[0] == 1)
		{
			break;
		}
		else
		{
			times++;
		}
		a = add(a, b);
	}
	for (int i = 0; i < 5; i++)
	{
		a.push_back(0);
		a.erase(a.begin());
		temp_remainder = add(a, b);
		if (temp_remainder[0] == 1)
		{
			remainder.push_back(0);
			continue;
		}
		else
		{
			remainder.push_back(1);
		}
		a = add(a, b);
	}
	res = to_binary(times);
	if (!sign)
	{
		res[0] = 1;
	}
	print(res);
	cout << ".";
	print(remainder);
}
vector <vector<bool>> from_float_to_binary_part2(float number)
{
	float integer, fractional = modf(number, &integer);
	vector <bool> fractional_bin, integer_bin = to_binary(integer);
	if (integer == 0)
	{
		integer_bin = binary_zero;
	}
	int counter = -1;
	while (fractional > 0)
	{
		if (fractional - pow(2., counter) >= 0)
		{
			fractional_bin.push_back(1);
			fractional -= pow(2., counter);
		}
		else
		{
			fractional_bin.push_back(0);
		}
		counter--;
	}
	vector <vector<bool>> result;
	result.push_back(integer_bin);
	result.push_back(fractional_bin);
	return result;
}
binary_float from_float_to_binary_part1(float number)
{
	binary_float res;
	res.index = binary_zero;
	res.sign = 0;
	if (number < 0)
	{
		res.sign = 1;
	}
	vector <vector<bool>> binary_number = from_float_to_binary_part2(number);
	vector <bool> integer_bin = binary_number[0];
	vector <bool>fractional_bin = binary_number[1];
	if (integer_bin == binary_zero)
	{
		while (integer_bin != binary_one)
		{
			integer_bin.emplace(integer_bin.end(), fractional_bin[0]);
			integer_bin.erase(integer_bin.begin());
			fractional_bin.erase(fractional_bin.begin());
			fractional_bin.emplace(fractional_bin.end(), 0);
			res.index = add(res.index, minus_one_ñomplementary);
		}
	}
	while (integer_bin != binary_one)
	{
		fractional_bin.emplace(fractional_bin.begin(), integer_bin[integer_bin.size() - 1]);
		integer_bin.erase(integer_bin.end() - 1);
		integer_bin.emplace(integer_bin.begin(), 0);
		res.index = add(res.index, binary_one);
	}
	res.index = add(res.index, to_binary(perception));
	for (size_t i = 0; i < adicianal_zeros_to_eight - res.index.size(); i++)
	{
		res.index.emplace(res.index.begin(), 0);
	}
	res.mantissa = fractional_bin;
	for (size_t i = res.mantissa.size(); i < adicianal_zeros_to_twenty_three; i++)
	{
		res.mantissa.push_back(0);
	}

	return res;
}
bool lower_index(binary_float a, binary_float b)
{
	if (add(a.index, multiply(b.index, minus_one_ñomplementary))[0] == 1)
	{
		return 1;
	}
	else
	{
		return 0;
	}

}
pair <binary_float, binary_float> alignment_of_indexes(binary_float a, binary_float b)
{
	int times = 0;
	while (a.index != b.index)
	{
		a.index = add(a.index, binary_one);
		times < 1 ? a.mantissa.emplace(a.mantissa.begin(), 1) : a.mantissa.emplace(a.mantissa.begin(), 0);
		a.mantissa.erase(a.mantissa.end() - 1);
		++times;
	}
	times == 0 ? a.mantissa.emplace(a.mantissa.begin(), 1) : a.mantissa.emplace(a.mantissa.begin(), 0);
	a.index = add(a.index, binary_one);
	a.mantissa.erase(a.mantissa.end() - 1);
	b.mantissa.emplace(b.mantissa.begin(), 1);
	b.index = add(b.index, binary_one);
	b.mantissa.erase(b.mantissa.end() - 1);
	pair <binary_float, binary_float> pair_of_terms(a, b);
	return pair_of_terms;
}
binary_float float_add(binary_float a, binary_float b)
{
	binary_float res;
	pair <binary_float, binary_float> pair_of_terms;
	if (lower_index(a, b))
	{
		pair_of_terms = alignment_of_indexes(a, b);
	}
	else
	{
		pair_of_terms = alignment_of_indexes(b, a);
	}
	a = pair_of_terms.first;
	b = pair_of_terms.second;
	a.mantissa.emplace(a.mantissa.begin(), 0);
	b.mantissa.emplace(b.mantissa.begin(), 0);
	res.index = b.index;
	res.mantissa = add(a.mantissa, b.mantissa);
	if (!res.mantissa[0])
	{
		res.index = add(res.index, minus_one_ñomplementary);
		res.mantissa.erase(res.mantissa.begin());
		res.mantissa.emplace(res.mantissa.end(), 0);
	}
	res.mantissa.erase(res.mantissa.begin());
	res.sign = 0;
	return res;
}

void print_binary_float(binary_float a)
{
	cout << a.sign << " ";
	print(a.index);
	cout << " ";
	print(a.mantissa);
}
void generate_menu1()
{
	cout << "1) Integer numbers operations\n";
	cout << "2) Float numbers summary\n";
}
void generate_menu2()
{
	cout << "1) x1 + x2\n";
	cout << "2) x1 * x2\n";
	cout << "3) x1 / x2\n\n";
}


int main()
{
	int input1;
	generate_menu1();
	cin >> input1;
	system("cls");
	vector <bool> x1_;
	vector <bool> x2_;
	switch (input1)
	{
	case 1:
		int x1, x2, input2;
		cin >> x1 >> x2;
		generate_menu2();
		x1_ = to_binary(x1);
		x2_ = to_binary(x2);
		cin >> input2;
		switch (input2) {
		case 1:
			if (x1_[0] == 1) x1_ = from_straight_to_ñomplementary(x1_);
			if (x2_[0] == 1) x2_ = from_straight_to_ñomplementary(x2_);
			print(add(x1_, x2_));
			break;
		case 2:
			print(multiply(x1_, x2_));
			break;
		case 3:
			x1_ = to_binary(x1);
			x2_ = to_binary(x2);
			division(x1_, x2_);
			break;

		}
		break;
	case 2:
		float f1, f2;
		cin >> f1 >> f2;
		binary_float f1_ = from_float_to_binary_part1(f1);
		binary_float f2_ = from_float_to_binary_part1(f2);
		print_binary_float(f1_);
		cout << "\n+\n";
		print_binary_float(f2_);
		cout << "\n--------------------------------\n";
		print_binary_float(float_add(f1_, f2_));
		break;
	}

	return 0;
}
