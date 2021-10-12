//Eight usual sorting algorithms
//written by xu yongjie 2016-12-29
//>>>For communicating only!<<<
#include<iostream>
#include <cstring>
using namespace std;

template<typename Type>
void bubbleSort(Type* list, int len);
template<typename Type>
void altBubbleSort(Type* list, int len);
template<typename Type>
void insertionSort(Type* list, int len);
template<typename Type>
void exchange(Type* list, int u, int v);
template<typename Type>
void downNode(Type* list, int len, int i);
template<typename Type>
bool pri(Type a, Type b);
template<typename Type>
void heapSort(Type* list, int len);
template<typename Type>
Type pop(Type* list, int* len);
template<typename Type>
void merge(Type* list, Type* outlist, int len, int mid);
template<typename Type>
void mergeSort(Type* list, Type* temp, int len);
template<typename Type>
void quickSort(Type* list, int len);
template<typename Type>
void bucketSort(Type* list, int len);
int getDigit(int num, int n);
template<typename Type>
void radixSort(Type* list, int len);

int main(int argc, char const *argv[])
{
	int len;
	cin >> len;
	int* list = new int[len + 1];
	for (int i = 1; i <= len; i++)
		cin >> list[i];
	bool equal = true;
	if (!strcmp(argv[1], "-bubble"))
		bubbleSort(list + 1, len);
	else if (!strcmp(argv[1], "-altbubble"))
		altBubbleSort(list + 1, len);
	else if (!strcmp(argv[1], "-insertion"))
		insertionSort(list + 1, len);
	else if (!strcmp(argv[1], "-heap"))
		heapSort(list, len);
	else if (!strcmp(argv[1], "-merge"))
	{
		int* temp = new int[len];
		mergeSort(list + 1, temp, len);
		delete[] temp;
	}
	else if (!strcmp(argv[1], "-quick"))
		quickSort(list + 1, len);
	else if (!strcmp(argv[1], "-bucket"))
		bucketSort(list + 1, len);
	else if (!strcmp(argv[1], "-radix"))
		radixSort(list + 1, len);

	//for (int i = 1; i <= len; i++)
		//cout << list[i] << endl;
	delete[] list;
	cin.get();
	cin.get();
}
//	>>>>>these two functions below are used in several sorting algorithms<<<<<  //

template<typename Type>
bool pri(Type a, Type b)
{ //return true if a's priority is bigger
	if (a < b)//>>>>>>the condition here can be defined by yourself<<<<<<<//
		return true;
	return false;
}

template<typename Type>
void exchange(Type* list, int u, int v)
{//exchange two nodes in
	Type temp;
	temp = list[u];
	list[u] = list[v];
	list[v] = temp;
}
//////////////////////////////////////////////
template<typename Type>
void bubbleSort(Type* list, int len)
{//flagged and range limiting bubble sort
	for (int i = len - 1; i > 0;)
	{
		Type max = list[0];
		bool sorted = true;//flage
		int ii = 0;//range limiting
		for (int j = 1; j <= i; j++)
		{
			if (pri(list[j], max))
			{
				list[j - 1] = list[j];
				sorted = false;
				ii = j - 1;
			}
			else
			{
				list[j - 1] = max;
				max = list[j];
			}
		}
		list[i] = max;
		if (sorted)
			break;
		i = ii;
	}
}
////////////////////////////////////////////////
template<typename Type>
void altBubbleSort(Type* list, int len)
{//alternating, flagged and range limiting bubble sort
	int front = 0;
	for (int i = len - 1; i > 0;)
	{
		Type max = list[front];
		bool sorted = true;
		int ii = 0;
		int frontii = 0;
		for (int j = front + 1; j <= i; j++)
		{//go from front to back
			if (pri(list[j], max))
			{
				list[j - 1] = list[j];
				sorted = false;
				ii = j - 1;
			}
			else
			{
				list[j - 1] = max;
				max = list[j];
			}
		}
		list[i] = max;
		if (sorted)
			break;
		i = ii;
		sorted = true;
		Type min = list[i];
		for (int j = i - 1; j >= front; j--)
		{//go from back to front
			if (pri(min, list[j]))
			{
				list[j + 1] = list[j];
				sorted = false;
				frontii = j + 1;
			}
			else
			{
				list[j + 1] = min;
				min = list[j];
			}
		}
		list[front] = min;
		if (sorted)
			break;
		front = frontii;
	}
}
/////////////////////////////////////////////
template<typename Type>
void insertionSort(Type* list, int len)
{
	for (int i = 1; i < len; i++)
	{
		int temp = list[i];
		int j = i - 1;
		for (j; j >= 1; j--)
		{
			if (pri(temp, list[j]))
				list[j + 1] = list[j];
			else
			{
				list[j + 1] = temp;
				goto g;// use 'goto' to avoid repeaded check
			}
		}
		if (pri(temp, list[0]))
		{//special when come to the first one
			list[1] = list[0];
			list[0] = temp;
		}
		else
			list[1] = temp;
	g:;
	}
}
/////////////////////////////////////////////////////////////
template<typename Type>
void downNode(Type* list, int len, int i)
{//to let a node go down, stop if the one below is bigger  
	bool b;
	while (2 * i <= len)
	{
		if (2 * i == len)
		{
			if (pri(list[i], list[2 * i]))
				exchange(list, i, 2 * i);
			break;
		}
		else if (pri(list[i], list[2 * i]) ||
			pri(list[i], list[2 * i + 1]))
		{
			b = pri(list[2 * i], list[2 * i + 1]);
			exchange(list, i, 2 * i + b);
			i = 2 * i + b;
		}
		else
			break;
	}
}

template<typename Type>
Type pop(Type* list, int* len)
{//take out a node
	Type temp = list[1];
	list[1] = list[*len];
	list[*len] = 0;
	*len -= 1;
	downNode(list, *len, 1);
	return temp;
}

template<typename Type>
void heapSort(Type* list, int len)
{
	int len0 = len;
	for (int m = len; m > 1; m /= 2)
	{
		for (int i = m / 2; i >= m / 4 + 1; i--)
			downNode(list, len, i);
	}
	for (int i = 1; i < len0; i++)
		list[len] = pop(list, &len);
}

//////////////////////////////////////////////////////
template<typename Type>
void merge(Type* list, Type* outlist, int len, int mid)
{//merge two sorted list into one
	int i1 = 0, i2 = mid, k = 0;
	while (i1 < mid && i2 < len)
	{
		if (pri(list[i1], list[i2]))
		{
			outlist[k] = list[i1];
			i1++;
		}
		else
		{
			outlist[k] = list[i2];
			i2++;
		}
		k++;
	}
	for (i1; i1 < mid; i1++, k++)
		outlist[k] = list[i1];
	for (i2; i2 < len; i2++, k++)
		outlist[k] = list[i2];
	for (int i = 0; i < len; i++)
		list[i] = outlist[i];
}

template<typename Type>
void mergeSort(Type* list, Type* temp, int len)
{
	if (len < 15)
		insertionSort(list, len);
	else
	{
		int mid = len / 2;
		mergeSort(list, temp, mid);
		mergeSort(list + mid, temp, len - mid);
		merge(list, temp, len, mid);
	}
}
///////////////////////////////////////////////////////
template<typename Type>
void quickSort(Type* list, int len)
{
	if (len < 64)
	{
		insertionSort(list, len);
		return;
	}
	int indexs[3] = { 0, len - 1, len / 2 };
	Type pivot;
	int index;
	for (int i = 0; i < 3; i++)
	{//find the mid one of three numbers
		if ((!pri(list[indexs[i]], list[indexs[(i + 1) % 3]]) && !pri(list[indexs[(i + 2) % 3]], list[indexs[i]]))
			|| (!pri(list[indexs[(i + 1) % 3]], list[indexs[i]]) && !pri(list[indexs[i]], list[indexs[(i + 2) % 3]])))
		{
			index = indexs[i];
			break;
		}
	}
	pivot = list[index];
	list[index] = list[len - 1];
	int big = 0, small = len - 1;//small should be len - 1 rather than len - 2 to avoid the case pivot is the biggest one
	for (big; big < small; big++)
	{
		if (pri(pivot, list[big]))
		{
			small -= 1;
			for (small; big < small; small--)
			{
				if (pri(list[small], pivot))
				{
					exchange(list, big, small);
					break;
				}
			}
		}
	}
	list[len - 1] = list[small];
	list[small] = pivot;
	quickSort(list, small);
	quickSort(list + small + 1, len - small - 1);
}
////////////////////////////////////////////////////////
template<typename Type>
struct bucket
{
	int len = 0;
	int num = 0;
	Type* list;
};

template<typename Type>
void bucketSort(Type* list, int len)
{
	int scale = 32;//the scale of each bucket we assume
	int num = len / scale + 1;//the number of all buckets
	int min, max;
	min = max = list[0];
	for (int i = 1; i < len; i++)
	{//find the biggest and smallest ones to determin the span of number of a bucket
		list[i] < min ? min = list[i] : 0;
		list[i] > max ? max = list[i] : 0;
	}
	int divide = (max - min) / num + 1;//the span of number of a bucket
	bucket<Type>** bucList = new bucket<Type>*[num += 1];
	for (int i = 0; i < num; i++)
		bucList[i] = new bucket<Type>;
	for (int i = 0; i < len; i++)//find the real scale of each bucket
		bucList[(list[i] - min) / divide]->len += 1;
	for (int i = 0; i < num; i++)
		bucList[i]->list = new Type[bucList[i]->len];
	for (int i = 0; i < len; i++)
	{
		int temp = (list[i] - min) / divide;
		bucList[temp]->list[bucList[temp]->num] = list[i];
		bucList[temp]->num += 1;
	}
	int temp = 0;
	for (int i = 0; i < num; i++)
	{//copy the ranked numbers in every bucket back to origin list
		insertionSort(bucList[i]->list, bucList[i]->len);
		for (int j = 0; j < bucList[i]->len; j++)
			list[j + temp] = bucList[i]->list[j];
		temp += bucList[i]->len;
		delete[] bucList[i]->list;
		delete bucList[i];
	}
	delete[] bucList;
}
//////////////////////////////////////////////////////////
int getDigit(int num, int n)
{//get the n th(from right) digit of a number
	for (int i = 1; i < n; i++)
		num /= 10;
	return num % 10;
}

template<typename Type>
void radixSort(Type* list, int len)
{
	int n = 0, max, min;
	min = max = list[0];
	for (int i = 1; i < len; i++)
	{
		list[i] < min ? min = list[i] : 0;
		list[i] > max ? max = list[i] : 0;
	}
	-min > max ? max = -min : 0;
	while (max != 0)
	{
		max /= 10;
		n += 1;//find the longest digit length
	}
	Type* list0 = new Type[len];
	Type* radix[19] = {};//there are 19 digits (from -9 to 9)
	int count[19] = {};//a list record the length of every radix
	for (int i = 1; i <= n; i++)
	{
		for (int j = 0; j < len; j++)
			count[getDigit(list[j], i) + 9] += 1;
		int sum = 0;
		for (int j = 0; j < 19; sum += count[j], j++)
			radix[j] = list0 + sum;
		for (int j = 0; j < 19; j++)
			count[j] = 0;
		int temp = 0;
		for (int j = 0; j < len; j++)
		{
			temp = getDigit(list[j], i) + 9;
			radix[temp][count[temp]] = list[j];
			count[temp] += 1;
		}
		for (int k = 0; k < len; k++)
			list[k] = list0[k];
		for (int j = 0; j < 19; j++)
			count[j] = 0;
	}
	delete[] list0;
}
