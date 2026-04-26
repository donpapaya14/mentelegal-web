"""
Planifica temas evitando duplicados y rotando categorías.
Lee artículos existentes en src/content/blog/ para evitar repetir.
"""

import os
import random
import re
from pathlib import Path

BLOG_DIR = Path(__file__).parent.parent / "src" / "content" / "blog"

CATEGORIES = ["consumidor", "laboral", "vivienda", "tramites", "reclamaciones"]

ARTICLE_FORMULAS = {
    "consumidor": [
        "Derecho del consumidor con articulo de ley EXACTO, ejemplo de uso y como reclamar paso a paso",
        "Estafa comun y como protegerte legalmente con referencia a ley y organismo donde denunciar",
        "Devolucion o garantia: tus derechos REALES con plazos legales exactos y modelo de reclamacion",
    ],
    "laboral": [
        "Derecho laboral que pocos conocen con articulo del Estatuto de los Trabajadores y ejemplo real",
        "Que hacer si te despiden: guia paso a paso con plazos legales, cantidades de indemnizacion y donde reclamar",
        "Derechos en el trabajo que tu empresa no te cuenta con leyes concretas y como exigirlos",
    ],
    "vivienda": [
        "Derecho del inquilino con articulo de la LAU y ejemplo de aplicacion practica",
        "Problemas con el casero: que dice la ley EXACTAMENTE y como actuar paso a paso",
        "Gastos de comunidad: que puedes y que no puedes rechazar con base legal exacta",
    ],
    "tramites": [
        "Tramite legal paso a paso con documentos necesarios, plazos y coste real",
        "Como hacer [tramite especifico] online: guia completa con URLs oficiales y capturas",
        "Tramites que puedes hacer gratis y no lo sabias con enlaces directos a organismos oficiales",
    ],
    "reclamaciones": [
        "Como reclamar a [tipo de empresa] con modelo de carta, organismos y plazos legales",
        "Reclamacion exitosa paso a paso: ejemplo real con cantidades recuperadas y procedimiento",
        "Organismos gratuitos donde reclamar con nombres, URLs y tipo de casos que resuelven",
    ],
}


def get_existing_titles() -> set[str]:
    """Lee títulos de artículos existentes del frontmatter."""
    titles = set()
    if not BLOG_DIR.exists():
        return titles

    for md_file in BLOG_DIR.glob("*.md"):
        content = md_file.read_text(encoding="utf-8")
        match = re.search(r'^title:\s*["\']?(.+?)["\']?\s*$', content, re.MULTILINE)
        if match:
            titles.add(match.group(1).lower().strip())
    return titles


def get_category_counts() -> dict[str, int]:
    """Cuenta artículos por categoría."""
    counts = {cat: 0 for cat in CATEGORIES}
    if not BLOG_DIR.exists():
        return counts

    for md_file in BLOG_DIR.glob("*.md"):
        content = md_file.read_text(encoding="utf-8")
        match = re.search(r'^category:\s*["\']?(\w+)["\']?\s*$', content, re.MULTILINE)
        if match and match.group(1) in counts:
            counts[match.group(1)] += 1
    return counts


def pick_category() -> str:
    """Elige categoría con menos artículos (rotación equilibrada)."""
    counts = get_category_counts()
    min_count = min(counts.values())
    least_covered = [cat for cat, count in counts.items() if count == min_count]
    return random.choice(least_covered)


def pick_formula(category: str) -> str:
    """Elige fórmula aleatoria para la categoría."""
    formulas = ARTICLE_FORMULAS.get(category, ARTICLE_FORMULAS["nutricion"])
    return random.choice(formulas)


def plan_topic() -> dict:
    """Devuelve categoría y fórmula para el próximo artículo."""
    category = pick_category()
    formula = pick_formula(category)
    existing = get_existing_titles()

    return {
        "category": category,
        "formula": formula,
        "existing_titles": list(existing)[:20],  # Para contexto al AI
        "existing_count": len(existing),
    }
