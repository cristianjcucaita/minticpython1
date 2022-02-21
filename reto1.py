#Datos que coloca el usuario
salario_basico,horas_extras,bonificaciones=map(float,input().split())

#Ciclo infinito para seguir utilizando el programa desde cero.
if horas_extras > 0:
    valor_hora_normal = salario_basico / 176
    precio_hora_extra = (((valor_hora_normal * 25 / 100) + valor_hora_normal) * horas_extras)
else:
    precio_hora_extra = 0
if bonificaciones == 1:
    precio_bonificaciones = salario_basico * 6.5 / 100
else:
    precio_bonificaciones = 0
salario_devengado = salario_basico + precio_hora_extra + precio_bonificaciones

#Datos de deducciones a descontar
plan_obligatorio_salud = salario_devengado * 2.5 / 100
aporte_pension = salario_devengado * 2.5 / 100
caja_compensacion = salario_devengado * 4 / 100
salario_total = salario_devengado - plan_obligatorio_salud - aporte_pension - caja_compensacion
print(round(salario_devengado,1),round(salario_total,1))

# Tipos de Dato - en caso de ser necesario utilizar siglas:
# s_b : salario_basico
# h_e : horas_extras
# b_n : bonificaciones 
# v_h_n : valor_hora_normal
# p_h_e : precio_hora_extra
# p_b : precio_bonificaciones
# s_t : salario_devengado
# p_o_s : plan_obligatorio_salud
# a_a_p : aporte_pension
# c_d_c : caja_compensacion
# v_a_p_d_d : salario_total