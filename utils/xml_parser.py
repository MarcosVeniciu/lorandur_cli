import re

def extract_all_tags(text: str) -> dict:
    """
    Extrai tags XML/HTML de um texto de forma robusta e recursiva simples.
    Versão Limpa (Sem Debug Visual).
    """
    if not text:
        return {}

    # 1. Limpeza de Markdown (Remove ```xml ... ``` e ```)
    clean_text = re.sub(r"```[a-zA-Z]*", "", text).replace("```", "")
    
    # 2. Regex Poderoso
    # Captura <tag>conteudo</tag>, ignorando atributos (<tag id="1">) e case-insensitive
    tag_pattern = re.compile(r"<([a-zA-Z0-9_]+)[^>]*>(.*?)</\1>", re.DOTALL | re.IGNORECASE)
    
    matches = tag_pattern.findall(clean_text)
    
    result = {}
    for tag, content in matches:
        tag_clean = tag.lower().strip()
        content_clean = content.strip()
        
        # 3. Tentativa de Recursão ("Achatamento")
        # Se o conteúdo parece ter outras tags, extrai também e mistura no nível superior
        if "<" in content_clean and ">" in content_clean:
            try:
                sub_tags = extract_all_tags(content_clean)
                if sub_tags:
                    result.update(sub_tags)
            except:
                pass # Se falhar, mantém o texto original
                
        result[tag_clean] = content_clean
        
    return result