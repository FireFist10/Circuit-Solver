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



print("Enter Number of Nodes")

n = int ( input( ) )

print("Enter Number of Elements")

e = int ( input( ) )

dataarr = emptybox(e,5)

print("\nOrder of data entry: start node, end node, resistance, voltage source, current source separated by spaces")
print("Enter data for:\n")

for x in range(e):

    print ( "Element" , x+1 , ":" )

    tempvar = list ( map ( float , input().split() ) )

    tempvar [ 0 ] = int ( tempvar [ 0 ] )

    tempvar [ 1 ] = int ( tempvar [ 1 ] )

    dataarr[x] = tempvar

data = dataarr

Ie = emptybox ( e , 1 )

Ve = emptybox ( e , 1 )

Ise = emptybox ( e , 1 )

for z in range ( e ) :

    Ise [ z ] [ 0 ] = float ( data [ z ] [ 4 ])


Vse = emptybox ( e , 1 )

for z in range ( e ) :

    Vse [ z ] [ 0 ] = float ( data [ z ] [ 3 ]  )


Ge = emptybox ( e , e )

for z in range ( e ) :

    Ge [ z ] [ z ] = 1 / float( data [ z ] [ 2 ]  )


A = emptybox ( n , e )

for z in range ( e ) :

    A [ int (data [ z ] [ 0 ]  ) - 1 ] [ z ] = 1

    A [ int (data [ z ] [ 1 ]  ) - 1 ] [ z ] = -1

A = A[:-1]


Yn = multiply ( multiply ( A , Ge ) , transpose ( A ) )

Isn = subtract ( multiply ( multiply ( A , Ge ) , Vse ) , multiply ( A , Ise) ) 

Vn = multiply ( inverse ( Yn ) , Isn )

Ve = multiply ( transpose ( A ) , Vn )

Ie = subtract ( add ( multiply ( Ge , Ve ) , Ise ) , multiply ( Ge , Vse ) )


for x in range(e):
    print("\nElement " , x+1 , " : Ie = " , round(Ie[x][0],14) , "A || Ve = " , round(Ve[x][0],14) , "V" )