{\rtf1\ansi\ansicpg1252\cocoartf2513
\cocoatextscaling0\cocoaplatform0{\fonttbl\f0\fnil\fcharset0 Menlo-Regular;}
{\colortbl;\red255\green255\blue255;\red0\green0\blue0;\red255\green255\blue254;}
{\*\expandedcolortbl;;\cssrgb\c0\c0\c0;\cssrgb\c100000\c100000\c99608;}
\paperw11900\paperh16840\margl1440\margr1440\vieww22580\viewh8380\viewkind0
\deftab720
\pard\pardeftab720\sl420\partightenfactor0

\f0\fs28 \cf2 \cb3 \expnd0\expndtw0\kerning0
\outl0\strokewidth0 \strokec2 arr = list(map(int, input("Enter array: ").split()));\cb1 \
\cb3 key = int(input("Enter search key: "));\cb1 \
\
\cb3 def linearsearch(arr, key) :\cb1 \
\cb3   length = len(arr);\cb1 \
\cb3   for i in range(0, length):\cb1 \
\cb3     if(arr[i] == key):\cb1 \
\cb3       return i;\cb1 \
\cb3   return -1;\cb1 \
\
\cb3 search = linearsearch(arr, key);\cb1 \
\cb3 if (search == -1):\cb1 \
\cb3   print("Key doesnt exist in array");\cb1 \
\cb3 else:\cb1 \
\cb3   print("Key exists in index ", search);\cb1 \
\
}