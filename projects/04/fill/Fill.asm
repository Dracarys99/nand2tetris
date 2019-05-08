// This file is part of www.nand2tetris.org
// and the book "The Elements of Computing Systems"
// by Nisan and Schocken, MIT Press.
// File name: projects/04/Fill.asm

// Runs an infinite loop that listens to the keyboard input.
// When a key is pressed (any key), the program blackens the screen,
// i.e. writes "black" in every pixel;
// the screen should remain fully black as long as the key is pressed. 
// When no key is pressed, the program clears the screen, i.e. writes
// "white" in every pixel;
// the screen should remain fully clear as long as no key is pressed.

// Put your code here.
@0
M = 0
(KEYLOOP)
    @KBD
    D = M
    @BLACK
    D;JNE
    @WHITE
    D;JEQ
    @KEYLOOP
    0;JMP
(BLACK)
    @0
    D = M
    @KEYLOOP
    D;JNE
    @SCREEN
    D = A
    @1
    M = D
    (BLOOP)
        @0
        D = !A
        @1
        A = M
        M = D
        @1
        D = M
        D = D + 1
        @1
        M = D
        @KBD
        A = A - D
        D = A
        @BLOOP
        D;JNE
        @0
        M = 1
        @KEYLOOP
        0;JMP
(WHITE)
    @0
    D = M
    @KEYLOOP
    D;JEQ
    @SCREEN
    D = A
    @1
    M = D
    (WLOOP)
        @0
        D = A
        @1
        A = M
        M = D
        @1
        D = M
        D = D + 1
        @1
        M = D
        @KBD
        A = A - D
        D = A
        @WLOOP
        D;JNE
        @0
        M = 0
        @KEYLOOP
        0;JMP
