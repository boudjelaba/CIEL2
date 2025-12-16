CXX := g++
CXXFLAGS := -std=c++11 -Wall -Wextra -Iinclude
SRC := src/main.cpp src/Rectangle.cpp src/Carre.cpp
OBJ := $(SRC:.cpp=.o)
TARGET := prog1

all: $(TARGET)

$(TARGET): $(OBJ)
	$(CXX) $(CXXFLAGS) -o $@ $(OBJ)


%.o: %.cpp
	$(CXX) $(CXXFLAGS) -c $< -o $@

clean:
	rm -f $(OBJ) $(TARGET)

.PHONY: all clean

# /Users/kb/Desktop/POO_V2/partie1p && make -j