def hora_to_minutos(hora: str):
    aux_hora = hora.split(':')
    return int(aux_hora[0]) * 60 + int(aux_hora[1])


def not_sleeping_hours(horas: tuple[int, int]):
    starts_sleeping = 360 <= horas[0] <= 1440 or 1800 <= horas[0] <= 2880 or 3240 <= horas[0] <= 4320
    ends_sleeping = 360 <= horas[1] <= 1440 or 1800 <= horas[1] <= 2880 or 3240 <= horas[1] <= 4320
    return starts_sleeping and ends_sleeping


def visitas(reuniones: list[str]):
    dias_to_minutos = {
        'sabado': 0,
        'domingo': 1440,
        'lunes': 2880,
    }

    finish_time = sorted([(dias_to_minutos[reu[0]] +
                          hora_to_minutos(reu[1]) + int(reu[2]), dias_to_minutos[reu[0]] +
                          hora_to_minutos(reu[1])) for reu in reuniones])
    scheduled = 0
    k = 0
    for i in range(0, len(finish_time)):
        if i == 0:
            if not_sleeping_hours(finish_time[i]):
                scheduled += 1
        elif not_sleeping_hours(finish_time[i]) and finish_time[i][1] >= finish_time[k][0]:
            scheduled += 1
            k = i
    return scheduled


C = int(input())

for i in range(C):
    F = int(input())
    reuniones = []
    for j in range(F):
        reuniones.append(input().split())
    print(visitas(reuniones))
