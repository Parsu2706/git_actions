from src.math_operation import add , sub 



def test_add(): 
    assert add(2 , 3) == 5 
    assert add( 1 , -1 ) == 0 
    assert add(2 , 0) == 0 

def test_sub(): 
    assert sub(-1 , 1 ) == 2 
    assert sub(5 , 1) == 4 
    assert sub(1 , 1 ) == 0 

    
     