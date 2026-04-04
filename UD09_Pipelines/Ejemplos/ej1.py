import rx 
import time
from rx import operators as ops, interval, repeat_value, timer


def ejemplo():
    cadenas = ["Pepe Garcia", "Maria Lopez", "Juan Perez"]
    source = rx.from_(cadenas)

    pipeline= source.pipe(
        ops.map(lambda s: s.replace(' ', '_')),
        ops.map(lambda s: s.lower())
    )

    pipeline.subscribe(
        on_next=lambda e: print(e),
        on_completed=lambda: print("Completado")
    )

def aux(x):
    print(x)

def ejemplo2():
    rx.of(1, 2, 3, 4, 5, 6, 7, 8, 9, 0).pipe(
        ops.filter(lambda x: x % 2 == 0),
        ops.do_action(aux),
        ops.skip(2)
    ).subscribe(
        on_next=lambda e: print(e),
        on_completed=lambda: print("Completado")
    )

def ejemplo3():
    interval(1).subscribe(print)
    time.sleep(6)


if __name__ == "__main__":
    ejemplo3()