from tkinter import *
from numpy import *

# Returns a m x n matrix with all elements = 0

def emptybox ( m , n ) :

    a = []

    for i in range ( 0 , m ) :

        x = []

        for j in range ( 0 , n ) :

            x += [ 0 ]

        a += [ x ]

    return a



# Returns a deep copy of the matrix

def copy ( A ) :

    a = []

    for i in range ( 0 , len ( A ) ) :

        x = []

        for j in range ( 0 , len ( A[0] ) ) :

            x += [ A [ i ] [ j ] ]

        a += [ x ]

    return a



# Returns the transpose of the matrix

def transpose ( A ) :

    if len ( A ) == 0 :

        return A

    a = emptybox ( len( A [ 0 ] ) , len( A ) )

    for i in range ( 0 , len ( A ) ) :

        for j in range ( 0 , len ( A [ 0 ] ) ) :

            a [ j ] [ i ] = A [ i ] [ j ]

    return a



# Returns a matrix with ith row and jth column removed

def trim ( A , icut , jcut ) :

    if len ( A ) == 0 :

        return A
    
    a = []

    for i in range ( 0 , len ( A ) ) :

        if i == icut :

            continue

        x = []

        for j in range ( 0 , len ( A [ 0 ] ) ) :

            if j == jcut :

                continue

            x += [ A [ i ] [ j ] ]

        a += [ x ]

    return a



# Returns the determinant of the matrix or 'x' if it is not a square matrix

def determinant ( A ) :

    if len ( A ) == 0 :

        return 0

    if len ( A ) != len ( A [ 0 ] ) :

        return 'x'

    if len ( A ) == 1 and len ( A [ 0 ] ) == 1 :

        return A [ 0 ] [ 0 ]

    Determinant = 0

    for j in range ( len ( A [ 0 ] ) ) :

        Determinant += ( 1 if j%2 == 0 else -1 ) * A[0][j] * determinant ( trim ( A , 0 , j ) )

    return Determinant



# Returns of the minor matrix of the given matrix

def minor ( A ) :

    a = emptybox ( len( A [ 0 ] ) , len( A ) )

    for i in range ( 0 , len ( A ) ) :

        for j in range ( 0 , len ( A [ 0 ] ) ) :
 
            a [ i ] [ j ] = determinant ( trim ( A , i , j ) )

    return a



# Returns of the cofactor matrix of the given matrix

def cofactor ( A ) :

    a = emptybox ( len( A [ 0 ] ) , len( A ) )

    b = minor ( A )

    for i in range ( 0 , len ( A ) ) :

        for j in range ( 0 , len ( A [ 0 ] ) ) :
 
            a [ i ] [ j ] = ( 1 if ( i + j ) % 2 == 0 else -1 ) * ( b [ i ] [ j ] )

    return a



# Returns of the adjoint matrix of the given matrix

def adjoint ( A ) :

    a = cofactor ( A )

    a = transpose ( a )

    return a
    


# Returns of the adjoint matrix of the given matrix

def inverse ( A ) :

    Determinant = determinant ( A )

    if Determinant == 0 :

        return 'X'

    a = adjoint ( A )

    for i in range ( 0 , len ( A ) ) :

        for j in range ( 0 , len ( A [ 0 ] ) ) :

            if a [ i ] [ j ] % Determinant == 0 :

                a [ i ] [ j ] = a [ i ] [ j ] // Determinant

            else :

                a [ i ] [ j ] = a [ i ] [ j ] / Determinant
    
    return a



# Returns the product of the two given matrices

def multiply ( A , B ) :

    if len ( A ) == 0 or len ( B ) == 0 :

        return []

    if len ( A [ 0 ] ) != len ( B ) :

        return 'X'

    a = emptybox ( len ( A ) , len ( B [ 0 ] ) )

    for j in range ( 0 , len ( B [ 0 ] ) ) :

        for i in range ( 0 , len ( A ) ) :

            for h in range ( 0 , len ( A [ 0 ] ) ) :

                a [ i ] [ j ] += A [ i ] [ h ] * B [ h ] [ j ]

    return a



# Returns the sum of the two given matrices

def add ( A , B ) :

    if len ( A ) == 0 or len ( B ) == 0 :

        return []

    if len ( A ) != len ( B ) or len ( A [ 0 ] ) != len ( B [ 0 ] ) :

        return 'X'

    a = emptybox ( len ( A ) , len ( A [ 0 ] ) )

    for i in range ( 0 , len ( A ) ) :

        for j in range ( 0 , len ( A [ 0 ] ) ) :

            a [ i ] [ j ] = A [ i ] [ j ] + B [ i ] [ j ]
         
    return a



# Returns the difference of the two given matrices

def subtract ( A , B ) :

    if len ( A ) == 0 or len ( B ) == 0 :

        return []

    if len ( A ) != len ( B ) or len ( A [ 0 ] ) != len ( B [ 0 ] ) :

        return 'X'

    a = emptybox ( len ( A ) , len ( A [ 0 ] ) )

    for i in range ( 0 , len ( A ) ) :

        for j in range ( 0 , len ( A [ 0 ] ) ) :

            a [ i ] [ j ] = A [ i ] [ j ] - B [ i ] [ j ]
         
    return a

app = Tk()
app.title("Circuit Solver")
app.geometry("1000x800")
app.resizable(False, False)
app.grid_columnconfigure(0, weight=1)
app.grid_columnconfigure(7, weight=1)



      
def input():

    def solve():
        
        n=node_entry.get()
        e=element_entry.get()
        n=int(n)
        e=int(e)
        result=Frame(app, height=800, width=1000).grid(row=0, column=0, columnspan=8, rowspan=e+2)
        
        Ie = emptybox ( e , 1 )

        Ve = emptybox ( e , 1 )

        Ise = emptybox ( e , 1 )

        for z in range ( e ) :

            Ise [ z ] [ 0 ] = float ( data [ z ] [ 4 ] .get() )


        Vse = emptybox ( e , 1 )

        for z in range ( e ) :

            Vse [ z ] [ 0 ] = float ( data [ z ] [ 3 ] .get() )
        

        Ge = emptybox ( e , e )

        for z in range ( e ) :

            Ge [ z ] [ z ] = 1 / float( data [ z ] [ 2 ] .get() )


        A = emptybox ( n , e )

        for z in range ( e ) :

            A [ int (data [ z ] [ 0 ] .get() ) - 1 ] [ z ] = 1

            A [ int (data [ z ] [ 1 ] .get() ) - 1 ] [ z ] = -1

        A = A[:-1]


        Yn = multiply ( multiply ( A , Ge ) , transpose ( A ) )

        Isn = subtract ( multiply ( multiply ( A , Ge ) , Vse ) , multiply ( A , Ise) ) 

        Vn = multiply ( inverse ( Yn ) , Isn )

        Ve = multiply ( transpose ( A ) , Vn )

        Ie = subtract ( add ( multiply ( Ge , Ve ) , Ise ) , multiply ( Ge , Vse ) )

        
        for x in range(e):
            element=Label(result, text="Element "+str(x+1), font=("Arial", 16))
            element.grid(row=x+1,column=1)
            ielem=Label(result, text=round(Ie[x][0],14), font=("Arial", 16))
            ielem.grid(row=x+1, column=2)
            velem=Label(result, text=round(Ve[x][0],14), font=("Arial", 16))
            velem.grid(row=x+1, column=4)
        
        ab=Label(result, text="Ie: Element\nCurrent", font=("Arial", 20))
        ab.grid(row=0,column=2)

        cd=Label(result, text="Ve: Element\nVoltage", font=("Arial", 20))
        cd.grid(row=0,column=4)

    n=node_entry.get()
    e=element_entry.get()
    n=int(n)
    e=int(e)

    data_input=Frame(app, height=800, width=1000).grid(row=0, column=0, sticky=NS, columnspan=8, rowspan=e+2)
    
    dataarr = emptybox(e,5)

    sn=Label(data_input, text="START\nNODE", font=("Arial", 20))
    sn.grid(row=1,column=1)

    sn=Label(data_input, text="END\nNODE", font=("Arial", 20))
    sn.grid(row=1,column=2)

    sn=Label(data_input, text="RESISTOR", font=("Arial", 20))
    sn.grid(row=1,column=3)

    sn=Label(data_input, text="VOLTAGE\nSOURCE", font=("Arial", 20))
    sn.grid(row=1,column=4)
    
    sn=Label(data_input, text="CURRENT\nSOURCE", font=("Arial", 20))
    sn.grid(row=1,column=5)

    for x in range(e):
        ele=Label(data_input, text="Element "+str(x+1), font=("Arial", 25))
        ele.grid(row=x+2,column=0)
        space=Label(data_input, text=" ")
        space.grid(column=7, sticky=EW)
        for y in range(5):
            dataarr[x][y] = Entry(data_input, font=('Arial 10'))
            dataarr[x][y].grid(row=x+2, column=y+1, ipadx=10, ipady=20)

    data = dataarr

    calculate=Button(data_input, text="SOLVE CIRCUIT",font=("Arial", 15), height=5, command=solve)
    calculate.grid(row=0, column=2, columnspan=2, sticky=EW)

    
first=Frame(app, height=800, width=1000)
first.grid(row=0, column=0, sticky=NS, columnspan=8, rowspan=4)

rowzero=Label(first, text=" ", font=("Arial", 128))
rowzero.grid(row=0)

node_label=Label(first, text='Enter Number of Nodes', font=("Arial", 20))
node_entry = Entry(first)
node_entry.grid(row=1, column=2,padx=5, ipadx=10, ipady=20)
node_label.grid(row=1, column=1,padx=5)

element_label=Label(first, text='Enter Number of Elements', font=("Arial", 20))
element_entry = Entry(first)
element_entry.grid(row=2, column=2,padx=5, ipadx=10, ipady=20)
element_label.grid(row=2, column=1,padx=5)


input_button=Button(
    first,
    text="INPUT DATA", 
    padx=100, 
    pady=5,
    command=input,
    height=5,
    font=("Arial", 15)
    ).grid(row=3,column=1, columnspan=2)


app.mainloop()