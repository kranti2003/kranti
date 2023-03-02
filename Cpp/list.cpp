#include "list.h" 

int main()
{
	std::list<std::string> ll;
	ll.push_back("Kranthi");
	ll.push_back("Kumar");
	ll.push_back("Reddy");

	std::list<std::string>::iterator iter = ll.begin();

	
	for (;iter != ll.end(); ++iter)
	{
		std::string str = *iter;
		std::cout <<str.c_str() << " "; 

	}
	std::cout<< std::endl ;
	return 0;
}
