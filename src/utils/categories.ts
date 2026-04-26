export const CATEGORIES = {
  'consumidor': { name: 'Consumidor', slug: 'consumidor', description: 'Tus derechos como consumidor con leyes reales' },
  'laboral': { name: 'Laboral', slug: 'laboral', description: 'Derechos laborales, despidos y contratos' },
  'vivienda': { name: 'Vivienda', slug: 'vivienda', description: 'Alquiler, hipotecas y comunidad de vecinos' },
  'tramites': { name: 'Tramites', slug: 'tramites', description: 'Guias paso a paso de tramites legales' },
  'reclamaciones': { name: 'Reclamaciones', slug: 'reclamaciones', description: 'Como reclamar y ganar con la ley' },
} as const;

export type Category = keyof typeof CATEGORIES;

export function getCategoryName(cat: Category): string {
  return CATEGORIES[cat].name;
}

export function getCategoryBadgeClass(cat: Category): string {
  return `badge badge--${cat}`;
}
