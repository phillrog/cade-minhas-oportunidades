import urllib.parse

class Dork:
    """Responsável estritamente pela lógica de construção das queries."""
    
    @staticmethod
    def construir(titulos, obrigatorios, regime, exclusoes) -> str:
        intitle = f"intitle:({' OR '.join([f'\"{t}\"' for t in titulos])})" if titulos else ""
        mandatory = " ".join([f'"{m}"' for m in obrigatorios])
        work_type = f"({' OR '.join([f'\"{r}\"' for r in regime])})" if regime else ""
        negate = " ".join([f"-{e}" for e in exclusoes])
        
        return f'site:br.linkedin.com (inurl:jobs/view OR inurl:posts) {intitle} {mandatory} {work_type} {negate}'.strip()

    @staticmethod
    def google_url(dork, start_date, end_date) -> str:
        query_encoded = urllib.parse.quote(dork)
        return f"https://www.google.com/search?q={query_encoded}&tbs=cdr:1,cd_min:{start_date.strftime('%m/%d/%Y')},cd_max:{end_date.strftime('%m/%d/%Y')}&sort=date:r"