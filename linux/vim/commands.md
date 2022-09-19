# Concepts
operator + (multiplier) * movement
### examples
```
d2d delete 2 lines
3w move forward 3 words
d3w delete the next 3 words
```

## Basic
k => up  
j => down  
h => left  
l => right  

## By words
w => jump to next word (beggining of next word) 
e => end of the word
b => hop backwards by a word  

## Copy paste
y => yank (COPY)  
yy => COPY a line  
p => paste a copied line one line below (and clear the register)  
P => paste a copied line one line above (and clear the register)  
d + movement => CUT (and save in the register) 
D + movement => CUT the rest of the line
dd => delete a line (and save in the register)  

## Select
V => highlight a line  
v => start selection from current point  

## Insert mode
i => insert mode where the cursor is  
I => insert mode from the beggining of the line  
a => insert mode one character to the right  
A => insert mode at the end of the line  
o => new line bellow and into insert mode  
O => new line above and into insert mode

### delete & insert
c => delete and go into insert mode (example cw: delete word and go into insert mode)
C => delete from current position to the end and go insert mode
s => delete (number) characters and go into insert mode
S => delete (number) lines and go into insert mode (properly indented)

## Find
/ => regex mode  
n => next occurrence  
N => previous occurrence  
\* => next occurence of the word you are at  
\# => previous occurence of the word you are at  

### Find in line
f+<character> => jump  on to the first occurence of that character  (F same but backwards)
t+<character> => jump  before the first occurence of that character (T same but backwards)
; => next occurence of that find
, => previous occurrence of that find
  
# Others
u => undo last command  
esc or ctrl+c or ctrl+[ => leave insert mode  
:w => save file  

# Combos
## delete inside parenthesis
If I have this line
`def myfunction(parameterA: str = "default"):`
  
And I want to remove all that is inside the parenthesis
```
> f( => to jump to the parenthesis
> ct) => to delete up to the closing parenthesis
```

