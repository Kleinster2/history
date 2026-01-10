# Human History Vault

Welcome to your personal knowledge base on human history.

---

## Quick Navigation

### Index Files
- [[Timeline MOC]] - Chronological overview
- [[Civilizations MOC]] - Major civilizations
- [[Themes MOC]] - Cross-cutting themes
- [[People MOC]] - Notable figures

### Time Periods
- [[01 - Prehistory/Prehistory Index|Prehistory]] - Before 3000 BCE
- [[02 - Ancient/Ancient Index|Ancient]] - 3000 BCE to 500 CE
- [[03 - Medieval/Medieval Index|Medieval]] - 500 to 1500
- [[04 - Early Modern/Early Modern Index|Early Modern]] - 1500 to 1800
- [[05 - Modern/Modern Index|Modern]] - 1800 to 1945
- [[06 - Contemporary/Contemporary Index|Contemporary]] - 1945 to Present

---

## Recently Modified
```dataview
TABLE file.mtime AS "Modified"
SORT file.mtime DESC
LIMIT 10
```

---

## Statistics
```dataview
TABLE length(rows) AS "Count"
FROM ""
WHERE type
GROUP BY type
```

---

## Getting Started

1. **Create notes** using templates in the `Templates` folder
2. **Link liberally** - connect events, people, and civilizations
3. **Use tags** - add `#event`, `#person`, `#civilization` etc.
4. **Add to MOCs** - keep index files updated

## Recommended Plugins
- **Dataview** - for dynamic queries (used in MOCs)
- **Templater** - for better template insertion
- **Calendar** - for timeline visualization
- **Graph Analysis** - to explore connections
