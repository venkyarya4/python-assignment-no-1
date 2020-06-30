{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "#Python Assignment no 1"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 1,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Hai How Are You??\n"
     ]
    }
   ],
   "source": [
    "#1.Simple Message: Store a message in a variable, and then print that message.\n",
    "mes='Hai How Are You??'\n",
    "print(mes)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 3,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Hello\n",
      "Hai\n"
     ]
    }
   ],
   "source": [
    "#2.Store a message in a variable and print that message. Then change the value of your variable to a new message and print the new message.\n",
    "mes1='Hello'\n",
    "print(mes1)\n",
    "mes2='Hai'\n",
    "print(mes2)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 115,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\"\\Hello Venky,would you like to learn some python today?\"\n"
     ]
    }
   ],
   "source": [
    "#3.Store a person’s name in a variable and print a message to that person. Your message should be simple, such as, “Hello Eric, would you like to learn some Python today?”\n",
    "name='Venky'\n",
    "print(f'\\\"Hello {name},would you like to learn some python today?\\\"')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 114,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\"Eleanor Roosevelt once said,\"The future belongs to those who believe in the beauty of thier dreams.\"\n"
     ]
    }
   ],
   "source": [
    "4.#Find a quote from a famous person you admire. Print the quote and the name of its author. Your output should look something like the following, including the quotation marks: \n",
    "    #Albert Einstein once said, “A person who never made a mistake never tried anything new.\"\n",
    "#The future belongs to those who believe in the beauty of thier dreams by  Eleanor Roosevelt \n",
    "print(\"\\\"Eleanor Roosevelt once said,\\\"The future belongs to those who believe in the beauty of thier dreams.\\\"\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 112,
   "metadata": {},
   "outputs": [],
   "source": [
    "#Repeat Exercise 4, but this time store the famous person’s name in a variable called famous_person. Then compose your message and store it in a new variable called message.Print your message."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 74,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Addition of two numbers is 8\n",
      "Subtraction of two numbers is 8\n",
      "Multiplication of two numbers is 8\n",
      "division of two numbers is 8\n"
     ]
    }
   ],
   "source": [
    "#Write addition, subtraction, multiplication, and division operations that each result in the number 8.Be sure to enclose your operations in print statements to see the results.You should create four lines that look like this:print (5 + 3)Your output should simply be four lines with the number 8 appearing once on each line.\n",
    "def add(a,b):\n",
    "  sum=a+b\n",
    "  print('Addition of two numbers is',sum)\n",
    "add(5,3)\n",
    "def sub(a,b):\n",
    "   subtract=a-b\n",
    "   print('Subtraction of two numbers is',subtract)\n",
    "sub(16,8)\n",
    "def multi(a,b):\n",
    "  multiply=a*b\n",
    "  print('Multiplication of two numbers is',multiply)\n",
    "multi(4,2)\n",
    "def div(a,b):\n",
    "  division=a//b\n",
    "  print('division of two numbers is',division)\n",
    "div(32,4)\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "#Store your favourite number in a variable.Then, using that variable, create a message that reveals your favourite number.Print that message"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 85,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Greetings of the day!\n"
     ]
    }
   ],
   "source": [
    "fav_num=4\n",
    "def mes(fav_num):\n",
    "     if fav_num==4:\n",
    "        print('Greetings of the day!')\n",
    "mes(4)\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "Choose two of the programs you’ve written and add at least one comment to each.If you don’t have anything specific to write because your programs are too simple at this point, just add your name and the current date at the top of each program file.Then write one sentence describing what the program does"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "#program no-1\n",
    "#Name:Venkatesh D.S\n",
    "#Date:6/25/2020\n",
    "#This program does the arithmetic operations such as addition,subtraction,multiplication,division by using functions.\n",
    "def add(a,b):\n",
    "  sum=a+b\n",
    "  print('Addition of two numbers is',sum)\n",
    "add(5,3)\n",
    "def sub(a,b):\n",
    "   subtract=a-b\n",
    "   print('Subtraction of two numbers is',subtract)\n",
    "sub(16,8)\n",
    "def multi(a,b):\n",
    "  multiply=a*b\n",
    "  print('Multiplication of two numbers is',multiply)\n",
    "multi(4,2)\n",
    "def div(a,b):\n",
    "  division=a//b\n",
    "  print('division of two numbers is',division)\n",
    "div(32,4\n",
    "\n",
    "#program no-2\n",
    "#Name:Venkatesh D.S\n",
    "#Date:6/25/2020\n",
    "#This program stores the favourite number in some variable if we enter that favourite number we get desired output to that number\n",
    "\n",
    "fav_num=4\n",
    "def mes(fav_num):\n",
    "     if fav_num==4:\n",
    "        print('Greetings of the day!')\n",
    "mes(4)\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "#9 Store the names of a few of your friends in a list called names.Print each person’s name by accessing each element in the list, one at a time."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 86,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Venky\n",
      "Ram\n",
      "Raj\n",
      "virat\n"
     ]
    }
   ],
   "source": [
    "names=['Venky','Ram','Raj','virat']\n",
    "for i in names:\n",
    "    print(i)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "#Start with the list you used in Exercise 9, but instead of just printing each person’s name, print a message to them. The text of each message should be the same, but each message should be personalized with the person’s name."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 90,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Hi Venky!\n",
      "Hi Ram!\n",
      "Hi Raj!\n",
      "Hi virat!\n"
     ]
    }
   ],
   "source": [
    "names=['Venky','Ram','Raj','virat']\n",
    "def message(names):\n",
    " for i in names:\n",
    "        if i==names[0]:\n",
    "            print('Hi Venky!')\n",
    "        elif i==names[1]:\n",
    "            print('Hi Ram!')\n",
    "        elif i==names[2]:\n",
    "             print('Hi Raj!')\n",
    "        elif i==names[3]:\n",
    "             print('Hi virat!')\n",
    "        else:\n",
    "             print('Name not in list!')\n",
    "message(names)\n",
    "                          "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "#11 Think of your favourite mode of transportation, such as a motorcycle or a car, and make a list that stores several examples.Use your list to print a series of statements about these items, such as “I would like to own a Honda motorcycle.”Python Basics-Assignment"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 97,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "I like Bike riding\n",
      "I like Audi car\n",
      "moring cycle ride ia awesome!\n",
      "Flying makes me feel special\n"
     ]
    }
   ],
   "source": [
    "motor_cycle=['Bike','Car','Cycle','flight']\n",
    "def motor(motor_cycle):\n",
    "    for i in motor_cycle:\n",
    "        if i == motor_cycle[0]:\n",
    "            print('I like Bike riding')\n",
    "        elif i== motor_cycle[1]:\n",
    "            print('I like Audi car')\n",
    "        elif i==motor_cycle[2]:\n",
    "             print('moring cycle ride ia awesome!')\n",
    "        elif i==motor_cycle[3]:\n",
    "            print('Flying makes me feel special')\n",
    "        else:\n",
    "            print('required motor cycle not in list')\n",
    "motor(motor_cycle)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.7.4"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 2
}
