class Logica:
    """
    Clase con métodos para realizar operaciones de lógica booleana y algoritmos.
    """
    
    def AND(self, a, b):
        """
        Implementa la operación lógica AND.
        
        Args:
            a (bool): Primer valor booleano
            b (bool): Segundo valor booleano
            
        Returns:
            bool: Resultado de a AND b
        """
        return a and b
    
    def OR(self, a, b):
        """
        Implementa la operación lógica OR.
        
        Args:
            a (bool): Primer valor booleano
            b (bool): Segundo valor booleano
            
        Returns:
            bool: Resultado de a OR b
        """
        return a or b
    
    def NOT(self, a):
        """
        Implementa la operación lógica NOT.
        
        Args:
            a (bool): Valor booleano
            
        Returns:
            bool: Resultado de NOT a
        """
        return not a
    
    def XOR(self, a, b):
        """
        Implementa la operación lógica XOR (OR exclusivo).
        
        Args:
            a (bool): Primer valor booleano
            b (bool): Segundo valor booleano
            
        Returns:
            bool: Resultado de a XOR b
        """
        return a!=b
    
    def NAND(self, a, b):
        """
        Implementa la operación lógica NAND (NOT AND).
        
        Args:
            a (bool): Primer valor booleano
            b (bool): Segundo valor booleano
            
        Returns:
            bool: Resultado de a NAND b
        """
        return not ( a and b)
    
    def NOR(self, a, b):
        """
        Implementa la operación lógica NOR (NOT OR).
        
        Args:
            a (bool): Primer valor booleano
            b (bool): Segundo valor booleano
            
        Returns:
            bool: Resultado de a NOR b
        """
        return not ( a or b)
    
    def XNOR(self, a, b):
        """
        Implementa la operación lógica XNOR (NOT XOR).
        
        Args:
            a (bool): Primer valor booleano
            b (bool): Segundo valor booleano
            
        Returns:
            bool: Resultado de a XNOR b
        """
        return a==b
    
    def implicacion(self, a, b):
        """
        Implementa la operación lógica de implicación (a -> b).
        
        Args:
            a (bool): Primer valor booleano (antecedente)
            b (bool): Segundo valor booleano (consecuente)
            
        Returns:
            bool: Resultado de la implicación
        """
        return (not a) or b
    
    def bi_implicacion(self, a, b):
        """
        Implementa la operación lógica de bi-implicación (a <-> b).
        
        Args:
            a (bool): Primer valor booleano
            b (bool): Segundo valor booleano
            
        Returns:
            bool: Resultado de la bi-implicación
        """
        return a==b
    
