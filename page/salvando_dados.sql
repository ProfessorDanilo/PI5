CREATE TABLE IF NOT EXISTS dados (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    ano INTEGER NOT NULL,
    mes INTEGER NOT NULL,
    dia INTEGER NOT NULL,
    hora INTEGER NOT NULL,
    minuto INTEGER NOT NULL,
    umidade INTEGER NOT NULL,
    temperatura INTEGER NOT NULL,
    pressao INTEGER NOT NULL,
    CO INTEGER NOT NULL
);
