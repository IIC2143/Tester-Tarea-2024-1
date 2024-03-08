from src.models import Team, Match, Player


TEAMS_A = [
    Team('Cobreloa', 'Zorros del desierto', 12102, 'Calama'),
    Team('Cobresal', 'El Cobre', 11240, 'El Salvador'),
    Team('Huachipato', 'Huachipato-CAP Acero', 10050, 'Talcahuano'),
    Team('Colo Colo', 'Monumental', 43667, 'Macul'),
    Team('Universidad de Chile', 'No tienen :(', 0, 'Ñuñoa'),
    Team('Deportes Magallanes', 'Municipal Luis Navarro Avilés', 3500, 'Santiago'),
    Team('Unión Española', 'Santa Laura', 19887, 'Independencia'),
    Team('Audax Italiano', 'Bicentenario de La Florida', 12000, 'La Florida'),
    Team('Santiago Morning', 'Municipal de La Pintana', 5000, 'La pintana'),
    Team('San Luis de Quillota', 'Municipal Lucio Fariña Fernández', 7860, 'Quillota')
]

TEAMS_B = [
    Team('Universidad de Chile', 'No tienen :(', 0, 'Ñuñoa'),
    Team('Universidad Católica', 'San Carlos de Apoquindo', 16000, 'Las Condes'),
    Team('Unión Española', 'Santa Laura', 19887, 'Independencia'),
    Team('Audax Italiano', 'Bicentenario de La Florida', 12000, 'La Florida'),
    Team('Deportes Magallanes', 'Municipal Luis Navarro Avilés', 3500, 'Santiago'),
    Team('Santiago Morning', 'Municipal de La Pintana', 5000, 'La pintana'),
    Team('San Luis de Quillota', 'Municipal Lucio Fariña Fernández', 7860, 'Quillota'),
    Team('Deportes La Serena', 'La Portada', 18243, 'La Serena'),
    Team('Deportes Temuco', 'Germán Becker', 18413, 'Temuco'),
    Team('Deportes Puerto Montt', 'Chinquihue', 8000, 'Puerto Montt')
]

TEAMS_C = [
    Team('Everton', 'Sausalito', 22000, 'Viña del Mar'),
    Team('Santiago Wanderers', 'Elías Figueroa Brander', 18000, 'Valparaíso'),
    Team('Deportes Iquique', 'Cavancha', 10000, 'Iquique'),
    Team('Deportes Antofagasta', 'Calvo y Bascuñán', 21000, 'Antofagasta'),
    Team('Cobresal', 'El Cobre', 11240, 'El Salvador'),
    Team('Huachipato', 'Huachipato-CAP Acero', 10050, 'Talcahuano'),
    Team('Colo Colo', 'Monumental', 43667, 'Macul'),
    Team('Universidad de Chile', 'No tienen :(', 0, 'Ñuñoa'),
    Team('Deportes Magallanes', 'Municipal Luis Navarro Avilés', 3500, 'Santiago'),
    Team('Unión Española', 'Santa Laura', 19887, 'Independencia')
]


WRONG_TEAMS= [
    Team('Universidad de Chile', '', 0, 'Ñuñoa'),
    Team('', 'San Carlos de Apoquindo', 16000, 'Las Condes'),
    Team('', '', 0, 'Ñuñoa'),
    Team('Deportes La Serena', 'La Portada', 18243, ''),
    Team('Deportes Temuco', 'Germán Becker', 0, 'Temuco'),
    Team('Deportes Puerto Montt', '', 8000, 'Puerto Montt'),
    Team('Everton', 'Sausalito', 22000, ''),
    Team('', '', 18000, 'Valparaíso'),
    Team('', '', 10000, 'Iquique'),
    Team('', '', 21000, 'Antofagasta')
]

WRONG_TEAMS_2 = [
    Team('', '', 0, 'Ñuñoa'),
    Team('Catolica', '', 16000, 'Las Condes'),
    Team('', '', 0, ''),
    Team('Deportes La Serena', '', 18243, ''),
    Team('Deportes Temuco', 'Germán Becker', 0, ''),
    Team('Deportes Puerto Montt', '', 8000, ''),
    Team('Everton', 'Sausalito', 22000, ''),
    Team('', '', 18000, 'Valparaíso'),
    Team('', '', 10000, 'Iquique'),
    Team('', '', 21000, 'Antofagasta')
]

MATCHES_A = [
    Match(True, '2-1'),
    Match(True, '1-1'),
    Match(True, '0-0'),
    Match(True, '3-1'),
    Match(True, '1-0'),
    Match(False, '--'),
    Match(False, '--'),
    Match(False, '--'),
    Match(False, '--'),
    Match(False, '--')
]

MATCHES_B = [
    Match(True, '2-1'),
    Match(True, '3-2'),
    Match(True, '0-0'),
    Match(True, '3-4'), 
    Match(True, '6-0'),
    Match(False, '--'),
    Match(False, '--'),
    Match(False, '--'),
    Match(False, '--'),
    Match(False, '--')
]

MATCHES_C  = [
    Match(True, '2-2'),
    Match(True, '3-1'),
    Match(True, '5-0'),
    Match(True, '5-6'),
    Match(True, '0-0'),
    Match(False, '--'),
    Match(False, '--'),
    Match(False, '--'),
    Match(False, '--'),
    Match(False, '--')
]

WRONG_MATCHES = [
    Match('','1-1'),
    Match(True, ''),
    Match('','--')
]

WRONG_MATCHES_2 = [
    Match('','2-1'),
    Match(False,''),
    Match(True,''),
    Match('','--')
]

PLAYERS_A = [
    Player('Cristian Ruz', 10, 4,0),
    Player('Arturo Vidal', 0, 3, 5),
    Player('Felipe Loyola', 4, 1, 5),
    Player('Sebatian Saez', 2, 1, 0),
    Player('Ignacio Jeraldino',4,0,3),
    Player('Felipe Flores', 3, 2, 1)
    ]

PLAYERS_B = [
    Player('Joe Abrigo', 2, 2, 0),
    Player('Bryan Rabello', 0, 3, 5),
    Player('Felipe Fritz', 4, 1, 5),
    Player('Cristian Palacios', 2, 1, 0),
    Player('Felipe Flores',4,0,3),
    Player('Emiliano Vecchio', 3, 2, 1),
    Player('Patricio Rubio', 1, 0, 0)
]

PLAYERS_C = [
    Player('Gustavo Lanaro', 1, 0, 0),
    Player('Diego Valencia', 0, 0, 0),
    Player('Pablo Parra', 0, 0, 0),
    Player('Matias Rodriguez', 0, 2, 0),
    Player('Edson Puch', 2, 0, 2),
    Player('Felipe Fritz', 0, 0, 0),
    Player('Diego Sanchez', 0, 0, 0)
]

WRONG_PLAYERS = [
    Player('', 1, 0, 0)
    ]



