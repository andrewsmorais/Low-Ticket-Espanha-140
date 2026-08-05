# -*- coding: utf-8 -*-
import json, os

data = json.load(open('data/recetas_completo_140.json', encoding='utf-8'))
md = '# 📖 Catálogo Oficial: 140 Recetas Fitness (Edición España)\n\n'
md += 'Este documento contiene el índice y resumen nutricional de las **140 recetas** completas del Ebook, estructuradas en las dos partes principales.\n\n'
md += '## Parte 1: Whole Food Power (Comida Real - Sin Suplementos)\n\n'
md += '| # | Capítulo | Título de la Receta | Calorías | Proteínas | Carbos | Grasas |\n'
md += '|---|---|---|---|---|---|---|\n'
for r in data['parte1']:
    m = r['macros']
    md += f"| #{r['id']} | {r['capitulo']} | **{r['titulo']}** | {m['calorias']} | {m['proteinas']} | {m['carbohidratos']} | {m['grasas']} |\n"

md += '\n## Parte 2: Protein Boosted (Con Suplementación: Whey, Creatina, Colágeno)\n\n'
md += '| # | Capítulo | Título de la Receta | Calorías | Proteínas | Carbos | Grasas |\n'
md += '|---|---|---|---|---|---|---|\n'
for r in data['parte2']:
    m = r['macros']
    md += f"| #{r['id']} | {r['capitulo']} | **{r['titulo']}** | {m['calorias']} | {m['proteinas']} | {m['carbohidratos']} | {m['grasas']} |\n"

art_dir = r'C:\Users\andre\.gemini\antigravity\brain\7bd301b7-d0d7-4a00-ae57-2cc7336d0acd'
os.makedirs(art_dir, exist_ok=True)
with open(os.path.join(art_dir, 'catalogo_140_recetas.md'), 'w', encoding='utf-8') as f:
    f.write(md)
with open('catalogo_140_recetas.md', 'w', encoding='utf-8') as f:
    f.write(md)

print("OK! Catalogo markdown generado con exito!")
