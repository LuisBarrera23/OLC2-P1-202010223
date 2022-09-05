from enum import Enum
from src.Abstract.Expresion import Expresion
from src.Abstract.RetornoType import RetornoType, TipoDato
from src.PatronSingleton.Singleton import Singleton
from src.Symbol.Error import Error

class TIPO_OPERACION(Enum):
    SUMA = 1,
    RESTA = 2,
    MULTIPLICACION = 3,
    DIVISION = 4,
    POTENCIA = 5,
    MODULO = 6,
    MAYOR = 7,
    MENOR = 8,
    MAYORIGUAL = 9,
    MENORIGUAL = 10,
    IGUALIGUAL = 11,
    DIFERENTE = 12,
    OR = 13,
    AND = 14,
    NOT = 15,

class Operacion(Expresion):

    def __init__(self,izquierda,tipo,derecha,unario,linea,columna):
        self.izquierda=izquierda
        self.tipo=tipo
        self.derecha=derecha
        self.unario=unario
        self.linea=linea
        self.columna=columna
        self.tipo2:TipoDato=TipoDato.ERROR
        

    def obtenerValor(self, entorno) -> RetornoType:
        s=Singleton.getInstance()
        E1=RetornoType()
        E2=RetornoType()
        RetornoUnario=RetornoType()

        if self.unario:
            RetornoUnario=self.izquierda.obtenerValor(entorno)
            if RetornoUnario.tipo==TipoDato.I64:
                return RetornoType(valor=int(RetornoUnario.valor*-1),tipo=RetornoUnario.tipo)
            elif RetornoUnario.tipo==TipoDato.F64:
                return RetornoType(valor=float(RetornoUnario.valor*-1),tipo=RetornoUnario.tipo)
            elif RetornoUnario.tipo==TipoDato.BOOL and self.tipo==TIPO_OPERACION.NOT:
                return RetornoType(valor=not RetornoUnario.valor,tipo=TipoDato.BOOL)

        else:
            E1=self.izquierda.obtenerValor(entorno)
            E2=self.derecha.obtenerValor(entorno)
            
            if self.tipo==TIPO_OPERACION.SUMA:
                if E1.tipo==TipoDato.F64 and E2.tipo==TipoDato.F64:
                    return RetornoType(valor=float(E1.valor+E2.valor),tipo=TipoDato.F64)
                elif E1.tipo==TipoDato.I64 and E2.tipo==TipoDato.I64:
                    return RetornoType(valor=int(E1.valor+E2.valor),tipo=TipoDato.I64)
                elif E1.tipo==TipoDato.I64 and E2.tipo==TipoDato.USIZE:
                    return RetornoType(valor=int(E1.valor+E2.valor),tipo=TipoDato.USIZE)
                elif E1.tipo==TipoDato.USIZE and E2.tipo==TipoDato.I64:
                    return RetornoType(valor=int(E1.valor+E2.valor),tipo=TipoDato.USIZE)
                elif E1.tipo==TipoDato.USIZE and E2.tipo==TipoDato.USIZE:
                    return RetornoType(valor=int(E1.valor+E2.valor),tipo=TipoDato.USIZE)
                elif E1.tipo==TipoDato.STRING and E2.tipo==TipoDato.STR:
                    return RetornoType(valor=str(E1.valor+E2.valor),tipo=TipoDato.STRING)
                elif E1.tipo==TipoDato.STR and E2.tipo==TipoDato.STRING:
                    return RetornoType(valor=str(E1.valor+E2.valor),tipo=TipoDato.STRING)

                else:
                    raise Exception(s.addError(Error("Tipo de suma no valida",self.linea,self.columna)))
            
            elif self.tipo==TIPO_OPERACION.RESTA:
                if E1.tipo==TipoDato.F64 and E2.tipo==TipoDato.F64:
                    return RetornoType(valor=float(E1.valor-E2.valor),tipo=TipoDato.F64)
                elif E1.tipo==TipoDato.I64 and E2.tipo==TipoDato.I64:
                    return RetornoType(valor=int(E1.valor-E2.valor),tipo=TipoDato.I64)
                elif E1.tipo==TipoDato.I64 and E2.tipo==TipoDato.USIZE:
                    return RetornoType(valor=int(E1.valor-E2.valor),tipo=TipoDato.USIZE)
                elif E1.tipo==TipoDato.USIZE and E2.tipo==TipoDato.I64:
                    return RetornoType(valor=int(E1.valor-E2.valor),tipo=TipoDato.USIZE)
                elif E1.tipo==TipoDato.USIZE and E2.tipo==TipoDato.USIZE:
                    return RetornoType(valor=int(E1.valor-E2.valor),tipo=TipoDato.USIZE)
                else:
                    raise Exception(s.addError(Error("Tipo de resta no valida",self.linea,self.columna)))
            
            elif self.tipo==TIPO_OPERACION.MULTIPLICACION:
                if E1.tipo==TipoDato.F64 and E2.tipo==TipoDato.F64:
                    return RetornoType(valor=float(E1.valor*E2.valor),tipo=TipoDato.F64)
                elif E1.tipo==TipoDato.I64 and E2.tipo==TipoDato.I64:
                    return RetornoType(valor=int(E1.valor*E2.valor),tipo=TipoDato.I64)
                else:
                    raise Exception(s.addError(Error("Tipo de multiplicacion no valida",self.linea,self.columna)))

            elif self.tipo==TIPO_OPERACION.DIVISION:
                if E1.tipo==TipoDato.F64 and E2.tipo==TipoDato.F64:
                    return RetornoType(valor=float(E1.valor/E2.valor),tipo=TipoDato.F64)
                elif E1.tipo==TipoDato.I64 and E2.tipo==TipoDato.I64:
                    return RetornoType(valor=int(E1.valor/E2.valor),tipo=TipoDato.I64)

                else:
                    raise Exception(s.addError(Error("Tipo de division no valida",self.linea,self.columna)))

            elif self.tipo==TIPO_OPERACION.POTENCIA:
                if E1.tipo==TipoDato.F64 and E2.tipo==TipoDato.F64 and self.tipo2==TipoDato.F64:
                    return RetornoType(valor=float(E1.valor**E2.valor),tipo=TipoDato.F64)
                elif E1.tipo==TipoDato.I64 and E2.tipo==TipoDato.I64 and self.tipo2==TipoDato.I64:
                    return RetornoType(valor=int(E1.valor**E2.valor),tipo=TipoDato.I64)

                else:
                    raise Exception(s.addError(Error("Tipo de potencia no valida",self.linea,self.columna)))
            
            elif self.tipo==TIPO_OPERACION.MODULO:
                if E1.tipo==TipoDato.F64 and E2.tipo==TipoDato.F64:
                    return RetornoType(valor=float(E1.valor%E2.valor),tipo=TipoDato.F64)
                elif E1.tipo==TipoDato.I64 and E2.tipo==TipoDato.I64:
                    return RetornoType(valor=int(E1.valor%E2.valor),tipo=TipoDato.I64)
                else:
                    raise Exception(s.addError(Error("Tipo de modulo no valida",self.linea,self.columna)))


#--------------------------------------------------------------------------------
#Operaciones Relacionales
            elif self.tipo==TIPO_OPERACION.MAYOR:
                return RetornoType(valor=E1.valor>E2.valor,tipo=TipoDato.BOOL)

            elif self.tipo==TIPO_OPERACION.MENOR:
                return RetornoType(valor=E1.valor<E2.valor,tipo=TipoDato.BOOL)

            elif self.tipo==TIPO_OPERACION.MAYORIGUAL:
                return RetornoType(valor=E1.valor>=E2.valor,tipo=TipoDato.BOOL)

            elif self.tipo==TIPO_OPERACION.MENORIGUAL:
                return RetornoType(valor=E1.valor<=E2.valor,tipo=TipoDato.BOOL)
            
            elif self.tipo==TIPO_OPERACION.IGUALIGUAL:
                return RetornoType(valor=E1.valor==E2.valor,tipo=TipoDato.BOOL)

            elif self.tipo==TIPO_OPERACION.DIFERENTE:
                return RetornoType(valor=E1.valor!=E2.valor,tipo=TipoDato.BOOL)

#--------------------------------------------------------------------------------
#Operaciones logicas

            elif self.tipo==TIPO_OPERACION.OR:
                if E1.tipo==TipoDato.BOOL and E2.tipo==TipoDato.BOOL:
                    return RetornoType(valor=E1.valor or E2.valor,tipo=TipoDato.BOOL)
                else:
                    raise Exception(s.addError(Error("Tipo de OR no valido",self.linea,self.columna)))

            elif self.tipo==TIPO_OPERACION.AND:
                if E1.tipo==TipoDato.BOOL and E2.tipo==TipoDato.BOOL:
                    return RetornoType(valor=E1.valor and E2.valor,tipo=TipoDato.BOOL)
                else:
                    raise Exception(s.addError(Error("Tipo de AND no valido",self.linea,self.columna)))