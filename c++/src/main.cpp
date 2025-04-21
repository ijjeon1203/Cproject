#include <iostream>
#include <vector>


//////////////
#include <string>
#include <bitset>
#include <sstream>


////////

//#include <iostream>
//#include <vector>
//#include <string>
//#include <bitset>




/// <summary>
/// </summary>

using namespace std;
/*
input
- combi
- front end
- total count

total 개수와 start 입력
출력

case ~10 개

*/


void inputBinaryDatas(vector<string>& values) {

	string line;
	while (true) {
		std::getline(std::cin, line);
		if (line.empty()) {
			break;  // 빈 줄 입력 시 종료}
			if (line.length() != 8) {
				//std::cerr << "⚠️ 8자리 이진수만 입력하세요. 입력된 값: [" << line << "]" << std::endl;
				cerr << " only 8자리 이진수" << endl;
				continue;
			}
		}

		values.push_back(line);
	}
}

void makeAbnormalTestData(vector<string>& values, vector<string>& values2) {

	for (string& value : values) {
		string flipped = value;
		for (char& ch : flipped) {
			if (ch == '0') { ch = '1'; }
			else if (ch == '1') {
				ch = '0';
			}
		}
		values2.push_back(flipped);
	}
}

string binaryToHexa(string line) {

	int ch1 = 0;
	int ch2 = 0;

	for (int i = 0; i < 4; i++) {
		if (line[i] == '1') {
			ch1 += (1 << (3 - i));  // 2^(3-i)
		}
	}

	for (int i = 4; i < 8; i++) {
		if (line[i] == '1') {
			ch2 += (1 << (7 - i));  // 2^(3-i)
		}
	}

	stringstream result;
	result << hex << uppercase << ch1 << ch2;
	return result.str();

}

void printResult(vector<string>& data) {

	printf("------------------------------------\n");
	for (int i = 0; i < data.size(); i++) {
		cout << data[i] << endl;
	}
	printf("------------------------------------\n");
}


void printResult(vector<string>& data, vector<string>& data1) {

	printf("------------------------------------\n");
	cout << "data\t\t" << "hexa\t" << "data\t" << "hexa" << endl;
	for (int i = 0; i < data.size(); i++) {
		cout << data[i] << "\t" << binaryToHexa(data[i]) << "\t" << data1[i] << "\t" << binaryToHexa(data1[i]) << endl;
	}
	printf("------------------------------------\n");
}

void allResult(vector<string>& data, vector<string>& data1, vector<string>& result) {
	cout << "전체 비트 확인" << endl;


	for (int i = 0; i < data.size(); i++) {
		//result = (int)data + (int)data1;
	}

}


int n = 6, k = 5, a[6] = { 1,2,3,4,5,6 };

void printVector(vector<int>& nums) {
	for (int num : nums) {
		cout << num + 1 << " ";
	}
	cout << '\n';
}

void combiWithFor() {
	for (int i = 0; i < n; i++) {
		for (int j = i + 1; j < n; j++) {
			for (int k = j + 1; k < n; k++) {
				cout << i << " " << j << " " << k << "\n";
			}
		}
	}
}
void combi(int start, vector<int>& b) {
	if (b.size() == k) {
		printVector(b);
		return;
	}

	for (int i = start + 1; i < n; i++) {

		b.push_back(i);
		combi(i, b);
		b.pop_back();
	}
	return;
}



int main() {
	//vector<int> a;
	//combi(-1, a);
	//printVector(a);
	//while (1) {
	//	string binary;
	//	cout << "input bin num\n";
	//	cin >> binary;

	//	int remainder = binary.length() % 4;
	//	if (remainder != 0) {
	//		binary = string(4 - remainder, '0') + binary;
	//	}


	//	// binary to hex 
	//	stringstream ss;
	//	for (size_t i = 0; i < binary.length(); i += 4) {
	//		string nibble = binary.substr(i, 4);
	//		int decimal = bitset<4>(nibble).to_ulong();
	//		ss << hex << uppercase << decimal;

	//	}
	//	cout << "hex : " << ss.str() << endl;
	//}


	cout << "Please Input Data" << endl;

	string BinaryData;
	vector<string> a;
	vector<string> b;
	inputBinaryDatas(a);
	makeAbnormalTestData(a, b);
	printResult(a, b);


}