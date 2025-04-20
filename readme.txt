how to run c libs:(Vscode)

gcc filename -o name_of_file_to_save
./name_of_file_to_save

eg:
gcc main.c -o con
./con.exe

        or

gcc main.c
./a.exe


how to run lex:

flex filename.l
gcc lex.yy.c
./a.exe

how to run yacc:

win_bison -d filename.y
win_flex filename.l
gcc filename.tab.c lex.yy.c
./a.exe

or 

yacc -d filename.y
flex filename.l
gcc filename.tab.c lex.yy.c
./a.exe

