from src.models import Team, Match, Player


TEAM_A = [
    Team('Cobreloa', 'Zorros del desierto', 12102, 'Calama'),
    Team('Cobresal', 'El Cobre', 11240, 'El Salvador'),
    Team('Huachipato', 'Huachipato-CAP Acero', 10050, 'Talcahuano'),
    Team('Colo Colo', 'Monumental', 43667, 'Macul'),
    Team('Universidad de Chile', 'No tienen :(', 0, 'Ñuñoa'),
    Team('Deportes Magallanes', 'Municipal Luis Navarro Avilés', 3500, 'Santiago'),
    Team('Unión Española', 'Santa Laura', 19887, 'Independencia'),
    Team('Audax Italiano', 'Bicentenario de La Florida', 12000, 'La Florida'),
    Team('Santiago Morning', 'Municipal de La Pintana', 5000, 'La pintana'),
    Team('San Luis de Quillota', 'Municipal Lucio Fariña Fernández', 7860, 'Quillota'),
]

TEAM_B = [
    Team('Universidad de Chile', 'No tienen :(', 0, 'Ñuñoa'),
    Team('Universidad Católica', 'San Carlos de Apoquindo', 16000, 'Las Condes'),
    Team('Unión Española', 'Santa Laura', 19887, 'Independencia'),
    Team('Audax Italiano', 'Bicentenario de La Florida', 12000, 'La Florida'),
    Team('Deportes Magallanes', 'Municipal Luis Navarro Avilés', 3500, 'Santiago'),
    Team('Santiago Morning', 'Municipal de La Pintana', 5000, 'La pintana'),
    Team('San Luis de Quillota', 'Municipal Lucio Fariña Fernández', 7860, 'Quillota'),
    Team('Deportes La Serena', 'La Portada', 18243, 'La Serena'),
    Team('Deportes Temuco', 'Germán Becker', 18413, 'Temuco'),
    Team('Deportes Puerto Montt', 'Chinquihue', 8000, 'Puerto Montt'),
]

TEAM_C = [
    Team('Everton', 'Sausalito', 22000, 'Viña del Mar'),
    Team('Santiago Wanderers', 'Elías Figueroa Brander', 18000, 'Valparaíso'),
    Team('Deportes Iquique', 'Cavancha', 10000, 'Iquique'),
    Team('Deportes Antofagasta', 'Calvo y Bascuñán', 21000, 'Antofagasta'),
    Team('Cobresal', 'El Cobre', 11240, 'El Salvador'),
    Team('Huachipato', 'Huachipato-CAP Acero', 10050, 'Talcahuano'),
    Team('Colo Colo', 'Monumental', 43667, 'Macul'),
    Team('Universidad de Chile', 'No tienen :(', 0, 'Ñuñoa'),
    Team('Deportes Magallanes', 'Municipal Luis Navarro Avilés', 3500, 'Santiago'),
    Team('Unión Española', 'Santa Laura', 19887, 'Independencia'),
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
    Team('', '', 21000, 'Antofagasta'),
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
    Team('', '', 21000, 'Antofagasta'),
]

MATCHES_A = [
    Match('played', '2-1'),
    Match('played', '1-1'),
    Match('played', '0-0'),
    Match('played', '3-1'),
    Match('played', '1-0'),
    Match('Not played', '--'),
    Match('Not played', '--'),
    Match('Not played', '--'),
    Match('Not played', '--'),
    Match('Not played', '--'),
]

MATCHES_B = [
    Match('played', '2-1'),
    Match('played', '3-2'),
    Match('played', '0-0'),
    Match('played', '3-4'), 
    Match('played', '6-0'),
    Match('Not played', '--'),
    Match('Not played', '--'),
    Match('Not played', '--'),
    Match('Not played', '--'),
    Match('Not played', '--'),
]

MATCHES_C  = [
    Match('played', '2-2'),
    Match('played', '3-1'),
    Match('played', '5-0'),
    Match('played', '5-6'),
    Match('played', '0-0'),
    Match('Not played', '--'),
    Match('Not played', '--'),
    Match('Not played', '--'),
    Match('Not played', '--'),
    Match('Not played', '--'),
]

WRONG_MATCHES = [
    Match('','1-1'),
    Match('played', ''),
    Match('','--')
]

WRONG_MATCHES_2 = [
    Match('','2-1'),
    Match('Not played',''),
    Match('played',''),
    Match('','--')
]

PLAYERS_A = [
    Player('Javier Perez', 28, 4,5),
    Player('Carlos Perez', 30, 3, 5),
    Player('Juan Perez', 25, 4, 5),
    Player('Pedro Perez', 27, 4, 5)
    ]



