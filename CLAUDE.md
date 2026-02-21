# History Vault

A history vault viewed through the lens of **economic progress**—how humanity went from subsistence to modernity.

## The Throughline

This vault explores one central question: **How did we get here?**

From hunter-gatherers to industrial civilization, from local subsistence to global markets, from muscle power to machines—this is the story of material progress. Technology, wealth, trade, institutions, innovation: all facets of one transformation.

## What the Notes Cover

| Topic | Question It Answers |
|-------|---------------------|
| Steam Engine | How did progress happen? |
| Timber Crisis | What constraints forced innovation? |
| Great Divergence | Why did progress happen where it did? |
| Templars | How did financial innovation enable progress? |
| Florence, Venice | Who captured the gains? |
| Economic Collapse | What makes progress reverse? |
| Economic Persistence | What survives across all systems? |

## Structure

### By Period
- **01 - Prehistory** — Origins of economic behavior
- **02 - Ancient** — First civilizations, different paths
- **03 - Medieval** — Multiple centers, commercial revival
- **04 - Early Modern** — Divergence, industrialization

### Cross-Cutting Themes
- **Themes/** — Notes spanning multiple periods (Great Divergence, Wealth Through History, Economic Persistence)

## Conventions

- **Wikilinks** connect related notes: `[[Steam Engine]]`
- **Link on first mention + Related Notes** — Link a term inline when it first appears, then include in Related Notes section at the end. Don't repeat links for subsequent mentions. If a term appears in a table, prefer linking there over prose.
- **Link to relevant period** — When a civilization spans multiple periods (e.g., Egypt), link to the specific period note (e.g., `[[New Kingdom Egypt]]`) rather than the general index.
- **YAML frontmatter** provides metadata (type, period, tags)
- **Tables** present structured information
- **Sources** listed at end of each note

## Creating New Notes

1. **Check if note exists first** — Use Glob to search for the filename before creating
2. **Check for incoming links** — Search for `[[Note Name]]` in existing files to find notes that already reference the topic
3. **Add bidirectional links** — After creating a note, update related existing notes to link back to the new note
4. **Use Related Notes section** — Each note ends with links to connected topics
5. **Research predecessors** — Before writing about any innovation, ask "what came before?" The predecessor often explains why the innovation mattered. (Example: the silver florin (1237) explains why Florence switched to gold (1252).)
6. **Research founding context** — When researching an innovation, ask not just "what was it?" but: What were the founding circumstances? Who were the political actors? How did it change over time? (Example: the florin's success came partly from Florence's alliances with the Angevin Crown and Papacy—political networks that spread the coin beyond commercial use.)

## The Lens

Every note, whether about Cistercian monks or Chinese emperors, asks: what does this tell us about economic progress? How did people produce, trade, accumulate, innovate? What enabled growth, and what held it back?

This isn't economic history as a subdiscipline. It's history with economics as the throughline—the material story of how the world changed.

## Cross-Vault Awareness

Two other vaults track the present and future that this vault's history leads to:

- **Investing vault** (`C:\Users\klein\financial-charts\investing\`, Obsidian vault name `investing`, repo `Kleinster2/financial-charts`) — market positioning, company analysis, investment theses. Actor notes there include Evolution sections tracing key inflection points. This vault provides the deeper backstory.
- **Geopolitics vault** (`C:\Users\klein\obsidian\geopolitics\`, Obsidian vault name `geopolitics`, repo `Kleinster2/geopolitics`) — statecraft, alliances, power dynamics. Topics like sanctions, trade wars, balance of power, and imperial overreach have deep roots here.

**Post-creation flag:** After creating or significantly updating a note on a theme with present-day relevance (defense contracting, commodity trade routes, sanctions history, monetary systems, industrial policy, infrastructure control, etc.), flag to the user that the investing or geopolitics vaults may benefit from the historical context. This vault provides precedent; the other two apply it.

**Cross-vault links:** When a history note connects to a current analysis in the other vaults, add a clickable `obsidian://` URI link:
```markdown
### Cross-vault
- [Investing: Note Name](obsidian://open?vault=investing&file=Folder%2FNote%20Name) — current relevance
- [Geopolitics: Note Name](obsidian://open?vault=geopolitics&file=Folder%2FNote%20Name) — current relevance
```
Place under `### Cross-vault` at end of Related Notes. URL-encode paths: spaces → `%20`, slashes → `%2F`.
