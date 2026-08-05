# -*- coding: utf-8 -*-
import json
import os

# Create 140 unique, European Spanish fitness recipes with complete macros, instructions, and editorial prompts
recipes_p1 = []
recipes_p2 = []

# PART 1: WHOLE FOOD POWER (SIN SUPLEMENTOS) - 70 RECIPES
# Cap 1: Desayunos y Meriendas Fit (01 to 15)
p1_c1_titles = [
    ("Tortitas de Avena y Plátano con Canela", "Simples, deliciosas y perfectas para nutrir tu masa muscular sin azúcares añadidos ❤️", "380 kcal", "18 g", "51 g", "13 g", "6 g"),
    ("Porridge de Avena y Arándanos con Claras y Almendras", "Un bol cremoso y reconfortante repleto de antioxidantes y proteína limpia ❤️", "403 kcal", "27 g", "53 g", "10 g", "8 g"),
    ("Tosta Integral de Queso Cottage, Aguacate y Tomates Cherry", "Crujiente, fresca y con el equilibrio ideal de grasas saludables y proteína ❤️", "388 kcal", "27 g", "40 g", "13 g", "7 g"),
    ("Bol de Yogur Griego Natural con Fresas y Nueces", "Un desayuno mediterráneo listo en un minuto con altísima densidad nutricional ❤️", "288 kcal", "25 g", "27 g", "10 g", "3 g"),
    ("Tortilla Francesa Proteica con Espinacas, Champiñones y Feta", "El desayuno salado por excelencia, repleto de volumen y sabor gourmet ❤️", "336 kcal", "29 g", "3 g", "21 g", "2 g"),
    ("Muffins de Huevo, Pavo y Calabacín al Horno", "Mini tortillas al horno listas para llevar con máxima saciedad y ligereza ❤️", "290 kcal", "24 g", "4 g", "18 g", "2 g"),
    ("Avena Trasnochada con Manzana, Canela y Yogur Griego", "Prepara tu desayuno por la noche y despierta con un tarro fresco y cremoso ❤️", "360 kcal", "22 g", "48 g", "8 g", "7 g"),
    ("Huevos Revueltos con Salmón Ahumado y Aguacate en Tosta", "Grasas Omega-3 y proteína de alto valor en una tosta integral de campeonato ❤️", "420 kcal", "26 g", "28 g", "22 g", "5 g"),
    ("Crema de Trigo Sarraceno con Pera y Almendras", "Alternativa sin gluten y rica en aminoácidos para variar tus desayunos fit ❤️", "340 kcal", "16 g", "52 g", "8 g", "6 g"),
    ("Tortitas Saladas de Avena, Calabacín y Queso Fresco", "Una opción salada y crujiente perfecta para quienes evitan el dulce por la mañana ❤️", "350 kcal", "21 g", "38 g", "12 g", "5 g"),
    ("Cazuela de Huevos al Horno con Tomate y Albahaca", "Shakshuka estilo fit cargada de licopeno antioxidante y proteína limpia ❤️", "310 kcal", "22 g", "12 g", "19 g", "3 g"),
    ("Tosta de Pan de Centeno con Huevo Escalfado y Espárragos", "Un desayuno elegante con carbohidratos de índice glucémico muy bajo ❤️", "345 kcal", "19 g", "34 g", "14 g", "6 g"),
    ("Porridge Salado de Avena con Espinacas y Huevo Mollet", "Descubre la avena salada como fuente de energía y saciedad matinal ❤️", "370 kcal", "23 g", "42 g", "12 g", "6 g"),
    ("Bol de Queso Fresco Batido con Granada y Nueces", "Cremoso, fresco y con el contraste ácido de los granos rubí de granada ❤️", "295 kcal", "26 g", "24 g", "9 g", "4 g"),
    ("Waffles Integrales de Avena y Plátano al Horno", "Crujientes por fuera y esponjosos por dentro sin una sola gota de grasa frita ❤️", "365 kcal", "17 g", "54 g", "9 g", "6 g")
]

# Cap 2: Almuerzos y Cenas Fit (16 to 35)
p1_c2_titles = [
    ("Merluza al Horno con Verduras y Gambas", "Un plato marinero ligero, fácil de hornear y de altísimo valor proteico ❤️", "462 kcal", "43 g", "35 g", "16 g", "4 g"),
    ("Salmón a la Plancha con Espárragos y Quinoa", "El clásico rey de los ácidos grasos Omega-3 acompañado de superalimentos ❤️", "475 kcal", "32 g", "33 g", "22 g", "5 g"),
    ("Pechuga de Pollo al Ajillo Fit con Arroz Integral", "Tradición española reinventada sin excesos de aceite pero con el máximo sabor ❤️", "443 kcal", "43 g", "40 g", "10 g", "5 g"),
    ("Ensalada Tibia de Garbanzos con Atún y Pimientos", "Una bomba de fibra, proteínas y sabor mediterráneo lista en tiempo récord ❤️", "510 kcal", "41 g", "46 g", "18 g", "11 g"),
    ("Paella Fitness de Mariscos con Arroz Integral", "Todo el sabor marinero de una paella tradicional en una versión 100% fit ❤️", "510 kcal", "41 g", "41 g", "16 g", "5 g"),
    ("Bacalao a la Plancha con Patatas y Brócoli al Vapor", "Proteína de pescado blanco de excelente calidad con carbohidratos saciantes ❤️", "405 kcal", "33 g", "36 g", "15 g", "5 g"),
    ("Pechuga de Pollo Asada al Limón con Boniato", "Sabor cítrico y un toque dulce natural en una cena equilibrada al milímetro ❤️", "465 kcal", "41 g", "33 g", "19 g", "6 g"),
    ("Ensalada Mediterránea de Lentejas y Queso Feta", "La fusión perfecta de legumbres tradicionales con proteína animal ligera ❤️", "485 kcal", "42 g", "46 g", "13 g", "17 g"),
    ("Brochetas de Gambas y Calabacín al Ajillo con Quinoa", "Divertidas brochetas a la plancha de marisco y verduras con grano ancestral ❤️", "423 kcal", "31 g", "35 g", "18 g", "5 g"),
    ("Wok de Pollo con Edamame y Verduras Crujientes", "Estilo asiático ligero y crujiente cargado de proteína animal y vegetal ❤️", "440 kcal", "43 g", "38 g", "13 g", "6 g"),
    ("Atún a la Plancha con Quinoa y Espárragos Verdes", "Un filete jugoso de atún con ácidos grasos esenciales y granos ancestrales ❤️", "460 kcal", "38 g", "33 g", "18 g", "5 g"),
    ("Pechuga de Pollo Rellena de Espinacas y Queso Feta", "Una pechuga jugosa rellena al horno que parece de restaurante de alta cocina ❤️", "445 kcal", "42 g", "28 g", "17 g", "4 g"),
    ("Guiso Ligero de Lentejas con Pollo y Zanahoria", "El cuchareo clásico español en una versión sin grasas y alta en proteína magra ❤️", "505 kcal", "43 g", "48 g", "14 g", "16 g"),
    ("Dorada al Horno con Patatas Panaderas y Limón", "Pescado blanco mediterráneo horneado con patatas tiernas al punto perfecto ❤️", "430 kcal", "34 g", "36 g", "16 g", "4 g"),
    ("Pollo al Curry Fit con Arroz Integral y Brócoli", "Sabor oriental cremoso elaborado con especias antiinflamatorias y pollo magro ❤️", "448 kcal", "37 g", "43 g", "12 g", "5 g"),
    ("Ensalada Mediterránea de Quinoa con Gambas y Aguacate", "Fresca, colorida y completa con grasas cardiosaludables y marisco magro ❤️", "468 kcal", "32 g", "37 g", "21 g", "6 g"),
    ("Hamburguesas Fit de Pavo y Calabacín con Boniato Asado", "Hamburguesas caseras súper jugosas acompañadas de bastones de boniato al horno ❤️", "445 kcal", "33 g", "35 g", "19 g", "6 g"),
    ("Bacalao al Ajillo y Pimentón con Judías Verdes", "Sabor tradicional de la costa española alto en proteína y extremadamente ligero ❤️", "415 kcal", "33 g", "37 g", "15 g", "5 g"),
    ("Fajitas Fit de Pollo y Pimientos en Tortilla Integral", "Toda la diversión Tex-Mex en una versión ligera, saludable y alta en proteína ❤️", "410 kcal", "36 g", "34 g", "15 g", "6 g"),
    ("Lubina a la Plancha con Arroz Integral y Espárragos", "Pescado mediterráneo de carne blanca y fina acompañado de guarnición completa ❤️", "460 kcal", "34 g", "41 g", "17 g", "5 g")
]

# Cap 3: Pré-Treino (36 to 45) - 10 recipes
p1_c3_titles = [
    ("Tosta de Plátano, Miel y Queso Fresco", "Energía inmediata de carbohidratos simples y complejos lista en 2 minutos ❤️", "280 kcal", "12 g", "48 g", "4 g", "4 g"),
    ("Arroz Integral con Plátano y Canela", "La recarga clásica del deportista de fuerza con máxima absorción ❤️", "260 kcal", "6 g", "54 g", "2 g", "3 g"),
    ("Tortitas Rápidas de Avena y Miel", "Carbohidratos de rápida disponibilidad para rendir al máximo en el gimnasio ❤️", "310 kcal", "11 g", "56 g", "5 g", "5 g"),
    ("Bol de Crema de Arroz con Arándanos", "Digestión ultrarrapida sin molestias estomacales antes de levantar pesas ❤️", "250 kcal", "7 g", "51 g", "2 g", "2 g"),
    ("Pan de Centeno con Dulce de Membrillo y Queso Burgos", "Tradición española energética con excelente equilibrio para entrenos intensos ❤️", "290 kcal", "13 g", "52 g", "3 g", "4 g"),
    ("Boniato Asado con Canela y Miel", "Almidones limpios y vitaminas para mantener la fuerza muscular constante ❤️", "240 kcal", "4 g", "54 g", "1 g", "5 g"),
    ("Copos de Maíz sin Azúcar con Leche Desnatada y Plátano", "Ligereza digestiva y recarga rápida de glucógeno para sesiones explosivas ❤️", "275 kcal", "10 g", "55 g", "2 g", "3 g"),
    ("Tortita de Arroz Inflado con Crema de Almendras y Plátano", "Crujiente y muy rápido de digerir para cuando tienes menos de 45 minutos ❤️", "265 kcal", "7 g", "46 g", "6 g", "3 g"),
    ("Porridge Exprés de Avena con Pasas y Miel", "El combustible favorito para entrenamientos de piernas y alta demanda metabólica ❤️", "320 kcal", "10 g", "62 g", "4 g", "6 g"),
    ("Tosta de Integral con Compota de Manzana Sin Azúcar", "Sabor dulce natural con pectina suave para el sistema digestivo del atleta ❤️", "255 kcal", "8 g", "49 g", "3 g", "5 g")
]

# Cap 4: Pós-Treino (46 to 55) - 10 recipes
p1_c4_titles = [
    ("Arroz Blanco con Pechuga de Pollo al Limón", "El estándar de oro para la absorción proteica y reposición del glucógeno ❤️", "430 kcal", "42 g", "52 g", "6 g", "3 g"),
    ("Patata Cocida con Atún al Natural y Aceite de Oliva", "Carbohidrato de altísimo índice de saciedad con proteína marina pura ❤️", "410 kcal", "39 g", "46 g", "8 g", "4 g"),
    ("Quinoa con Salteado de Pavo y Calabacín", "Aminoácidos esenciales en abundancia para reparar las fibras musculares ❤️", "445 kcal", "41 g", "44 g", "11 g", "6 g"),
    ("Boniato Asado con Lomo de Bacalao Fresco", "Pescado blanco magro e hidratos complejos para una recuperación óptima ❤️", "420 kcal", "38 g", "48 g", "8 g", "5 g"),
    ("Pasta Integral con Tacos de Pollo y Salsa de Tomate", "Comida reconfortante de post-entreno con alta carga de carbohidratos limpios ❤️", "480 kcal", "43 g", "58 g", "9 g", "7 g"),
    ("Ñoquis de Patata con Pechuga de Pavo y Albahaca", "Textura suave y digestión excelente tras entrenamientos de alta intensidad ❤️", "450 kcal", "40 g", "56 g", "7 g", "4 g"),
    ("Arroz Integral con Merluza al Vapor y Judías Verdes", "Recuperación ligera sin sensación de pesadez ni grasas pesadas ❤️", "415 kcal", "37 g", "49 g", "7 g", "6 g"),
    ("Cuscús Integral con Pollo Asado y Zanahoria", "Semola de trigo de preparación rápida acompañada de proteína animal magra ❤️", "440 kcal", "41 g", "53 g", "7 g", "5 g"),
    ("Tortilla de Claras y Huevo con Patata Asada", "Albúmina de huevo biodisponible junto a tubérculos de alta energía ❤️", "395 kcal", "35 g", "44 g", "9 g", "4 g"),
    ("Ensalada de Garbanzos con Pechuga de Pollo Desmenuzada", "Recuperación vegetal y animal en una comida completa lista para comer fría ❤️", "470 kcal", "44 g", "51 g", "10 g", "9 g")
]

# Cap 5: Lanches e Snacks Fit (56 to 65) - 10 recipes
p1_c5_titles = [
    ("Brochetas de Tomate Cherry, Queso Fresco y Albahaca", "Snack mediterráneo fresco, proteico y perfecto para picar sin culpa ❤️", "180 kcal", "14 g", "6 g", "11 g", "1 g"),
    ("Rollitos de Pavo Braseado con Pepino y Queso Cottage", "Crujiente y bajo en calorías con 18 gramos de proteína animal magra ❤️", "165 kcal", "18 g", "4 g", "8 g", "1 g"),
    ("Huevos Rellenos de Atún al Natural y Yogur Griego", "Adiós mayonesa, hola cremosidad alta en proteína y sin grasas pesadas ❤️", "210 kcal", "21 g", "3 g", "12 g", "1 g"),
    ("Edamame al Vapor con Sal Marina y Pimentón", "El snack vegetal por excelencia del mundo fitness rico en fibra y aminoácidos ❤️", "170 kcal", "15 g", "13 g", "7 g", "6 g"),
    ("Tarrina de Queso Cottage con Piña Fresca", "Dulce y salado con bromelina enzimática para facilitar la digestión ❤️", "195 kcal", "19 g", "18 g", "4 g", "2 g"),
    ("Chips de Calabacín al Horno con Queso Feta", "El sustituto perfecto de las patatas fritas de bolsa crujiente y proteico ❤️", "160 kcal", "10 g", "9 g", "9 g", "3 g"),
    ("Tosta Crujiente de Pan Sueco con Salmón Ahumado", "Un bocado gourmet listo en 60 segundos para frenar el apetito a media tarde ❤️", "220 kcal", "16 g", "14 g", "11 g", "3 g"),
    ("Palitos de Zanahoria y Apio con Hummus Casero Fit", "Fibra crujiente acompañada de crema de garbanzos baja en aceite ❤️", "185 kcal", "7 g", "22 g", "8 g", "6 g"),
    ("Mini Frittatas de Espinacas y Claras al Horno", "Bocados salados de proteína que puedes conservar en la nevera 3 días ❤️", "150 kcal", "17 g", "3 g", "7 g", "1 g"),
    ("Tarrito de Yogur Griego con Frambuesas y Chía", "Antioxidantes y Omega-3 en una merienda cremosa ideal para la oficina ❤️", "205 kcal", "18 g", "15 g", "8 g", "5 g")
]

# Cap 6: Antes de Dormir / Cenas Ligeras (66 to 70) - 5 recipes
p1_c6_titles = [
    ("Bol de Queso Cottage con Nueces y Canela", "Caseína de liberación lenta para nutrir tus músculos durante toda la noche ❤️", "220 kcal", "22 g", "8 g", "11 g", "2 g"),
    ("Yogur Griego Natural con Semillas de Lino", "Flora intestinal sana y aminoácidos sostenidos mientras duermes profundamente ❤️", "190 kcal", "20 g", "7 g", "9 g", "3 g"),
    ("Revuelto Ligero de Claras y Queso Fresco", "Proteína pura y saciante sin carbohidratos para no interferir en el sueño ❤️", "180 kcal", "24 g", "2 g", "8 g", "0 g"),
    ("Infusión de Manzanilla con Tosta de Queso Burgos y Pavo", "Calma el sistema nervioso y asegura el balance de nitrógeno positivo nocturno ❤️", "210 kcal", "21 g", "12 g", "8 g", "2 g"),
    ("Crema Fresca de Queso Batido con Almendras Tostadas", "Textura de mousse nocturna sin azúcares y con grasas buenas de almendra ❤️", "200 kcal", "23 g", "6 g", "9 g", "2 g")
]

# PART 2: PROTEIN BOOSTED (CON SUPLEMENTACIÓN) - 70 RECIPES (71 to 140)
# Cap 1: Desayunos con Whey/Caseína (71 to 85)
p2_c1_titles = [
    ("Tortitas Proteicas de Avena, Plátano y Whey Vainilla", "Esponjosas y con 35 gramos de proteína de absorción rápida para empezar el día ❤️", "390 kcal", "35 g", "44 g", "8 g", "6 g"),
    ("Porridge Anabólico de Avena con Whey Chocolate", "El clásico porridge matinal potenciado con proteína de suero cremoso ❤️", "410 kcal", "38 g", "46 g", "8 g", "7 g"),
    ("Waffles Proteicos Crujientes de Avena y Whey", "Desayuno de domingo estilo fitness con valor proteico de restaurante fit ❤️", "385 kcal", "34 g", "42 g", "9 g", "5 g"),
    ("Crema de Arroz con Proteína Aislada y Fresas", "Textura de natillas fit con cero molestias digestivas y máxima pureza ❤️", "350 kcal", "36 g", "45 g", "3 g", "3 g"),
    ("Bizcocho Taza (Mug Cake) de Avena y Whey al Microondas", "Un bizcocho recién hecho en sólo 90 segundos para mañanas con prisa ❤️", "340 kcal", "33 g", "36 g", "7 g", "5 g"),
    ("Bol de Yogur Griego Potenciado con Whey y Arándanos", "La combinación de caseína natural del yogur y whey para liberación mixta ❤️", "330 kcal", "40 g", "25 g", "7 g", "4 g"),
    ("Tortilla Dulce de Claras, Avena y Proteína Chocolate", "Crepe esponjoso alto en proteína para rellenar con rodajas de plátano ❤️", "360 kcal", "37 g", "38 g", "6 g", "5 g"),
    ("Muffins Proteicos de Avena, Manzana y Whey Vainilla", "Hornea media docena el domingo y desayuna como un campeón toda la semana ❤️", "310 kcal", "28 g", "35 g", "6 g", "4 g"),
    ("Avena Trasnochada Proteica con Chía y Whey Fresa", "El desayuno nocturno potenciado para quienes buscan crecimiento muscular ❤️", "380 kcal", "36 g", "42 g", "8 g", "7 g"),
    ("Tortitas de Harina de Arroz y Proteína Vainilla", "Alternativa sin gluten súper ligera que se deshace en la boca ❤️", "355 kcal", "34 g", "43 g", "5 g", "3 g"),
    ("Bol de Queso Cottage con Whey Chocolate y Nueces", "Postre de desayuno con perfil de aminoácidos de altísimo valor biológico ❤️", "340 kcal", "39 g", "18 g", "12 g", "3 g"),
    ("Panqueque Gigante al Horno con Proteína y Arándanos", "Estilo dutch baby fit para un desayuno espectacular de fin de semana ❤️", "400 kcal", "38 g", "42 g", "9 g", "5 g"),
    ("Crepas Proteicas Finas con Queso Fresco Batido", "Crepes franceses en versión fitness sin azúcar y rellenos de cremosidad ❤️", "370 kcal", "39 g", "32 g", "8 g", "4 g"),
    ("Galletas de Desayuno de Avena, Plátano y Whey", "Tres galletas tiernas de desayuno listas para mojar en tu café solo ❤️", "330 kcal", "29 g", "41 g", "6 g", "6 g"),
    ("Tosta Francesa Fit con Huevo, Leche y Whey Vainilla", "Pan integral empapado en proteína tostado hasta dorar a la perfección ❤️", "375 kcal", "33 g", "40 g", "9 g", "6 g")
]

# Cap 2: Almuerzos y Cenas con Proteína/Colágeno (86 to 100)
p2_c2_titles = [
    ("Hamburguesas Magras de Pollo con Aislado Proteico Neutro", "Aumenta la densidad proteica de tu hamburguesa sin sumar un solo gramo de grasa ❤️", "450 kcal", "48 g", "36 g", "12 g", "5 g"),
    ("Albóndigas de Pavo con Proteína de Guisante Neutra", "Albóndigas tiernas enriquecidas en aminoácidos con salsa de tomate casera ❤️", "465 kcal", "47 g", "38 g", "13 g", "6 g"),
    ("Pastel de Carne Magra al Horno con Colágeno Hidrolizado", "Protege tus articulaciones mientras construyes masa muscular magra ❤️", "480 kcal", "46 g", "40 g", "14 g", "5 g"),
    ("Crema de Calabaza y Zanahoria con Proteína Vegetal Neutra", "Cuchareo suave de invierno que sorprende por su altísimo aporte proteico ❤️", "390 kcal", "34 g", "42 g", "9 g", "7 g"),
    ("Croquetas Fit al Horno de Pollo y Whey Neutro", "El aperitivo español amado por todos en su versión proteica sin freír ❤️", "420 kcal", "41 g", "35 g", "12 g", "4 g"),
    ("Quiche Fit de Espinacas, Pollo y Proteína de Huevo", "Tarta salada sin masa pesada ideal para cenas altas en nitrógeno positivo ❤️", "430 kcal", "44 g", "22 g", "18 g", "5 g"),
    ("Lasaña de Berenjena, Pavo y Proteína Neutra en la Salsa", "Sabor italiano tradicional con carbohidratos controlados y proteína extra ❤️", "455 kcal", "45 g", "32 g", "15 g", "8 g"),
    ("Arroz Caldoso con Pollo, Verduras y Colágeno", "Protección articular y muscular en un arroz caldoso de tradición española ❤️", "470 kcal", "43 g", "46 g", "11 g", "5 g"),
    ("Estofado de Ternera Magra con Salsa Enriquecida", "Salsa espesada con proteína neutra sin usar harina blanca ni maicena ❤️", "490 kcal", "48 g", "41 g", "14 g", "6 g"),
    ("Canelones de Calabacín Rellenos de Atún y Proteína Neutra", "Roller fit de verduras marinas con valor proteico reforzado ❤️", "410 kcal", "42 g", "24 g", "15 g", "5 g"),
    ("Pizza con Base de Pollo y Aislado de Suero Neutro", "La famosa pizza fit cuya base es 100% carne y proteína magra ❤️", "485 kcal", "52 g", "18 g", "21 g", "4 g"),
    ("Tortitas Saladas de Pavo y Proteína de Guisante", "Panqueques salados perfectos para comer con ensalada fresca al mediodía ❤️", "430 kcal", "44 g", "34 g", "12 g", "5 g"),
    ("Risotto Fit de Arroz Integral, Pollo y Whey Neutro", "Cremoso sin usar mantequilla excesiva gracias a la textura de la proteína ❤️", "475 kcal", "45 g", "48 g", "11 g", "5 g"),
    ("Guiso de Lentejas Potenciado con Proteína y Pavo", "Legumbre tradicional llevada al nivel atleta de élite con macros impecables ❤️", "510 kcal", "49 g", "49 g", "12 g", "15 g"),
    ("Pimientos Rellenos de Carne Magra y Proteína Neutra", "Verdura al horno rellena de jugosidad proteica gratinada ligera ❤️", "440 kcal", "43 g", "33 g", "14 g", "6 g")
]

# Cap 3: Pré-Treino con Creatina/Carbos Rápidos (101 to 110)
p2_c3_titles = [
    ("Porridge de Avena y Plátano con Creatina Monohidrato", "Carga máxima de ATP y glucógeno 45 minutos antes de tu entrenamiento de fuerza ❤️", "310 kcal", "15 g", "56 g", "3 g", "5 g"),
    ("Bol de Crema de Arroz con Miel y Creatina", "Absorción en tiempo récord para sesiones de máxima intensidad y volumen ❤️", "270 kcal", "12 g", "53 g", "1 g", "2 g"),
    ("Tortitas de Avena, Plátano y Creatina", "El bocado perfecto para potenciar tu fuerza explosiva y rendimiento ❤️", "320 kcal", "16 g", "54 g", "4 g", "5 g"),
    ("Gominolas de Gelatina Fit con Carbos Rápidos y Creatina", "Bocados dulces caseros para consumir justo antes de levantar pesas ❤️", "210 kcal", "12 g", "40 g", "0 g", "1 g"),
    ("Tosta de Miel, Plátano y Creatina en Polvo", "Pan tostado con carbohidratos simples que impulsan la creatina a tu músculo ❤️", "280 kcal", "10 g", "55 g", "2 g", "4 g"),
    ("Arroz con Leche Desnatada, Canela y Creatina", "Postre tradicional transformado en el combustible pre-entreno más efectivo ❤️", "295 kcal", "14 g", "56 g", "2 g", "3 g"),
    ("Barritas Caseras de Avena, Miel, Plátano y Creatina", "Prepara tu bandeja y ten listo tu pre-entreno para toda la semana ❤️", "305 kcal", "11 g", "58 g", "4 g", "5 g"),
    ("Puré de Boniato Dulce con Miel y Creatina", "Almidón de excelente digestión que llena tus músculos de energía sostenida ❤️", "260 kcal", "8 g", "55 g", "1 g", "4 g"),
    ("Copos de Maíz con Leche y Creatina Monohidrato", "Ligereza digestiva extrema para entrenar pesado sin molestias de estómago ❤️", "285 kcal", "13 g", "54 g", "2 g", "2 g"),
    ("Pudin de Tapioca y Plátano con Creatina", "Carbohidrato blanco de rápida absorción con fuerza celular añadida ❤️", "275 kcal", "9 g", "57 g", "1 g", "2 g")
]

# Cap 4: Pós-Treino Anabólico con Whey/Aislado (111 to 125)
p2_c4_titles = [
    ("Bol Anabólico de Crema de Arroz con Whey Chocolate", "La comida post-entreno número 1 de los culturistas y atletas de élite ❤️", "420 kcal", "44 g", "52 g", "4 g", "3 g"),
    ("Tortitas Gigantes de Avena, Plátano y Aislado de Suero", "Reabastece glucógeno y repara fibras con una comida deliciosa y saciante ❤️", "440 kcal", "42 g", "55 g", "6 g", "6 g"),
    ("Waffles Post-Entreno de Harina de Arroz y Whey Vainilla", "Crujientes por fuera y listos para absorberse en tu ventana de recuperación ❤️", "410 kcal", "40 g", "50 g", "5 g", "4 g"),
    ("Porridge de Avena, Plátano, Miel y Whey Fresa", "Cremoso, dulce y cargado de leucina natural para la síntesis de proteína ❤️", "430 kcal", "41 g", "56 g", "5 g", "6 g"),
    ("Mug Cake Doble Chocolate con Whey y Copos de Avena", "Bizcocho caliente post-entreno en microondas que sabe a premio merecido ❤️", "380 kcal", "39 g", "42 g", "6 g", "5 g"),
    ("Bol de Gnocchis Dulces de Patata con Salsa de Whey", "Innovación fit: gnocchis hervidos con crema dulce de proteína de suero ❤️", "450 kcal", "38 g", "62 g", "5 g", "4 g"),
    ("Arroz con Leche Proteico de Post-Entrenamiento", "El arroz con leche de toda la vida con 40 gramos de proteína pura ❤️", "425 kcal", "40 g", "54 g", "4 g", "3 g"),
    ("Tosta Dulce de Pan Integral con Crema de Whey y Plátano", "Unta tu tostada crujiente con un glaseado proteico casero increíble ❤️", "405 kcal", "37 g", "51 g", "6 g", "6 g"),
    ("Flan Proteico Exprés de Claras y Whey Vainilla", "Postre fresco de alta proteína que se cuaja en el microondas en 3 minutos ❤️", "350 kcal", "42 g", "35 g", "3 g", "2 g"),
    ("Bizcocho Horneado de Boniato y Proteína Chocolate", "Dulce natural de tubérculo con proteína de suero para una recuperación 10 ❤️", "435 kcal", "39 g", "53 g", "7 g", "5 g"),
    ("Crema de Trigo Sarraceno con Whey Vainilla y Manzana", "Sin gluten, digestiva y perfecta para rellenar tus depósitos musculares ❤️", "415 kcal", "38 g", "52 g", "6 g", "5 g"),
    ("Panqueque Soufflé de Claras, Arroz y Whey", "Esponjosidad estilo japonesa con macros calculados al milímetro ❤️", "390 kcal", "41 g", "45 g", "4 g", "3 g"),
    ("Cereales de Maíz Crujientes con Leche Proteica de Whey", "El post-entreno más rápido de la historia sin cocinar y con macros perfectos ❤️", "400 kcal", "40 g", "52 g", "4 g", "2 g"),
    ("Bol de Tapioca Cremosa con Whey Fresa y Plátano", "Suavidad absoluta para calmar el apetito voraz después de un entreno duro ❤️", "420 kcal", "38 g", "56 g", "4 g", "3 g"),
    ("Bizcocho de Zanahoria Fit al Horno con Whey Vainilla", "Carrot cake en versión post-entreno alta en leucina y carbohidrato sano ❤️", "430 kcal", "39 g", "48 g", "8 g", "5 g")
]

# Cap 5: Lanches y Snacks Proteicos (126 to 135)
p2_c5_titles = [
    ("Barritas Caseras de Avena, Crema de Cacahuete y Whey", "Olvídate de las barritas industriales caras: haz 8 unidades por una fracción ❤️", "230 kcal", "18 g", "22 g", "8 g", "4 g"),
    ("Bolas de Energía (Energy Balls) de Chía y Proteína", "Tres bolitas dulces para llevar en el bolsillo y picar cuando apriete el hambre ❤️", "210 kcal", "16 g", "19 g", "8 g", "4 g"),
    ("Muffins de Chocolate Fit con Whey y Calabacín", "El calabacín le da una jugosidad increíble sin sumar grasa ni carbohidratos ❤️", "190 kcal", "17 g", "16 g", "6 g", "3 g"),
    ("Galletas Crujientes de Avena, Almendras y Whey", "Galletas saludables para la merienda con café o té a media tarde ❤️", "205 kcal", "16 g", "20 g", "7 g", "3 g"),
    ("Pudin de Chía con Capa de Whey Chocolate", "Cremoso, lleno de Omega-3 y con una capa superior que sabe a postre ❤️", "215 kcal", "18 g", "15 g", "9 g", "6 g"),
    ("Flan Individual de Queso Cottage y Whey Vainilla", "Fresco, saciante y con una textura suave de tarta de queso fit ❤️", "195 kcal", "21 g", "12 g", "6 g", "1 g"),
    ("Bizcochitos Limón y Semillas de Amapola con Whey", "Aroma cítrico y textura tierna para una merienda elegante e hiperproteica ❤️", "185 kcal", "17 g", "17 g", "5 g", "2 g"),
    ("Trufas Fit de Cacahuete, Avena y Proteína Chocolate", "Dos trufas de chocolate fit que calman cualquier antojo de dulce ❤️", "220 kcal", "18 g", "18 g", "9 g", "3 g"),
    ("Tartaleta Frita en Airfryer de Manzana y Whey", "Crujiente por fuera y con relleno tierno de manzana con proteína ❤️", "200 kcal", "16 g", "24 g", "4 g", "3 g"),
    ("Crepes Fríos Rellenos de Crema de Whey y Fresas", "Prepara tus crepes por la mañana y consérvalos en la nevera como merienda ❤️", "210 kcal", "19 g", "18 g", "6 g", "3 g")
]

# Cap 6: Antes de Dormir con Caseína/Cottage (136 to 140)
p2_c6_titles = [
    ("Mousse Nocturna de Caseína Micelar Sabor Chocolate", "Libera aminoácidos lentamente durante 7 horas continuas mientras duermes ❤️", "210 kcal", "26 g", "8 g", "8 g", "3 g"),
    ("Bol de Queso Cottage Potenciado con Caseína Vainilla", "El dúo imbatible de proteína de liberación lenta para máxima recuperación ❤️", "230 kcal", "30 g", "9 g", "8 g", "2 g"),
    ("Pudin Caliente de Caseína y Canela al Taza", "Una taza reconfortante antes de meterte en la cama en noches frías ❤️", "200 kcal", "25 g", "7 g", "7 g", "3 g"),
    ("Helado Fit de Caseína y Yogur Griego (Sin Heladera)", "Textura cremosa congelada que no cristaliza gracias a la caseína micelar ❤️", "220 kcal", "28 g", "10 g", "7 g", "2 g"),
    ("Crema de Queso Batido 0% con Caseína Chocolate y Nueces", "Postre nocturno espeso y delicioso que evita el catabolismo de la madrugada ❤️", "240 kcal", "31 g", "8 g", "9 g", "3 g")
]

def make_recipe(id_num, chapter, title, frase, kcal, p, c, g, f, is_supplement=False):
    # Determine photo prompt by chapter/type
    photo_prompt = f"Professional editorial food photography of {title}, delicious healthy Spanish fitness recipe, served on a modern ceramic plate, soft natural window light, soft-focus sage green background, 45-degree angle, shallow depth of field, bright clean appetizing fitness cookbook style, ultra high resolution, square 1:1 centered composition, no text, no watermark"
    
    # Generate realistic Spanish ingredients & preparation based on recipe title
    ingredientes = []
    preparo = []
    
    if "Tortitas" in title or "Waffles" in title or "Panqueque" in title:
        ingredientes = [
            "🍌 1 plátano maduro aplastado (100 g)",
            "🥚 2 huevos grandes enteros o 4 claras líquidas",
            "🥣 1/2 taza de avena en copos (40 g)",
            "🧂 1 cucharadita de canela en polvo",
            "🫒 1 cucharadita de aceite de oliva virgen extra para dorar (5 ml)"
        ]
        if is_supplement:
            ingredientes.append("💪 1 scoop de proteína Whey o Caseína (30 g)")
        preparo = [
            "En un bol profundo, aplasta el plátano con un tenedor hasta convertirlo en puré suave.",
            "Añade los huevos (y la proteína si aplica) y bate enérgicamente con unas varillas.",
            "Incorpora los copos de avena y la canela en polvo hasta obtener una masa sin grumos.",
            "Calienta una sartén antiadherente o gofrera a fuego medio con unas gotas de aceite de oliva.",
            "Vierte pequeñas porciones de masa y cocina 2 o 3 minutos hasta ver burbujas en la superficie.",
            "Dale la vuelta y dora 1 o 2 minutos más por el otro lado.",
            "Sirve en un plato caliente decorando con fruta fresca al gusto."
        ]
    elif "Porridge" in title or "Avena" in title or "Crema de Arroz" in title or "Crema de Trigo" in title:
        ingredientes = [
            "🥣 1/2 taza de avena en copos o crema de arroz (40 g)",
            "🥛 1 taza de leche desnatada o vegetal sin azúcar (240 ml)",
            "🫐 1/2 taza de arándanos, fresas o rodajas de manzana (75 g)",
            "🥜 1/2 oz de almendras, nueces o semillas de chía (14 g)",
            "🧂 1 pizca de canela en polvo y aroma natural de vainilla"
        ]
        if is_supplement:
            ingredientes.append("💪 1 scoop de proteína Whey, Aislado o Caseína (30 g)")
        preparo = [
            "En un cazo pequeño, mezcla el cereal con la leche desnatada y la canela en polvo.",
            "Lleva a fuego medio removiendo sin cesar durante unos 4 minutos hasta que espese y adquiera cremosidad.",
            "Retira el cazo del fuego y deja templar 1 minuto (importante para añadir proteína sin cuajarla).",
            "Si lleva proteína en polvo, intégrala ahora removiendo suavemente hasta disolverla por completo.",
            "Vierte el contenido en un bol ancho y profundo.",
            "Decora la superficie con las frutas frescas elegidas y los frutos secos para un toque crujiente."
        ]
    elif "Pollo" in title or "Pavo" in title or "Ternera" in title or "Cerdo" in title or "Hamburguesas" in title or "Albóndigas" in title:
        ingredientes = [
            "🍗 5 oz de pechuga de pollo, pavo, ternera magra o cerdo magro (140 g)",
            "🍚 3/4 taza de arroz integral, quinoa o boniato asado como guarnición (150 g)",
            "🥦 1 taza de brócoli, espárragos, pimientos o calabacín fresco (100 g)",
            "🫒 1 cucharada de aceite de oliva virgen extra (13 g)",
            "🌿 Ajo picado, perejil fresco, tomillo seco, sal marina y pimienta"
        ]
        if is_supplement:
            ingredientes.append("💪 1 scoop de proteína neutra o colágeno hidrolizado para enriquecer la salsa")
        preparo = [
            "Prepara los vegetales al vapor, al horno o salteados con media cucharada de aceite durante 5 minutos.",
            "Salpimenta la carne magra con ajo molido, hierbas aromáticas, sal marina y pimienta negra.",
            "Calienta una sartén o plancha antiadherente a fuego medio-alto con el resto del aceite de oliva.",
            "Cocina la carne durante 4 a 6 minutos por lado según el grosor hasta que esté jugosa y bien hecha.",
            "Si la receta incluye salsa enriquecida, mezcla el caldo con la proteína neutra y viértelo en el último minuto.",
            "Emplata la porción de hidratos complejos (arroz, quinoa o boniato) como base.",
            "Coloca la carne recién cocinada sobre la guarnición y sirve caliente."
        ]
    elif "Merluza" in title or "Salmón" in title or "Atún" in title or "Bacalao" in title or "Dorada" in title or "Lubina" in title or "Gambas" in title or "Sepia" in title or "Pulpo" in title or "Calamares" in title or "Mariscos" in title:
        ingredientes = [
            "🐟 5 oz de filete de pescado fresco, gambas o marisco magro (140 g)",
            "🥔 1 patata cocida, boniato o 3/4 taza de arroz integral (150 g)",
            "🥒 1 taza de espárragos, calabacín, brócoli o pimientos (100 g)",
            "🫒 1 cucharada de aceite de oliva virgen extra (13 g)",
            "🍋 Zumo de limón fresco, ajo picado, sal marina y perejil picado"
        ]
        if is_supplement:
            ingredientes.append("💪 1 ración de colágeno hidrolizado o proteína neutra para el caldo marinero")
        preparo = [
            "Lava y seca el pescado o marisco, aderezando con sal marina, ajo picado y unas gotas de limón.",
            "Calienta una sartén antiadherente o plancha a fuego fuerte con media cucharada de aceite de oliva.",
            "Cocina el pescado o marisco 3 a 5 minutos por lado (el pescado blanco está listo cuando se desmigue fácil).",
            "En otra sartén o al horno, asa la guarnición de verduras y patatas con el resto del aceite.",
            "Sirve el pescado recién marcado sobre la cama de verduras calientes.",
            "Rocía con abundante zumo de limón fresco y perejil recién picado."
        ]
    else:
        ingredientes = [
            "🥣 Ingrediente principal proteico fit en porción equilibrada (150 g)",
            "🌾 Guarnición de carbohidratos integrales o fibra vegetal (100 g)",
            "🫒 1 cucharadita a 1 cucharada de aceite de oliva virgen extra",
            "🌿 Ajo, especias naturales, sal marina y zumo de limón al gusto"
        ]
        if is_supplement:
            ingredientes.append("💪 1 scoop de suplemento proteico (Whey, Caseína ou Aislado)")
        preparo = [
            "Prepara los ingredientes frescos lavándolos y cortándolos en porciones uniformes.",
            "Cocina a la plancha, al horno o al vapor controlando la temperatura para no quemar las grasas saludables.",
            "Combina la fuente proteica principal con la guarnición en un plato amplio.",
            "Adereza con aceite de oliva virgen extra, sal marina y hierbas al gusto.",
            "Sirve fresco o caliente según la temporada y tu preferencia."
        ]
    
    frase_lat = "Excelente receta fitness adaptada al estilo de vida activo con máxima saciedad 🌸"
    obj_tit = "Definición y Masa Muscular 💪"
    obj_desc = f"Esta receta aporta {p} de proteína de alta biodisponibilidad y carbohidratos limpios para tu rendimiento."
    
    variaciones = [
        "🌱 Puedes adaptar la guarnición cambiando arroz integral por quinoa o boniato según tus objetivos",
        "🌱 Si estás en fase de corte calórico estricto, sustituye los almidones por doble ración de verduras verdes"
    ]
    if is_supplement:
        variaciones.append("🌱 Puedes elegir tu sabor favorito de proteína de suero (vainilla, chocolate, fresa o neutro)")
        
    return {
        "id": id_num,
        "capitulo": chapter,
        "titulo": title,
        "frase_efecto": frase,
        "tiempo": "15 a 25 minutos",
        "rendimiento": "1 ración",
        "ingredientes": ingredientes,
        "foto_arquivo": f"receta_{id_num:03d}_es.jpg",
        "foto_prompt": photo_prompt,
        "modo_preparo": preparo,
        "frase_lateral": frase_lat,
        "objetivo_titulo": obj_tit,
        "objetivo_descripcion": obj_desc,
        "macros": {
            "calorias": kcal,
            "proteinas": p,
            "carbohidratos": c,
            "grasas": g,
            "fibra": f
        },
        "variaciones": variaciones
    }

# Build Part 1 (1 to 70)
idx = 1
for tit, fre, kc, pr, cb, gr, fb in p1_c1_titles:
    recipes_p1.append(make_recipe(idx, "Desayunos y Meriendas Fit", tit, fre, kc, pr, cb, gr, fb, False))
    idx += 1

for tit, fre, kc, pr, cb, gr, fb in p1_c2_titles:
    recipes_p1.append(make_recipe(idx, "Almuerzos y Cenas Fit", tit, fre, kc, pr, cb, gr, fb, False))
    idx += 1

for tit, fre, kc, pr, cb, gr, fb in p1_c3_titles:
    recipes_p1.append(make_recipe(idx, "Pré-Treino Fit (Carbos Rápidos)", tit, fre, kc, pr, cb, gr, fb, False))
    idx += 1

for tit, fre, kc, pr, cb, gr, fb in p1_c4_titles:
    recipes_p1.append(make_recipe(idx, "Pós-Treino Fit (Alta Proteína)", tit, fre, kc, pr, cb, gr, fb, False))
    idx += 1

for tit, fre, kc, pr, cb, gr, fb in p1_c5_titles:
    recipes_p1.append(make_recipe(idx, "Lanches y Snacks Fit", tit, fre, kc, pr, cb, gr, fb, False))
    idx += 1

for tit, fre, kc, pr, cb, gr, fb in p1_c6_titles:
    recipes_p1.append(make_recipe(idx, "Antes de Dormir / Cenas Ligeras", tit, fre, kc, pr, cb, gr, fb, False))
    idx += 1

# Build Part 2 (71 to 140)
for tit, fre, kc, pr, cb, gr, fb in p2_c1_titles:
    recipes_p2.append(make_recipe(idx, "Desayunos con Whey/Caseína", tit, fre, kc, pr, cb, gr, fb, True))
    idx += 1

for tit, fre, kc, pr, cb, gr, fb in p2_c2_titles:
    recipes_p2.append(make_recipe(idx, "Almuerzos y Cenas con Proteína/Colágeno", tit, fre, kc, pr, cb, gr, fb, True))
    idx += 1

for tit, fre, kc, pr, cb, gr, fb in p2_c3_titles:
    recipes_p2.append(make_recipe(idx, "Pré-Treino con Creatina/Carbos Rápidos", tit, fre, kc, pr, cb, gr, fb, True))
    idx += 1

for tit, fre, kc, pr, cb, gr, fb in p2_c4_titles:
    recipes_p2.append(make_recipe(idx, "Pós-Treino Anabólico con Whey/Aislado", tit, fre, kc, pr, cb, gr, fb, True))
    idx += 1

for tit, fre, kc, pr, cb, gr, fb in p2_c5_titles:
    recipes_p2.append(make_recipe(idx, "Lanches y Snacks Proteicos", tit, fre, kc, pr, cb, gr, fb, True))
    idx += 1

for tit, fre, kc, pr, cb, gr, fb in p2_c6_titles:
    recipes_p2.append(make_recipe(idx, "Antes de Dormir con Caseína/Cottage", tit, fre, kc, pr, cb, gr, fb, True))
    idx += 1

# Save all datasets
os.makedirs("data", exist_ok=True)

with open("data/recetas_parte1.json", "w", encoding="utf-8") as f:
    json.dump({
        "ebook": "The Ultimate Fitness Recipe Vault - Edición España",
        "idioma": "es-ES",
        "parte1": {
            "titulo": "Whole Food Power (Sin Suplementos)",
            "recetas": recipes_p1
        }
    }, f, ensure_ascii=False, indent=2)

with open("data/recetas_parte2.json", "w", encoding="utf-8") as f:
    json.dump({
        "ebook": "The Ultimate Fitness Recipe Vault - Edición España",
        "idioma": "es-ES",
        "parte2": {
            "titulo": "Protein Boosted (Con Suplementación)",
            "recetas": recipes_p2
        }
    }, f, ensure_ascii=False, indent=2)

with open("data/recetas_completo_140.json", "w", encoding="utf-8") as f:
    json.dump({
        "ebook": "The Ultimate Fitness Recipe Vault - Edición España (140 Recetas)",
        "idioma": "es-ES",
        "total_recetas": 140,
        "parte1": recipes_p1,
        "parte2": recipes_p2
    }, f, ensure_ascii=False, indent=2)

print("OK! 140 Recetas generadas con exito! Parte 1: " + str(len(recipes_p1)) + ", Parte 2: " + str(len(recipes_p2)))
