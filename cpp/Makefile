all: compile

compile: main.out

# Rule to create main.out
main.out: *.cpp
	g++ -o main.out *.cpp -I ./

run: main.out
# @ Makes next output silent
	@./main.out