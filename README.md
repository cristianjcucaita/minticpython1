# MinTic python reto 1
Es el primer reto finalizado por el programación de MinTic hecho el año 2021.

Problema del caso: Salario con parafiscales

Un empleado de una empresa de TV Cable desea conocer a cuánto dinero equivalen los descuentos de parafiscales exigidos por la ley en relación con los pagos 
que la empresa para la que trabaja le realizan mensualmente. Se ha firmado un contrato que le permite trabajar 48 horas semanales. Con el propósito de 
verificar el valor total de los descuentos han decidido construir un programa en Python que le permita verificar el valor de su salario antes y después de 
realizar los descuentos. 
Después de consultar sobre la normatividad y revisar con detalle su contrato laboral nota que debe tener en cuenta los siguientes aspectos:

- El valor de una hora de trabajo normal se obtiene dividiendo el salario base sobre 176.
- Las horas extras se liquidan con un recargo del 25% sobre el valor de una hora normal.
- Debido a buen desempeño de un empleado la empresa ocasionalmente otorga bonificaciones de 6.5% del salario base.
- El salario total antes de descuentos se calcula como la suma del salario base, más el valor de las horas extras, más las bonificaciones (si las hay).
- Se descontará 2.5% del salario total antes de descuentos para el plan obligatorio de salud.
- Se descontará 2.5% del salario total antes de descuentos para el aporte a pensión.
- Se descontará 4% del salario total antes de descuentos para caja de compensación.

Luego de considerar toda esta información, el empleado decide construir un programa que permita a cualquier empleado de la empresa verificar si los pagos son correctos.

Datos de ingreso:
El programa recibirá 3 parámetros:

- El salario base del empleado.
- La cantidad de horas extras se representa a través de un número entero positivo. En caso de no realizar horas extras durante el mes, se ingresará el valor 0.
- Si hubo bonificaciones se ingresará el valor 1, de lo contrario el valor 0.

Datos que debe mostrar:
El programa debe imprimir 2 valores:

- El valor a pagar al empleado luego de realizar los descuentos de ley. El resultado debe imprimirse con un número decimal.
- El salario total del empleado antes de descuentos. El resultado debe imprimirse con un número decimal.

Datos ejemplo de Solucion:

Entrada	        

1000000 0 0	    	  
2355255 2 1	    	  
1000000 5 0	    	  
1500000.25 3 1		  
0 0 0	                        
1 1 1	              

Esperado

1000000.0 910000.0 	    	  
2541801.9 2313039.7 	    	  
1035511.4 942315.3 	    	  
1629460.5 1482809.1 	    	  
0.0 0.0		    	  
1.1 1.0		    	  
